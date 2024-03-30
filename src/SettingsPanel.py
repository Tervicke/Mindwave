import app_settings
import tkinter as tk
from tkinter import ttk
class Settingspanel(tk.Toplevel):
    def __init__(self,master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.config(bg=app_settings.Settings['Background_color'])
        self.title("Settings")
        self.resizable(height=False,width=False)
        self.withdraw()
        self.protocol('WM_DELETE_WINDOW',self.close_settings)

        self.side_menu = None
        self.style = ttk.Style()

        self.colors = {"Blue":"#007AFF" , "Red":"Red" , "Green":"#34c759"}

        self.accent_label = None
        self.theme_label = None
        self.save_button = None

        self.theme_combobox= None 
        self.accent_color_combobox = None 

        self.setup_accent_color()
        self.setup_theme_chooser()
        self.setup_save_button()

        self.center_window_on_screen(self)

    def setup_accent_color(self):

        self.accent_label = tk.Label(self, font=app_settings.App_font,text="Accent color:", bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'])
        self.accent_label.grid(row=0,column=0,pady=5,padx=5)

        self.accent_color_combobox = ttk.Combobox(self,state="readonly",background=app_settings.Settings['Background_color'],foreground=app_settings.Settings['Foreground_color'],font=app_settings.App_font,style="Custom.TCombobox")
        self.accent_color_combobox.grid(row=0, column=1,padx=5,pady=5)
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
        self.save_button = tk.Button(self, text="save", command=self.apply_changes, bd=1)
        self.save_button.config(relief="solid")
        self.save_button.config(bg=app_settings.Settings['Theme_color'])
        self.save_button.config(fg="white")
        self.save_button.config(font=app_settings.App_font)
        self.save_button.config(highlightbackground=app_settings.Settings['Background_color'])
        self.save_button.config(activebackground=app_settings.Settings['Theme_color'])
        self.save_button.config(activeforeground="white")
        self.save_button.grid(row=2, column=1)


    def apply_changes(self):
        if not self.accent_color_combobox.get() == app_settings.Settings['Theme_color']:
            self.change_calendar_theme()
        if not self.theme_combobox.get() == app_settings.Settings['Theme']:
            self.change_theme()
            
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

    def setup_theme_chooser(self):


        self.theme_label = tk.Label(self, font=app_settings.App_font,text="Theme:", bg=app_settings.Settings['Background_color'], fg=app_settings.Settings['Foreground_color'])
        self.theme_label.grid(row=1,column=0,pady=5,padx=5)


        self.theme_combobox= ttk.Combobox(self,state="readonly",background=app_settings.Settings['Background_color'],foreground=app_settings.Settings['Foreground_color'],font=app_settings.App_font,style="Custom.TCombobox")
        self.theme_combobox.grid(row=1, column=1,padx=5,pady=5)


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

    def change_theme(self):
        app_settings.update_settings("Theme",self.theme_combobox.get())
        self.master.change_themes(self.theme_combobox.get())

    def reload(self):
        self.config(bg=app_settings.Settings['Background_color'])
        
        self.save_button.config(bg=app_settings.Settings['Theme_color'],
                                 highlightbackground=app_settings.Settings['Background_color'],
                                 activebackground=app_settings.Settings['Theme_color'])
                 
        self.accent_label.config(bg=app_settings.Settings['Background_color'],
                                  fg=app_settings.Settings['Foreground_color'])
        
        self.theme_label.config(bg=app_settings.Settings['Background_color'],
                                fg=app_settings.Settings['Foreground_color'])
        
        # Update combobox dropdown list styles for both accent and theme comboboxes
        self.style.map('Custom.TCombobox', fieldbackground=[('readonly', app_settings.Settings['Background_color'])])
        self.accent_color_combobox.configure(foreground=app_settings.Settings['Foreground_color'])
        self.theme_combobox.configure(foreground=app_settings.Settings['Foreground_color'])
         
        self.accent_color_combobox.option_add('*TCombobox*Listbox.background', app_settings.Settings['Background_color'])
        self.accent_color_combobox.option_add('*TCombobox*Listbox.font', app_settings.App_font)
        self.accent_color_combobox.option_add('*TCombobox*Listbox.foreground', app_settings.Settings['Foreground_color'])
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
