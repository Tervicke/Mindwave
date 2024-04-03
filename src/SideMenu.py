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

        tags_container= tk.Frame(self)
        tags_container.config(background=app_settings.Settings['Background_color'])
        tags_container.grid(row=2,column=0,sticky='ew')

        list_of_tags = [
            ["happy", "#B8860B"],
            ["sad", "grey"],
            ["excited", "green"],
            ["angry", "red"],
        ]

        for tag_name, color in list_of_tags:
            label = tk.Label(tags_container, text=tag_name, bg=color, padx=5, pady=2)
            label.font=app_settings.App_font
            label.config(fg='white')
            label.pack(side=tk.LEFT, padx=2, pady=5)
        '''
        tag1 = Tag(tags_container, text="Tag 1", bg="lightblue", text_color="black")
        tag1.pack(padx=5, pady=5)
        tag2 = Tag(tags_container, text="Tag 2", bg="lightgreen", text_color="white")
        tag2.pack( padx=5, pady=5)
        '''

class Tag(tk.Frame):
    def __init__(self, master=None, text="", bg="lightgray", text_color="black", **kwargs):
        super().__init__(master, bg=bg, **kwargs)
        self.text = text
        self.text_color = text_color
        self._create_widgets()

    def _create_widgets(self):
        self.label = tk.Label(self, text=self.text, bg=self["bg"], fg=self.text_color)
        self.label.pack(expand=True, fill="both", padx=5, pady=2)


