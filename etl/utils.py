import json

def load_json_data():

    with open('data.json', 'r') as file:
        return json.load(file)