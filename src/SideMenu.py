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

    def setup_calendar(self):
        self.calendar.config(selectmode='day')
        self.calendar.config(foreground=app_settings.Settings['Foreground_color'])
        self.calendar.config(background=app_settings.Settings['Editor_color'])
        self.calendar.config(bordercolor=app_settings.Settings['Background_color'])
        self.calendar.config(headersbackground=app_settings.Settings['Background_color'])
        self.calendar.config(headersforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(normalbackground=app_settings.Settings['Background_color'])
        self.calendar.config(normalforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(weekendbackground=app_settings.Settings['Background_color'])
        self.calendar.config(weekendforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(selectbackground=app_settings.Settings['Theme_color'])
        self.calendar.config(selectforeground=app_settings.Settings['Editor_color'])
        self.calendar.config(weekendforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(showweeknumbers=False)
        self.calendar.config(showothermonthdays=False)
        self.calendar.config(font=('Arial', 10))
        self.calendar.pack(fill="x",expand=True,pady=10,anchor="n")
        self.calendar.pack(fill="x", pady=10)
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
        self.calendar.config(background=app_settings.Settings['Editor_color'])
        self.calendar.config(bordercolor=app_settings.Settings['Background_color'])
        self.calendar.config(headersbackground=app_settings.Settings['Background_color'])
        self.calendar.config(headersforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(normalbackground=app_settings.Settings['Background_color'])
        self.calendar.config(normalforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(weekendbackground=app_settings.Settings['Background_color'])
        self.calendar.config(weekendforeground=app_settings.Settings['Foreground_color'])
        self.calendar.config(selectbackground=app_settings.Settings['Theme_color'])
        self.calendar.config(selectforeground=app_settings.Settings['Editor_color'])
        self.calendar.config(weekendforeground=app_settings.Settings['Foreground_color'])
