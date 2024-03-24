import tkinter as tk
from app_settings import Settings , App_font
from tkcalendar import Calendar
from EditorWidget import Editorwidget 
class Sidemenu(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        self.editor_widget = None

        self.configure(bg=Settings['Background_color'])

        self.calendar =  Calendar(self)
        self.setup_calendar()

    def setup_calendar(self):
        self.calendar.config(selectmode='day')
        self.calendar.config(foreground=Settings['Foreground_color'])
        self.calendar.config(background=Settings['Editor_color'])
        self.calendar.config(bordercolor=Settings['Background_color'])
        self.calendar.config(headersbackground=Settings['Background_color'])
        self.calendar.config(headersforeground=Settings['Foreground_color'])
        self.calendar.config(normalbackground=Settings['Background_color'])
        self.calendar.config(normalforeground=Settings['Foreground_color'])
        self.calendar.config(weekendbackground=Settings['Background_color'])
        self.calendar.config(weekendforeground=Settings['Foreground_color'])
        self.calendar.config(othermonthforeground=Settings['Foreground_color'])
        self.calendar.config(othermonthbackground=Settings['Background_color'])
        self.calendar.config(othermonthweforeground=Settings['Foreground_color'])
        self.calendar.config(othermonthwebackground=Settings['Background_color'])
        self.calendar.config(selectbackground=Settings['Theme_color'])
        self.calendar.config(selectforeground=Settings['Editor_color'])
        self.calendar.config(weekendforeground=Settings['Foreground_color'])
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
