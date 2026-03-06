data = {
    "notes": []
}

dict1 = {
    "note_id": 1,
    "note": "Note Message"
}



data["notes"].append(dict(dict1))

data["notes"][0]["note"] == "Note3"

print(data)

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
