import tkinter as tk
import app_settings
from tkcalendar import Calendar
from EditorWidget import Editorwidget 
class Sidemenu(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.editor_widget = None
        self.configure(bg=app_settings.Settings['Background_color'])
        self.calendar =  Calendar(self)
        self.setup_calendar()
        self.setup_tags()
    def setup_calendar(self):
        self.calendar.config(selectmode='day')
        self.calendar.config(foreground=app_settings.Settings['Foreground_color'])
        self.calendar.config(background=app_settings.Settings['Text_color'])
        self.calendar.config(bordercolor=app_settings.Settings['Background_color'])
        self.calendar.config(headersbackground=app_settings.Settings['Background_color'])
        self.calendar.config(headersforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(normalbackground=app_settings.Settings['Background_color'])
        self.calendar.config(normalforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(weekendbackground=app_settings.Settings['Background_color'])
        self.calendar.config(weekendforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(selectbackground=app_settings.Settings['Theme_color'])
        self.calendar.config(selectforeground="white")
        self.calendar.config(weekendforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(showweeknumbers=False)
        self.calendar.config(showothermonthdays=False)
        self.calendar.config(font=('Arial', 10))
        #self.calendar.pack(fill="x", pady=10)
        self.calendar.grid(row=0,column=0,pady=10)
        self.calendar.bind("<<CalendarSelected>>", self.date_selected)

    def set_editor_widget(self,editor_widget):
        self.editor_widget = editor_widget

    def date_selected(self,event=None):
        if self.editor_widget:
            self.editor_widget.open_date(self.calendar.get_date())
    def change_calendar_theme(self,updated_color):
        self.calendar.config(selectbackground=updated_color)
    def reload(self):
        self.configure(bg=app_settings.Settings['Background_color'])
        self.calendar.config(foreground=app_settings.Settings['Foreground_color'])
        self.calendar.config(background=app_settings.Settings['Text_color'])
        self.calendar.config(bordercolor=app_settings.Settings['Background_color'])
        self.calendar.config(headersbackground=app_settings.Settings['Background_color'])
        self.calendar.config(headersforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(normalbackground=app_settings.Settings['Background_color'])
        self.calendar.config(normalforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(weekendbackground=app_settings.Settings['Background_color'])
        self.calendar.config(weekendforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(selectbackground=app_settings.Settings['Theme_color'])
        self.calendar.config(weekendforeground=app_settings.Settings['Foreground_color'])
    def setup_tags(self):

        tags_label = tk.Label(self, text="Tags")
        tags_label.config(font=app_settings.App_font)
        tags_label.config(background=app_settings.Settings['Background_color'])
        tags_label.config(foreground=app_settings.Settings['Foreground_color'])
        tags_label.grid(row=1,column=0,stick='w')

        self.tags_container= tk.Frame(self)
        self.tags_container.config(background=app_settings.Settings['Background_color'])
        self.tags_container.grid(row=2,column=0,sticky='ew')

        self.add_tags()

    def add_tags(self):
        tags_list = [
            ["happy", "#FFD700", "#000000"],       # Yellow for happy, black foreground
            ["sad", "#4169E1", "#FFFFFF"],         # Dark blue for sad, white foreground
            ["work", "#FF4500", "#FFFFFF"],        # Orange-red for work-related entries, white foreground
            ["personal", "#00CED1", "#000000"],    # Dark cyan for personal entries, black foreground
            ["goals", "#FF69B4", "#000000"],       # Pink for goals, black foreground
            ["reflection", "#FF6347", "#FFFFFF"],  # Tomato red for reflection, white foreground
            ["health", "#87CEEB", "#000000"],      # Sky blue for health-related entries, black foreground
            ["travel", "#32CD32", "#FFFFFF"],      # Lime green for travel, white foreground
            ["ideas", "#FF1493", "#FFFFFF"],       # Deep pink for ideas, white foreground
            ["memories", "#9400D3", "#FFFFFF"]     # Dark violet for memories, white foreground
        ]

        # width of the the only label without character - 12 
        #width of each character is - 8 
        
        self.tags_container.update()
        container_width = self.tags_container.winfo_width()

        #making 3 frames right now only  
        tags_frame_list = []
        #add a initial frame
        frame = tk.Frame(self.tags_container, bg=app_settings.Settings['Background_color'])
        frame.pack(fill='x')
        tags_frame_list.append(frame)

        tags_added = 0
        current_frame = 0

        for tag_name, bg_color,fg_color in tags_list:
            #check if the tag can exist in the same line
            label = tk.Label(tags_frame_list[current_frame], text=tag_name, bg=bg_color,foreground=fg_color,padx=5, pady=2)
            label.font=app_settings.App_font
            if container_width - (tags_added * 12 + self.total_width_of_tags(tags_list,tags_added) ) > 12 + len(tags_list[tags_added] )*8:
                label.pack(side='left', padx=2, pady=5 ,anchor='w')
            else:
                #make a new frame and append that tag to the that frame 
                frame = tk.Frame(self.tags_container, bg=app_settings.Settings['Background_color'])
                frame.pack(fill='x')
                tags_frame_list.append(frame)

                tags_added = 0
                current_frame+=1

                label.pack(side='left', padx=2, pady=5 ,anchor='w')
            tags_added +=1

    def total_width_of_tags(self,tags_list , i ):
        ans = 0
        for tag_name,bg_color,fg_color in tags_list[:i]:
            ans += len(tag_name)
        return ans*8 

