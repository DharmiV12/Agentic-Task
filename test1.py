import json

file_path = "D:/DHARMI/Final Test/notes.json"

#data = input("Enter a data to add json: ")

def json_dump():

    with open(file_path, 'r') as f:
            data = json.load(f)

    print(data)

    result = data

    print(result)

    print(type(data))

    dict1 = {
        "note_id": 1,
        "note": "Note Message"
    }


    data["notes"].append(dict(dict1))

    print(f"Afetr data adding: {data}")

    print("length of data", len(data))
    print("length of data", len(data["notes"]))


    dict2 = {
        "note_id": 2,
        "note": "Note Message2"
    }

    data["notes"].append(dict(dict2))

    print(data)

    print("length of data", len(data))
    print("length of data", len(data["notes"]))

    json_data = json.dumps(data, indent=3)

    with open(file_path, 'w') as f:
          f.write(json_data)

json_dump()
