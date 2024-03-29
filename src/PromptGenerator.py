import google.generativeai as genai
import json
from datetime import datetime
import os
from dotenv import load_dotenv

def get_current_time_formatted():
    # Get the current time
    now = datetime.now()
    # Format the time as "HH:MM am/pm"
    formatted_time = now.strftime("%I:%M %p").lower()
    return formatted_time

prompt_template=f'''
Give me 1 open ended question that i can ask my friend that will help him reflect on himself at [time] give it to me in json format with 2 keys called question_type and question_text
'''
prompt=f'''
give me journal format for today
'''
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-pro')
def trim_first_and_last_line(text):
    lines = text.splitlines()
    trimmed_lines = lines[1:-1]
    trimmed_text = '\n'.join(trimmed_lines)
    return trimmed_text

def get_current_time_formatted():
    # Get the current time
    now = datetime.now()
    # Format the time as "HH:MM am/pm"
    formatted_time = now.strftime("%I:%M %p").lower()
    return formatted_time

def generate_prompt(retries = 3):
    if retries <=  0:
        return "Error "
    update_prompt = prompt_template.replace('[time]',get_current_time_formatted())
    response = model.generate_content(update_prompt)
    try:
        temp = json.loads(trim_first_and_last_line(response.text))
        return temp
    except json.JSONDecodeError as e:
        print(f'Error decoding json')
        return generate_prompt(retries-1)
print(model.generate_content(prompt))
