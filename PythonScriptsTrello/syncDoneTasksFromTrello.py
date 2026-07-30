import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.trello.com/1"
board_id = "6a6844906edc8a926ee337ec"
DoneListId = "6a6844916edc8a926ee33858"

def getHeader():
    return  {
            "Accept": "application/json"
            }   

def getQuery():
    return  {
            'key': os.getenv("TRELLO_API_KEY"),
            'token': os.getenv("TRELLO_API_TOKEN")
            }

def getBoardLists():
    response = requests.get(
    f"{base_url}/lists/{DoneListId}/cards?fields=name",
    headers= getHeader(),
    params= getQuery()
    )
    return response

response= getBoardLists()
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))