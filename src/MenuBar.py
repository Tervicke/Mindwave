import tkinter as tk
import app_settings
from datetime import datetime 
from EditorWidget import Editorwidget
from SettingsPanel import Settingspanel
class Menubar(tk.Frame):
    def __init__(self,master=None, **kw):
        super().__init__(master, **kw)

        self.editor_widget  = None
        self.settings_panel = None

        self.configure(bg=app_settings.Settings['Background_color'])
        self.configure(height=50)

        self.Datelabel = tk.Label(self) 
        #self.setup_label()
        
        self.edit_icon= tk.PhotoImage(file="icons/edit_todays.png")
        self.edit_todays = tk.Button(self ,image=self.edit_icon ,bg=app_settings.Settings['Background_color'] , bd=0 , highlightbackground=app_settings.Settings['Background_color'] , activebackground=app_settings.Settings['Background_color'],command=self.open_todays)
        self.edit_todays.pack(side='left',padx=0,pady=10)

        self.save_icon= tk.PhotoImage(file="icons/save_todays.png")
        self.save_todays= tk.Button(self ,image=self.save_icon ,bg=app_settings.Settings['Background_color'] , bd=0 , highlightbackground=app_settings.Settings['Background_color'] , activebackground=app_settings.Settings['Background_color'],command=self.save_todays)
        self.save_todays.pack(side='left',padx=2,pady=10)

        self.settings_icon= tk.PhotoImage(file="icons/settings.png")
        self.settings_button= tk.Button(self ,image=self.settings_icon,bg=app_settings.Settings['Background_color'] , bd=0 , highlightbackground=app_settings.Settings['Background_color'] , activebackground=app_settings.Settings['Background_color'],command=self.open_settings)
        self.settings_button.pack(side='right',padx=2,pady=10)


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
        if self.editor_widget:
            self.editor_widget.save_todays()

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
