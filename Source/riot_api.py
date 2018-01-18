from requests import get
from cfg      import SUMMONER_ID, SUMMONER_NAME, API_KEY, API_REGION

def getSummonerInfo():
    URL = "https://" + API_REGION + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + SUMMONER_NAME + "?api_key=" + API_KEY

    return get(URL).json()

def getRankedInfo():
    URL = "https://" + API_REGION + ".api.riotgames.com/lol/league/v3/positions/by-summoner/" + SUMMONER_ID + "?api_key=" + API_KEY

    return get(URL).json()