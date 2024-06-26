import app_settings
import tkinter as tk
from tkinter import ttk
import os 
import glob
import webbrowser
import customtkinter
class Settingspanel(tk.Toplevel):
    def __init__(self,master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.config(bg=app_settings.Settings['Background_color'])
        self.title("Settings")
        self.resizable(height=False,width=False)
        self.withdraw()
        self.protocol('WM_DELETE_WINDOW',self.close_settings)
        self.configure(borderwidth=2, relief="groove")  # Add border
    
        self.side_menu = None
        self.style = ttk.Style()

        self.colors = {"Blue":"#007AFF" , "Red":"Red" , "Green":"#34c759"}

        self.accent_label = None
        self.theme_label = None
        self.save_button = None

        self.theme_combobox= None 
        self.accent_color_combobox = None 

        self.current_row= -1;
        self.setup_accent_color()
        self.setup_theme_chooser()
        self.setup_template_chooser()
        self.setup_font_chooser()
        self.setup_streak_option()
        #save button 
        self.setup_save_button()

        #footer
        #self.setup_footer()


        self.center_window_on_screen(self)

        for i in range(self.grid_size()[0]):
            self.rowconfigure(i, weight=1)
        for i in range(self.grid_size()[0]):
            self.columnconfigure(i, weight=1)

        # Remove unnecessary padding and space between widgets
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
    def setup_accent_color(self):
        self.current_row+=1;

        self.accent_label = tk.Label(self, font=app_settings.App_font,text="Accent color:", bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'])
        self.accent_label.grid(row=self.current_row,column=0,padx=(5,0),pady=(5,0),sticky='w')

        self.accent_color_combobox = ttk.Combobox(self,state="readonly",background=app_settings.Settings['Background_color'],foreground=app_settings.Settings['Combobox_foreground'],font=app_settings.App_font,style="Custom.TCombobox")
        self.accent_color_combobox.grid(row=self.current_row, column=1,padx=(5,0),pady=(5,0))
        # Add items to the Combobox
        self.accent_color_combobox['values'] = ("Blue", "Green",  "Red" )

        # Set a default value by getting the color
        self.accent_color_combobox.set(self.get_keys_by_value(app_settings.Settings['Theme_color']))

        self.style.map('Custom.TCombobox', fieldbackground=[('readonly',app_settings.Settings['Background_color'])])
        self.style.map('Custom.TCombobox', background=[('readonly', app_settings.Settings['Background_color'])])
        self.style.map('Custom.TCombobox', foreground=[('readonly', app_settings.Settings['Foreground_color'])])
        self.accent_color_combobox.option_add('*TCombobox*Listbox.background', app_settings.Settings['Background_color'])
        self.accent_color_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.accent_color_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Foreground_color'])

    def setup_save_button(self):
        self.current_row+=1
        self.save_button = tk.Button(self, text="save", command=self.apply_changes, bd=1)
        self.save_button.config(relief="solid")
        self.save_button.config(bg=app_settings.Settings['Theme_color'])
        self.save_button.config(fg="white")
        self.save_button.config(font=app_settings.App_font)
        self.save_button.config(highlightbackground=app_settings.Settings['Background_color'])
        self.save_button.config(activebackground=app_settings.Settings['Theme_color'])
        self.save_button.config(activeforeground="white")
        self.save_button.grid(row=self.current_row, column=1)


    def apply_changes(self):
        if not self.accent_color_combobox.get() == app_settings.Settings['Theme_color']:
            update_color = self.accent_color_combobox.get()
            self.change_calendar_theme(update_color)
            self.change_save_buton_bg(update_color)
        if not self.theme_combobox.get() == app_settings.Settings['Theme']:
            self.change_theme()
        if not self.template_combobox.get() == app_settings.Settings['Template']:
            app_settings.update_settings('Template',self.template_combobox.get())
        if not self.font_combobox.get() == app_settings.App_font[0]:
            app_settings.update_font(self.font_combobox.get(),15) #15 is default for now
            self.master.reload_app()
    

    def change_save_buton_bg(self,update_color):
        self.save_button.config(bg=self.colors[update_color])
        self.save_button.config(activebackground=self.colors[update_color])
    def set_side_menu(self,side_menu):
        self.side_menu= side_menu 

    def change_calendar_theme(self,update_color):
        if self.side_menu:
            app_settings.update_settings("Theme_color",self.colors[update_color])
            self.side_menu.change_calendar_theme(self.colors[update_color])
        

    def get_keys_by_value(self,value):
        keys = []
        for key, val in self.colors.items():
            if val == value:
                keys.append(key)
        return keys if keys else None

    def setup_theme_chooser(self):

        self.current_row+=1;
        self.theme_label = tk.Label(self, font=app_settings.App_font,text="Theme:", bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'])
        self.theme_label.grid(row=self.current_row,column=0,pady=(5,0),padx=(5,0),sticky="w")


        self.theme_combobox= ttk.Combobox(self,state="readonly",background=app_settings.Settings['Background_color'],foreground=app_settings.Settings['Combobox_foreground'],font=app_settings.App_font,style="Custom.TCombobox")
        self.theme_combobox.grid(row=self.current_row, column=1,padx=(5,0),pady=(5,0))


        # Add items to the Combobox
        self.theme_combobox['values'] = ("Dark", "Light")

        # Set a default value by getting the color
        self.theme_combobox.set(app_settings.Settings['Theme'])

        self.style.map('Custom.TCombobox', fieldbackground=[('readonly',app_settings.Settings['Background_color'])])
        self.style.map('Custom.TCombobox', background=[('readonly', app_settings.Settings['Background_color'])])
        self.style.map('Custom.TCombobox', foreground=[('readonly', app_settings.Settings['Foreground_color'])])
        self.theme_combobox.option_add('*TCombobox*Listbox.background', app_settings.Settings['Background_color'])
        self.theme_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.theme_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Foreground_color'])

        #-------------------------------------------------------
    def setup_template_chooser(self):
        self.current_row+=1;
        self.template_label = tk.Label(self, font=app_settings.App_font,text="Template", bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'])
        self.template_label.grid(row=self.current_row,column=0,pady=(5,0),padx=(5,0),sticky='w')
        
        
        self.template_combobox = ttk.Combobox(self,state="readonly",background=app_settings.Settings['Background_color'],foreground=app_settings.Settings['Combobox_foreground'],font=app_settings.App_font,style="Custom.TCombobox")
        self.template_combobox.grid(row=self.current_row, column=1,padx=(5,0),pady=(5,0))

        # Construct the pattern to match all '.md' files
        template = "templates"
        pattern = f"{template}/*.md"

        # List all files in the directory with .md extension
        md_files = glob.glob(pattern)

        # Remove the '.md' extension and keep only the base names
        md_filenames = [os.path.splitext(os.path.basename(file))[0] for file in md_files]
        # Update self.template_combox['values'] with these filenames
        md_filenames.append("None")
        self.template_combobox['values'] = md_filenames 
        # Set a default value by getting the color
        self.template_combobox.set(app_settings.Settings['Template'])

        self.style.map('Custom.TCombobox', fieldbackground=[('readonly',app_settings.Settings['Background_color'])])
        self.style.map('Custom.TCombobox', background=[('readonly', app_settings.Settings['Background_color'])])
        self.style.map('Custom.TCombobox', foreground=[('readonly', app_settings.Settings['Foreground_color'])])
        self.template_combobox.option_add('*TCombobox*Listbox.background', app_settings.Settings['Background_color'])
        self.template_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.template_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Foreground_color'])

    def change_theme(self):
        app_settings.update_settings("Theme",self.theme_combobox.get())
        self.master.reload_app()

    def reload(self):
        self.config(bg=app_settings.Settings['Background_color'])
        
        self.save_button.config(bg=app_settings.Settings['Theme_color'],
                                 highlightbackground=app_settings.Settings['Background_color'],
                                 activebackground=app_settings.Settings['Theme_color'])
        self.save_button.config(font=app_settings.App_font)

        self.accent_label.config(bg=app_settings.Settings['Background_color'],
                                  fg=app_settings.Settings['Foreground_color'])
        self.accent_label.config(font=app_settings.App_font) 

        self.theme_label.config(bg=app_settings.Settings['Background_color'],
                                fg=app_settings.Settings['Foreground_color'])
        self.theme_label.config(font=app_settings.App_font) 

        self.template_label.config(bg=app_settings.Settings['Background_color'],
                                fg=app_settings.Settings['Foreground_color'])
        self.template_label.config(font=app_settings.App_font) 

        self.font_label.config(bg=app_settings.Settings['Background_color'],
                                fg=app_settings.Settings['Foreground_color'])
        self.font_label.config(font=app_settings.App_font) 

        # Update combobox dropdown list styles for both accent and theme comboboxes
        self.style.map('Custom.TCombobox', fieldbackground=[('readonly', app_settings.Settings['Background_color'])])
        self.accent_color_combobox.configure(foreground=app_settings.Settings['Combobox_foreground'])
        self.theme_combobox.configure(foreground=app_settings.Settings['Combobox_foreground'])
        self.theme_combobox.config(font=app_settings.App_font)
         
        self.accent_color_combobox.option_add('*TCombobox*Listbox.background', app_settings.Settings['Background_color'])
        self.accent_color_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.accent_color_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Combobox_foreground'])
        self.accent_color_combobox.config(font=app_settings.App_font)

        self.template_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.template_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Combobox_foreground'])
        self.template_combobox.configure(foreground=app_settings.Settings['Combobox_foreground'])
        self.template_combobox.config(font=app_settings.App_font)

        self.font_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.font_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Combobox_foreground'])
        self.font_combobox.configure(foreground=app_settings.Settings['Combobox_foreground'])
        self.font_combobox.config(font=app_settings.App_font)

        #update the footer
        self.footer_text.config(background=app_settings.Settings['Background_color'])
        self.footer_text.config(foreground=app_settings.Settings['Foreground_color'])
        self.footer_text.config(font=app_settings.App_font)
        self.switch.config(progress_color=(app_settings.Settings['Theme_color'],app_settings.Settings['Theme_color']))
    def open_setings(self):
        self.deiconify()
    def close_settings(self):
        self.withdraw()
    def center_window_on_screen(self,window):
        window.update_idletasks()  # Ensure window size is updated
        window_width = window.winfo_width()
        window_height = window.winfo_height()

        # Get the screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate the position of the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window position
        window.geometry('+{}+{}'.format(x, y))
    def setup_footer(self):
        self.current_row+=1 
        #self.footer_label.grid(row=5, column=1, pady=(5,0), padx=(5,0))
        self.footer_text = tk.Text(self, font=app_settings.App_font, bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'], height=1,highlightthickness=0,relief="flat")

        # Insert text into the Text widget
        self.footer_text.insert("1.0", "Made with ")
        self.footer_text.insert("1.10", "\u2665", "red")  # Insert the red heart symbol
        self.footer_text.insert("1.11", " by ")
        self.footer_text.insert("1.15", "tervicke", "clickable")  # Insert the clickable word
        self.footer_text.tag_config("red", foreground="red")  # Configure tag appearance for red color
        self.footer_text.tag_config("clickable", foreground="blue")
        self.footer_text.grid(row=self.current_row, column=1, pady=(5,0), padx=(5,0))
        self.footer_text.config(state='disabled')
        self.footer_text.tag_bind("clickable", "<Button-1>", self.open_link)
        self.footer_text.tag_bind("clickable", "<Leave>", self.leave_link)
        self.footer_text.tag_bind("clickable", "<Button-1>", self.open_link)

    def open_link(self,event):
        webbrowser.open("https://tervicke.netlify.app/")

    def enter_link(self,event):
       self.footer_text.config(cursor="hand2")

    def leave_link(self,event):
       self.footer_text.config(cursor="") 
    def setup_font_chooser(self):
        self.current_row+=1;
        self.font_label = tk.Label(self, font=app_settings.App_font,text="Font:", bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'])
        self.font_label.grid(row=self.current_row,column=0,pady=(5,0),padx=(5,0),sticky="w")


        self.font_combobox= ttk.Combobox(self,state="readonly",background=app_settings.Settings['Background_color'],foreground=app_settings.Settings['Combobox_foreground'],font=app_settings.App_font,style="Custom.TCombobox")
        self.font_combobox.grid(row=self.current_row, column=1,padx=(5,0),pady=(5,0))
        
        self.font_combobox.set(app_settings.App_font[0])

        self.font_combobox['values'] = ("Helvetica", "Courier New",  "Arial" ,"Tahoma" , "Times New Roman" , "DejaVU Sans","Verdana")

        self.style.map('Custom.TCombobox', fieldbackground=[('readonly',app_settings.Settings['Background_color'])])
        self.style.map('Custom.TCombobox', background=[('readonly', app_settings.Settings['Background_color'])])
        self.style.map('Custom.TCombobox', foreground=[('readonly', app_settings.Settings['Foreground_color'])])
        self.font_combobox.option_add('*TCombobox*Listbox.background', app_settings.Settings['Background_color'])
        self.font_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.font_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Foreground_color'])
    def setup_streak_option(self):
        self.current_row+=1;
        self.font_label = tk.Label(self, font=app_settings.App_font,text="Disable streaks", bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'])
        self.font_label.grid(row=self.current_row,column=0,pady=(5,0),padx=(5,0),sticky="w")
        

        self.streaks_switch = customtkinter.CTkSwitch(self, text="",command=self.toggle_streaks,switch_width=50,switch_height=25,progress_color=(app_settings.Settings['Theme_color'],app_settings.Settings['Theme_color']))
        self.streaks_switch.grid(row=self.current_row, column=1,padx=(5,0),pady=(5,0),sticky='w')
        #turn on the check if streaks are disabled
        if app_settings.Settings['Disable_streaks'] == 'true':
            self.streaks_switch.select()

    def toggle_streaks(self):
        if app_settings.Settings['Disable_streaks'] == 'false':
            app_settings.update_settings('Disable_streaks',"true")
        else:
            app_settings.update_settings('Disable_streaks',"false")
        print(app_settings.Settings['Disable_streaks'])
        self.master.reload_app()

