import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
baseUrl = "https://api.trello.com"


yourAPIKey = os.getenv("TRELLO_API_KEY")
yourAPIToken = os.getenv("TRELLO_API_TOKEN")

response = requests.get(f"https://api.trello.com/1/members/me/?key={yourAPIKey}&token={yourAPIToken}")
#print(response.status_code, response.text)

trelloId = response.json()["id"]
#print(trelloId)

#response = requests.get(f"{baseUrl}/1/boards/{trelloId}")

def getHeader():
    return  {
            "Accept": "application/json"
            }   

def getQuery():
    return  {
            'key': os.getenv("TRELLO_API_KEY"),
            'token': os.getenv("TRELLO_API_TOKEN")
            }


# response = requests.get(
#    f"{baseUrl}/1/members/me/boards",
#    headers=headers,
#    params=query
# )

#response.raise_for_status()
#print(json.dumps(response.json(), indent=2))
board_id = "6a6844906edc8a926ee337ec"

print(response.text)
#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

