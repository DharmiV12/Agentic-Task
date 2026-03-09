import re
import json
from file_validation import *

notes_filepath = "D:/DHARMI/Final Test/notes.json"
task_flepath = "D:/DHARMI/Final Test/task.json"

query = input("Enter a query: ")


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

                print("Already in file")

                return "Note already in notes"
        
        
        data["notes"].append(dict(note))

        print(f"After note added: {data}")

        json_data = json.dumps(data, indent=3)

        with open(notes_file_path, 'w') as f:
            f.write(json_data)

        print(f"Notes added to the JSON file\n")

        return "Note added successfully"

    except Exception as e:
        return f"Error: {str(e)}"



note_add(query)