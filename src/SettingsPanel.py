import app_settings
import tkinter as tk
from tkinter import ttk
class Settingspanel(tk.Toplevel):
    def __init__(self,master=None, **kw):
        super().__init__(master, **kw)
        self.config(bg=app_settings.Settings['Background_color'])
        self.title("Settings")
        self.resizable(height=False,width=False)
        self.side_menu = None

        self.colors = {"Blue":"#007AFF" , "Red":"Red" , "Green":"#34c759"}

        self.accent_color_combobox = None 
        self.setup_accent_color()
        self.setup_save_button()

    def setup_accent_color(self):
        frame = tk.Frame(self, bg=app_settings.Settings['Background_color'])
        frame.pack(padx=5, pady=5)

        label = tk.Label(frame, font=app_settings.App_font,text="Accent color:", bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'])
        label.pack(side=tk.LEFT,pady=5,padx=5)

        self.accent_color_combobox = ttk.Combobox(frame,state="readonly",background=app_settings.Settings['Background_color'],foreground=app_settings.Settings['Foreground_color'],font=app_settings.App_font)
        self.accent_color_combobox.pack(side=tk.RIGHT,padx=5,pady=5)

        # Add items to the Combobox
        self.accent_color_combobox['values'] = ("Blue", "Green",  "Red" )

        # Set a default value by getting the color
        self.accent_color_combobox.set(self.get_keys_by_value(app_settings.Settings['Theme_color']))

        style = ttk.Style()
        style.map('TCombobox', fieldbackground=[('readonly',app_settings.Settings['Background_color'])])
        style.map('TCombobox', background=[('readonly', app_settings.Settings['Background_color'])])
        style.map('TCombobox', foreground=[('readonly', app_settings.Settings['Foreground_color'])])
        self.accent_color_combobox.option_add('*TCombobox*Listbox.background', app_settings.Settings['Background_color'])
        self.accent_color_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.accent_color_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Foreground_color'])

    def setup_save_button(self):
        save_button = tk.Button(self, text="save", command=self.apply_changes,bd=1)
        save_button.config(relief="solid")
        save_button.config(bg=app_settings.Settings['Editor_color'])
        save_button.config(fg=app_settings.Settings['Foreground_color'])
        save_button.config(font=app_settings.App_font)
        save_button.config(highlightbackground=app_settings.Settings['Background_color'])
        save_button.config(activebackground=app_settings.Settings['Editor_color'])
        save_button.config(activeforeground=app_settings.Settings['Foreground_color'])
        save_button.pack(anchor="s")

    def apply_changes(self):
        if not self.accent_color_combobox.get() == app_settings.Settings['Theme_color']:
            self.change_calendar_theme()

    def set_side_menu(self,side_menu):
        self.side_menu= side_menu 

    def change_calendar_theme(self):
        if self.side_menu:
            update_color = self.accent_color_combobox.get()
            self.side_menu.change_calendar_theme(self.colors[update_color])
            app_settings.update_settings("Theme_color",self.colors[update_color])
        

    def get_keys_by_value(self,value):
        keys = []
        for key, val in self.colors.items():
            if val == value:
                keys.append(key)
        return keys if keys else None
