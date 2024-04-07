import tkinter as tk
import app_settings
from datetime import datetime 
from EditorWidget import Editorwidget
from SettingsPanel import Settingspanel
from TagsPanel import Tagspanel
from SideMenu import Sidemenu
import json
class Menubar(tk.Frame):
    def __init__(self,master=None, **kw):
        super().__init__(master, **kw)

        self.editor_widget  = None
        self.settings_panel = None
        self.tags_panel = None
        self.side_menu= None

        self.configure(bg=app_settings.Settings['Background_color'])
        self.configure(height=50)

        self.Datelabel = tk.Label(self) 
        #self.setup_label()
        
        self.colors = {"blue":"#007AFF" , "red":"Red" , "green":"#34c759"}

        self.edit_icon= tk.PhotoImage(file="icons/edit_" + self.get_keys_by_value(app_settings.Settings['Theme_color'])[0] + ".png")
        self.edit_todays = tk.Button(self ,image=self.edit_icon ,bg=app_settings.Settings['Background_color'] , bd=0 , highlightbackground=app_settings.Settings['Background_color'] , activebackground=app_settings.Settings['Background_color'],command=self.open_todays)
        self.edit_todays.pack(side='left',padx=0,pady=10)

        self.save_icon= tk.PhotoImage(file="icons/save_" + self.get_keys_by_value(app_settings.Settings['Theme_color'])[0] + ".png")
        self.save_todays= tk.Button(self ,image=self.save_icon ,bg=app_settings.Settings['Background_color'] , bd=0 , highlightbackground=app_settings.Settings['Background_color'] , activebackground=app_settings.Settings['Background_color'],command=self.save_todays)
        self.save_todays.pack(side='left',padx=2,pady=10)

        self.settings_icon= tk.PhotoImage(file="icons/settings_" + self.get_keys_by_value(app_settings.Settings['Theme_color'])[0] + ".png")
        self.settings_button= tk.Button(self ,image=self.settings_icon,bg=app_settings.Settings['Background_color'] , bd=0 , highlightbackground=app_settings.Settings['Background_color'] , activebackground=app_settings.Settings['Background_color'],command=self.open_settings)
        self.settings_button.pack(side='right',padx=2,pady=10)
       

        self.tags_icon= tk.PhotoImage(file="icons/tags_" + self.get_keys_by_value(app_settings.Settings['Theme_color'])[0] + ".png")
        #self.tags_icon= tk.PhotoImage(file="icons/tags_grey.png")
        self.tags_edit_button= tk.Button(self ,image=self.tags_icon,bg=app_settings.Settings['Background_color'] , bd=0 , highlightbackground=app_settings.Settings['Background_color'] , activebackground=app_settings.Settings['Background_color'],command=self.edit_tags)
        self.tags_edit_button.pack(side='left',padx=2,pady=10)

        self.search_entry = tk.Entry(self)
        self.search_entry.config(font=app_settings.App_font)
        self.search_entry.pack(side='left',padx=10,pady=10)


    def setup_label(self):
        self.Datelabel.config(bg=app_settings.Settings['Background_color'])
        self.Datelabel.config(fg=app_settings.Settings['Theme_color'])
        self.Datelabel.pack(side="left",padx=10,pady=10)
        self.Datelabel.config(font=app_settings.App_font)
        #set todays day by default
        todays_date = datetime.now().strftime("%d %B , %Y")
        self.update_Datelabel(todays_date)

    def update_Datelabel(self,text):
        self.Datelabel.config(text=text)

    def set_editor_widget(self,editor_widget):
        self.editor_widget = editor_widget

    def save_todays(self):
        formatted_date = datetime.now().strftime('%-d %B %Y')
        json_data = {
            "date":formatted_date,
            "content":"",
            "tags":""
        }
        if self.editor_widget:
            json_data['content']  = self.editor_widget.get_editor_content()
        if self.side_menu:
            json_data['tags'] = self.side_menu.get_tags()
        print(json_data)
        today_date_file = app_settings.Settings['Diary_folder'] + '/' +datetime.now().strftime("%d-%m-%y") + ".json"
        with open(today_date_file, "w") as file:
            file.write(json.dumps(json_data) )
    def open_todays(self):
        if self.editor_widget:
            self.editor_widget.open_todays()
    def reload(self):
        self.configure(bg=app_settings.Settings['Background_color'])

        self.edit_todays.config(bg=app_settings.Settings['Background_color'])
        self.edit_todays.config(highlightbackground=app_settings.Settings['Background_color'])
        self.edit_todays.config(activebackground=app_settings.Settings['Background_color'])
    
        self.save_todays.config(bg=app_settings.Settings['Background_color'])
        self.save_todays.config(highlightbackground=app_settings.Settings['Background_color'])
        self.save_todays.config(activebackground=app_settings.Settings['Background_color'])

        self.settings_button.config(bg=app_settings.Settings['Background_color'])
        self.settings_button.config(highlightbackground=app_settings.Settings['Background_color'])
        self.settings_button.config(activebackground=app_settings.Settings['Background_color'])

    def set_settings_panel(self,settings_panel):
        self.settings_panel = settings_panel

    def open_settings(self):
        if self.settings_panel:
            print(self.settings_panel)
            self.settings_panel.open_setings()

    def reset_prompt(self):
        if self.editor_widget:
            self.editor_widget.set_prompt()

    def get_keys_by_value(self,value):
        keys = []
        for key, val in self.colors.items():
            if val == value:
                keys.append(key)
        return keys if keys else None
    def set_tags_panel(self,tags_panel):
        self.tags_panel = tags_panel
    def edit_tags(self):
        tag_selector_window = Tagspanel(self,self.update_tags)

    def set_side_menu(self,side_menu):
        self.side_menu=side_menu 
    def update_tags(self,selected_tags):
        self.side_menu.add_tags(selected_tags)
