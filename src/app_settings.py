import json
App_font = ("Helvetica" , 15)
Settings= {  }
#color for blue -> 007AFF
#color for green -> 34C759
#color for red -> red

colors = {"Blue":"#007AFF" , "Red":"Red" , "Green":"#34c759"}

def load_settings():
    global Settings
    with open('src/settings.json', 'r') as file:
        temp = json.load(file)

        # Adding key-value pairs
        Settings["Theme"] = temp['Theme']
        Settings["Theme_color"] = temp['Theme_color']
        Settings["Diary_folder"] = temp['Diary_folder']
        Settings["Template"] = temp['Template']
        theme = temp["Theme"]

        # Dynamic update
        Settings["Background_color"] = temp[f"{theme}_Background_color"]
        Settings["Foreground_color"] = temp[f"{theme}_Foreground_color"]
        Settings["Text_color"] = temp[f"{theme}_Text_color"]
        Settings['Editor_foreground']=temp[f"{theme}_Editor_foreground"]
        Settings['Editor_background']=temp[f"{theme}_Editor_background"]
        Settings['Editor_insertbg']=temp[f"{theme}_Editor_insertbg"]

        Settings['Editor_selectbackground']=temp[f"{theme}_Editor_selectbackground"]
        Settings['Editor_highlightbackground']=temp[f"{theme}_Editor_hightlightbackground"]

def update_settings(setting_key,setting_value):
    global Settings
    with open('src/settings.json', 'r') as file:
        temp = json.load(file)
    if setting_key in temp:
        temp[setting_key] = setting_value
        with open("src/settings.json", 'w') as file:
            json.dump(temp,file,indent=4)

