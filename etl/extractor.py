import json

### EXTRACT ###
## Fetch ##
# Source : https://site.financialmodelingprep.com/developer/docs


def stage(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def get_jsonparsed_data(url):
    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen

    import certifi

    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

def extract():

    url = "https://financialmodelingprep.com/stable/earnings-calendar?apikey=L54QP5GBSaLen2zBLHu5VxtBRk36WGt7"

    parsed_data = get_jsonparsed_data(url)

    ## Dump ##
    stage(parsed_data)

    print("Data saved to data.json")





