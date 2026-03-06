import json
import os
import requests


WEATHER_API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

notes_file_path = "D:/DHARMI/Final Test/notes.json"

task_fle_path = "D:/DHARMI/Final Test/task.json"


def task_add(query: str):

    try:
        with open(task_fle_path, 'r') as f:
            data = json.load(f)

        print(data)
        print(type(data))

        print("length of data", len(data))
        print("length of data", len(data["tasks"]))

        task = {
            'id':len(data["tasks"]) + 1,
            'task': query,
            'status': 'Pending'
        }

        data["tasks"].append(dict(task))

        print(f"After task added: {data}")

        json_data = json.dumps(data, indent=3)

        with open(task_fle_path, 'w') as f:
            f.write(json_data)

        print("Tasks added to the json file")

        return "Task added Successfully"

    except Exception as e:
        return f"Error: {str(e)}"

def task_get(query:str):

    try:
        with open(task_fle_path, 'r') as f:
            data = json.load(f)

        return data
    
    except Exception as e:
        return f"Error: {str(e)}"
    

def note_add(query:str):
    try:

        with open(notes_file_path, 'r') as f:
            data = json.load(f)

        print(data)
        print(type(data))

        print("length of data", len(data))
        print("length of data", len(data["notes"]))

        note = {'id': len(data["notes"]) + 1,
                'note': query}
        
        data["notes"].append(dict(note))

        print(f"After note added: {data}")
        
        json_data = json.dumps(data, indent=3)

        with open(notes_file_path, 'w') as f:
            f.write(json_data)

        print("Notes added to the JSON file")

        return "Note added successfully"

    except Exception as e:
        return f"Error: {str(e)}"
    

def note_get(query: str):

    try:
        with open(notes_file_path, 'r') as f:
            data = json.load(f)

        return data
    
    except Exception as e:
        return f"Error: {str(e)}"
    

def weather_get(city_name: str):
    try:
        request_url = f"{BASE_URL}?q={city_name}&units=metric&appid={WEATHER_API_KEY}"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            print(f"Weather data: {data}")
            return data
        
        else:
            return "Error in response"
        
    except Exception as e:
        return f"Error: {str(e)}"
        
