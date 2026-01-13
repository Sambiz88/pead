import json

def load(data):
    ### LOAD ###
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)