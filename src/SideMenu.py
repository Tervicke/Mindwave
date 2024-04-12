import tkinter as tk
import app_settings
from tkcalendar import Calendar
from EditorWidget import Editorwidget 
import os
import json
from datetime import datetime
class Sidemenu(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.editor_widget = None
        self.configure(bg=app_settings.Settings['Background_color'])
        self.current_tags = None  
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
        date = self.calendar.selection_get().strftime("%d/%m/%y")
        print(date)
        if datetime.today().strftime("%d/%m/%y") != date:
            self.master.disable_tags_button()
        #open the file associated with it and write get the tags and then update by setup_tags()
        file_name = os.path.join(app_settings.Settings['Diary_folder'],date.replace('/','-') + '.json')
        file_name = os.path.expanduser(file_name)
        print(file_name)
        if os.path.exists(file_name):
            print("dkfjal")
            with open(file_name) as Diary_File:
                raw_data= Diary_File.read()
                json_data = json.loads(raw_data)
                print(json_data['content']) 
                #update the editor widget
                self.editor_widget.configure(state='normal')
                self.editor_widget.delete('1.0', 'end')
                self.editor_widget.apply_formatting(json_data['content'])
                self.editor_widget.config(state='disabled')
                #add tags 
                self.add_tags(json_data['tags'])
        else:
            #remove the content from the editor widget and add No entry found
            self.editor_widget.configure(state='normal')
            self.editor_widget.delete('1.0', 'end')
            self.editor_widget.insert('4.6',"No Entry found..")
            self.editor_widget.config(state='disabled')
            #remove the tags
            self.clear_container(self.tags_container) 

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
        self.tags_heading_container = tk.Frame(self)
        self.tags_heading_container.config(background=app_settings.Settings['Background_color'])
        self.tags_heading_container.config(highlightbackground=app_settings.Settings['Background_color'])
        self.tags_heading_container.grid(row=1,column=0,sticky='ew')

        self.tags_label = tk.Label(self.tags_heading_container, text="Tags")
        self.tags_label.config(font=app_settings.App_font)
        self.tags_label.config(background=app_settings.Settings['Background_color'])
        self.tags_label.config(foreground=app_settings.Settings['Foreground_color'])
        self.tags_label.pack(side='left')

        self.tags_container= tk.Frame(self)
        self.tags_container.config(background=app_settings.Settings['Background_color'])
        self.tags_container.grid(row=2,column=0,sticky='ew')
        


    def add_tags(self,tags_list):
        self.current_tags= tags_list
        # width of the the only label without character - 12 
        #width of each character is - 8 
        self.clear_container(self.tags_container) 

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
            if container_width - (tags_added * 12 + self.total_width_of_tags(tags_list,tags_added) ) - 100 > 12 + len(tags_list[tags_added] )*8:
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
    def clear_container(self,parent_widget):
        for widget in parent_widget.winfo_children():
            widget.destroy()

    def total_width_of_tags(self,tags_list , i ):
        ans = 0
        for tag_name,bg_color,fg_color in tags_list[:i]:
            ans += len(tag_name)
        return ans*8 

    def get_tags(self):
        if self.current_tags:
            return self.current_tags
        else:
            return []
    def remove_tags(self):
        self.clear_container(self.tags_container) 
