import json

def read_json():
    with open('data.json', 'r') as file:
        return json.load(file)


def write_json(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def change_attribute_name(old_key, new_key):

    data_list = read_json()

    for obj in data_list:
        if old_key in obj:
            obj[new_key] = obj.pop(old_key)

    write_json(data_list)