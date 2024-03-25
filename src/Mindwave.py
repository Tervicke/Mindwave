import tkinter as tk
import app_settings
from EditorWidget import Editorwidget
from SideMenu import Sidemenu
from MenuBar import Menubar
from SettingsPanel import Settingspanel
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        app_settings.load_settings()
        self.configure(bg=app_settings.Settings['Background_color'])  
        self.title('Mindwave')
        self.geometry('900x620')
        self.iconphoto(False, tk.PhotoImage(file='icons/app_icon.png'))

        #Editing window
        self.editor_widget = Editorwidget(self)
        self.side_menu = Sidemenu(self)
        self.menu_bar = Menubar(self,)
        self.setting_panel = Settingspanel(self)
        self.editor_widget.set_template()
        #placing the widgets 
        self.menu_bar.pack(fill='x',side='top',padx=10)
        self.editor_widget.pack(fill="both",expand=True , side="left",padx=10,pady=10)
        self.side_menu.pack(fill="both",expand=True,padx=10)            

        #pass the objects menu
        self.menu_bar.set_editor_widget(self.editor_widget)
        self.side_menu.set_editor_widget(self.editor_widget)
        self.setting_panel.set_side_menu(self.side_menu)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
