import json

# Parses a request from the main UI (in JSON) to a dictionary
# object.
def parseRequest(requestJSON):
    data = json.loads(requestJSON)
    return data
