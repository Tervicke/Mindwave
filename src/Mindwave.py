import tkinter as tk
import app_settings
from datetime import datetime
from EditorWidget import Editorwidget
from SideMenu import Sidemenu
from MenuBar import Menubar
from SettingsPanel import Settingspanel
from TagsPanel import Tagspanel
import sv_ttk
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        app_settings.load_settings()
        self.configure(bg=app_settings.Settings['Background_color'])  
        self.title('Mindwave')
        self.geometry('1000x620')
        self.iconphoto(False, tk.PhotoImage(file='icons/app_icon.png'))


        #Editing window
        self.editor_widget = Editorwidget(self)
        self.side_menu = Sidemenu(self)
        self.menu_bar = Menubar(self,)
        self.setting_panel = Settingspanel(self)

        #placing the widgets 
        self.menu_bar.pack(fill='x',side='top',padx=10)
        self.editor_widget.pack(fill="both",expand=True , side="left",padx=10,pady=(0,10))
        self.side_menu.pack(fill="both",expand=True,padx=10,pady=0)            

        #pass the objects menu
        self.menu_bar.set_editor_widget(self.editor_widget)
        self.menu_bar.set_side_menu(self.side_menu)
        self.menu_bar.set_settings_panel(self.setting_panel)
        self.side_menu.set_editor_widget(self.editor_widget)
        self.setting_panel.set_side_menu(self.side_menu)

        self.deiconify()

        #open todays
        self.side_menu.calendar.selection_set(datetime.today())
        self.side_menu.date_selected()
        #set editor focus 

        self.editor_widget.focus_set()

        sv_ttk.set_theme(app_settings.Settings['Theme']) 

    def reload_app(self):
        app_settings.load_settings()
        self.reload()
        self.editor_widget.reload()
        self.menu_bar.reload()
        self.side_menu.reload()
        self.setting_panel.reload()
        
    def reload(self):
        self.configure(bg=app_settings.Settings['Background_color'])  
        sv_ttk.set_theme(app_settings.Settings['Theme']) 


    def disable_tags_button(self):
        self.menu_bar.disable_tags_button()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
