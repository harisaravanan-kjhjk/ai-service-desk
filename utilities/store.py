USER_FILE="user.json"
import os
import json

def load():
    if not os.path.exist(USER_FILE):
        return {}
    else:
        with open(USER_FILE,"r") as f:
            return json.load(f)
        
def store(users):
    with open(USER_FILE,"w") as file:
        json.dump(users,file,indent=4)
     