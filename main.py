import requests
import pandas as pd
from glom import glom
from champ_dict import champ_binary_obj 
champ_binary= champ_binary_obj


API_KEY = "RGAPI-37df93cc-60f0-4485-b7d8-8d825ceadb89"

# summoner_name="6C0di9"
SERVER = "europe"
MATCH_ID = "EUW1_5868146939"

data = requests.get(f'https://{SERVER}.api.riotgames.com/lol/match/v5/matches/{MATCH_ID}/timeline/?api_key={API_KEY}')
#print(data.json()["metadata"])
after_game_data = requests.get(f'https://{SERVER}.api.riotgames.com/lol/match/v5/matches/{MATCH_ID}/?api_key={API_KEY}')
#print(after_game_data.json())

after_game_data = after_game_data.json()["info"]["participants"]
frames = data.json()["info"]["frames"]
frames=frames[:14] #up to minute 14

df=pd.DataFrame(champ_binary)
def get_after_game_stats(arr):
    for champ in arr:
        champ_binary[champ["championId"]] = 1
        #champ["lane"]
        #champ["perks"]
    
get_after_game_stats(after_game_data)
print(df)
