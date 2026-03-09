import json
import requests
from file_validation import *
import re
import os

WEATHER_API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

notes_filepath = "D:/DHARMI/Final Test/notes.json"
task_flepath = "D:/DHARMI/Final Test/task.json"


def task_add(query: str):

    try:

        task_file_path = task_file(task_flepath)

        with open(task_file_path, 'r') as f:
            data = json.load(f)

        print(data)
        print(type(data))

        print("length of data", len(data))
        print("length of data", len(data["tasks"]), "\n")

        task = {
            'id':len(data["tasks"]) + 1,
            'task': query,
            'status': 'Pending'
        }

        for t in data["tasks"]:
            if t["task"] == query:

                print("task is exist")

                return "Task is exist in task.json file"


        data["tasks"].append(dict(task))

        print(f"After task added: {data}\n")

        json_data = json.dumps(data, indent=3)

        with open(task_file_path, 'w') as f:
            f.write(json_data)

        print("Tasks added to the json file\n")

        return "Task added Successfully"

    except Exception as e:
        return f"Error: {str(e)}"


def task_get(query:str):

    try:

        if not os.path.exists(task_flepath):
            return "File is not found"

        with open(task_flepath, 'r') as f:
            data = json.load(f)

        print("Listed all the tasks\n")

        return data
    
    except Exception as e:
        return f"Error: {str(e)}"
    

def task_status_updation(query):
    
    try:

        print("Function task status updation is called..")

        print(f"Query: {query}")

        if not os.path.exists(task_flepath):
            return "File is not found"

        with open(task_flepath, 'r') as f:
            data = json.load(f)

        lst_id = re.findall(r'\d+', query)

        task_id = int(lst_id[0])

        print(f"Task id for updation is: {task_id}")

        for task in data["tasks"]:
            if task['id'] == task_id:
                task['status'] = "Completed"
                print(f"Updated task: {task}\n")    

                json_data = json.dumps(data, indent=3)

                with open(task_flepath, 'w') as f:
                    f.write(json_data)  

        print(f"Data: {data}\n")

        print(f"Task {task_id}'s status updated")

        return data

    except Exception as e:
        f"Error: {str(e)}"
    

def note_add(query:str):

    try:

        notes_file_path = notes_file(notes_filepath)

        with open(notes_file_path, 'r') as f:
            data = json.load(f)

        print(data)
        print(type(data))

        print("length of data", len(data))
        print("length of data", len(data["notes"]))

        note = {'id': len(data["notes"]) + 1,
                'note': query}
        
        for n in data["notes"]:
            if n["note"] == query:

                print("Note is already in file")

                return "Note already in notes files"
        
            
        data["notes"].append(dict(note))

        print(f"After note added: {data}")

        json_data = json.dumps(data, indent=3)

        with open(notes_file_path, 'w') as f:
            f.write(json_data)

        print(f"Notes added to the JSON file\n")

        return "Note added successfully"

    except Exception as e:
        return f"Error: {str(e)}"
    

def note_get(query: str):

    try:

        if not os.path.exists(notes_filepath):
            return "File is not found"
        
        with open(notes_filepath, 'r') as f:
            data = json.load(f)

        print("Listed all the notes\n")

        return data
    
    except Exception as e:
        return f"Error: {str(e)}"
    

def weather_get(city_name: str):
    
    try:
        request_url = f"{BASE_URL}?q={city_name}&units=metric&appid={WEATHER_API_KEY}"
        response = requests.get(request_url)

        if response.status_code == 200:
            
            data = response.json()
            print(f"Weather data: {data}\n")
            return data
        
        else:
            return "Error in response"
        
    except Exception as e:
        return f"Error: {str(e)}"
    