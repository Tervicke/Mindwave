import json
#App_font = ("Helvetica",15)
App_font = ()
Settings= {}
#color for blue -> 007AFF
#color for green -> 34C759
#color for red -> red
from datetime import datetime , timedelta
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
        Settings['Combobox_foreground'] = temp[f'{theme}_Foreground_color']
        Settings['Disable_streaks'] = temp['Disable_streaks']
        load_font(temp['Font']['font-face'] , temp['Font']['font-size'])
        last_date_recorded = datetime.strptime(temp['Last_date_recorded'], "%Y-%m-%d").date() #change the last recorded date to datetime object
        today_date = datetime.today().date()
        if not last_date_recorded == today_date:
            #do everything if the last recorded date is not today :

            #check if the last recorded date was yesterday
            yesterday_date = today_date  - timedelta(days=1)  #get todays date
            current_streak = int(temp['Streaks'])
            print("current streak" , current_streak)
            updated_streak = 1 #default is 1
            if last_date_recorded == yesterday_date:
                updated_streak = current_streak + 1
                print("true")

            Settings['Streaks'] = updated_streak 
            update_settings("Streaks",updated_streak)

            #update last recorded date
            update_settings("Last_date_recorded",str(datetime.today().date()))
        else:
            Settings['Streaks'] = temp['Streaks']
def load_font(font_face , font_size): #creating a temp font container list and then converting to a tuple at the end
    global App_font
    temp_font = []
    temp_font.append(font_face)
    temp_font.append(font_size)
    App_font = tuple(temp_font)

def update_settings(setting_key,setting_value):
    global Settings
    with open('src/settings.json', 'r') as file:
        temp = json.load(file)
    if setting_key in temp:
        temp[setting_key] = setting_value
        with open("src/settings.json", 'w') as file:
            json.dump(temp,file,indent=4)

def update_font(font_face,font_size):
    #update the font in the setting and then load_font again  
    with open('src/settings.json', 'r') as file:
        temp = json.load(file)
        temp["Font"]['font-face'] =  font_face
        temp["Font"]['font-size'] =  font_size
        with open("src/settings.json", 'w') as file:
            json.dump(temp,file,indent=4)
        load_font(font_face,font_size)

