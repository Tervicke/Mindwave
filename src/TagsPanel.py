import tkinter as tk
import json
import app_settings

# Load settings
app_settings.load_settings()
settings = app_settings.Settings

class Tagspanel(tk.Toplevel):
    def __init__(self, master,callback,initial_tags):
        super().__init__(master)
        self.title("Tag Selector")
        self.configure(bg=settings['Background_color'])
        self.geometry("250x150")  # Set width and height
        self.configure(borderwidth=2, relief="groove")  # Add border

        # Load tags and their colors from a JSON file
        self.load_tags()

        # Dropdown menu for available tags, placed at the top-left corner
        self.tag_var = tk.StringVar(self)
        self.tag_var.set("Select a tag")
        self.tag_dropdown = tk.OptionMenu(self, self.tag_var, *self.tag_names, command=self.add_tag)
        self.tag_dropdown.grid(row=0, column=0, padx=5, pady=5, sticky="nw")  # Anchor to northwest
        self.tag_dropdown.config(bg=settings['Background_color'], fg=settings['Foreground_color'], 
                                  activebackground=settings['Background_color'], 
                                  activeforeground=settings['Foreground_color'], highlightthickness=0)

        # Button to print selected tags, placed to the right of the dropdown
        self.print_button = tk.Button(self, text="Update", command=self.print_tags,
                                       bg=settings['Theme_color'], fg='white')
        self.print_button.grid(row=0, column=1, padx=5, pady=5, sticky="ne")  # Anchor to northeast
        self.print_button.config(activebackground=settings['Theme_color'], 
                                  activeforeground="white", highlightthickness=0)

        # Main frame for tag display areas, below the dropdown and button
        self.tag_main_frame = tk.Frame(self, bg=settings['Background_color'])
        self.tag_main_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

        # Frame width is now set to the max_width
        self.max_width = 250  # Maximum width set here
        self.space_between_tags = 5  # Adjust space between tags here
        self.min_label_width = 80  # Minimum width for the label

        self.selected_tags = []
        self.refresh_tags_display()

        self.callback = callback
        self.initial_tags = initial_tags 

        #append and load the initial tags 
        for tag in self.initial_tags:
            self.selected_tags.append(tag)
        self.refresh_tags_display()

    def load_tags(self):
        """Load tags and their colors from a JSON file."""
        with open('src/tags.json', 'r') as file:
            self.tags = json.load(file)
        # Extract just the tag names for the dropdown
        self.tag_names = [tag[0] for tag in self.tags]

    def refresh_tags_display(self):
        """Refresh the display of selected tags, wrapping based on an updated width."""
        # Clear current tags display
        for widget in self.tag_main_frame.winfo_children():
            widget.destroy()

        current_frame = tk.Frame(self.tag_main_frame, bg=settings['Background_color'])
        current_frame.pack(fill='x')
        current_width = 0

        for tag_info in self.selected_tags:
            tag, bg, fg = tag_info
            lbl = tk.Label(current_frame, text=tag, bg=bg, fg=fg, padx=5)
            lbl_width = max(lbl.winfo_reqwidth(), self.min_label_width) + self.space_between_tags
            if current_width + lbl_width > self.max_width:
                current_frame = tk.Frame(self.tag_main_frame, bg=settings['Background_color'])
                current_frame.pack(fill='x', pady=5)  # Add some space between lines
                current_width = 0
            lbl.pack(side="left", padx=2)
            current_width += lbl_width
            # Bind click event to remove the tag
            lbl.bind("<Button-1>", lambda event, label=lbl: self.remove_tag(label))

    def add_tag(self, selection):
        """Add a selected tag if not already selected and refresh display."""
        for tag_info in self.tags:
            if tag_info[0] == selection and tag_info not in self.selected_tags:
                self.selected_tags.append(tag_info)
                break
        self.refresh_tags_display()

    def remove_tag(self, label):
        """Remove the selected tag."""
        text = label.cget("text")
        self.selected_tags = [tag_info for tag_info in self.selected_tags if tag_info[0] != text]
        self.refresh_tags_display()

    def print_tags(self):
        self.callback(self.selected_tags)

# Example of embedding into another application
if __name__ == "__main__":
    root = tk.Tk()
    app = TagSelectorFrame(root)
    root.mainloop()

