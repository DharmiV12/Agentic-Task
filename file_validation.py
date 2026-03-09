import os
import json


def task_file(filepath):

    struct = {
            "tasks": []
        }

    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write(json.dumps(struct))

            print("Task json file created")

        return filepath
    
    else:
        return filepath
    

def notes_file(filepath):

    struct = {
            "notes": []
        }

    if not os.path.exists(filepath):
        with open(filepath, 'w') as file:
            file.write(json.dumps(struct))

            print("Notes json file created")

        return filepath
    
    else:
        return filepath