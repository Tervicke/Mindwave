import json
App_font = ("Arial" , 15)
Settings= {None}

def load_settings():
    global Settings
    with open('src/settings.json', 'r') as file:
        Settings = json.load(file)
    print(Settings)

def update_settings(setting_key,setting_value):
    global Settings
    if setting_key in Settings:
        Settings[setting_key] = setting_value
        with open("src/settings.json", 'w') as file:
            json.dump(Settings,file,indent=4)

