#update trello

import requests
import extractBlocks
import json
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.trello.com/1"
board_id = "6a6844906edc8a926ee337ec"
DoneListId = "6a6844916edc8a926ee33858"
#idList = "6a6844916edc8a926ee33856"

def convert_block_to_card(block_data,toDoList,doneList,boardLabels):

    print(block_data)
    cardData = {
        # 'idList': f"{toDoList}",
        'name' : f'{block_data["id"]}',
        'desc' : f'{block_data["description"]}'
    }  

    for label in boardLabels.json():
        #print(block_data["track"], label["name"])
        if f'{block_data["track"]}' == label["name"]:
            label_data = [label["id"]]
            cardData.update({'idLabels' : label_data})
            # print(f"Label found: {block_data["track"]} || {label["id"]}")

    print(block_data["done"])

    if block_data["done"] == True:
        print("task Done")
        cardData.update({'idList' : {doneList}})
    else:
        print("task not done")
        cardData.update({'idList' : {toDoList}})


    return cardData

def getHeader():
    return  {
            "Accept": "application/json"
            }   

def getQuery():
    return  {
            'key': os.getenv("TRELLO_API_KEY"),
            'token': os.getenv("TRELLO_API_TOKEN")
            }

def getBoardLabels():
    response = requests.get(
    f"{base_url}/boards/{board_id}/labels",
    headers=getHeader(),
    params=getQuery()
    )
    return response

# print(response)
# print(response.text)
def getBoardLists():
    response = requests.get(
    f"{base_url}/boards/{board_id}/lists",
    headers= getHeader(),
    params= getQuery()
    )
    return response

# print(response)
# print(response.json()[0]["id"])
response = getBoardLists()
toDoListId = response.json()[0]["id"]

# print(ListID)
# print(response.text)

response = requests.get(
   f"{base_url}/boards/{board_id}/cards",
    headers= getHeader(),
    params= getQuery()
)

preUpdateCards = []
for card in response.json():
    preUpdateCards.append(card)

# response = getBoardLists()
# print(response)
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


#print(f"#$#$#$#$#$#$#$#$#$#$ {response.json()} #$#$#$#$#$#$#$#$#$")

# print(response)

# print(response.json())


# Extract blocks and formate them to json for API delivery

boardLabels= getBoardLabels()
# print(boardLabels.json())
# print(getBoardLists().json())
# print(json.dumps(json.loads(getBoardLists().text), sort_keys=True, indent=4, separators=(",", ": ")))

for block in extractBlocks.current_week_tasks():
    block_data = convert_block_to_card(block, toDoListId, DoneListId,boardLabels)
    header = getHeader()
    params = getQuery()
    params.update(block_data)
    # print(params)

#test for duplicate cards
    duplicateCard = False
    for i, card in enumerate(preUpdateCards):
        if block_data["name"] == card["name"]:
            duplicateCard = True
            upadateCardId = card["id"]
            print(f"dupe found: {upadateCardId}")

#if no duplicate found add to list
    if duplicateCard == False:
        response = requests.post(
        f"{base_url}/cards",
        headers=header,
        params=params
        )
        print(f"Card Created {params["name"]}")
        #print(response)
        #print(response.text)

# If duplicate found update duplicate
    else:
        response = requests.put(
        f"{base_url}/cards/{upadateCardId}",
        headers=header,
        params=params
        )
        print(f"Card Updated:  {params["name"]}")
        #print(response)
        #print(response.text)

        
    

    
    




#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
#for tasks in extractBlocks.current_week_tasks():
