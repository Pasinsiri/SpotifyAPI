import json

def load_api_key():
    f = open('keys/credentials.json', 'r').read()
    data = json.loads(f)
    cred_id = data["id"]
    cred_secret = data["secret"]
    return cred_id, cred_secret