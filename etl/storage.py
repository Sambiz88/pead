import json

def read_json():
    with open('data.json', 'r') as file:
        return json.load(file)


def write_json(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)