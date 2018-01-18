from requests import get
from cfg      import SUMMONER_ID, SUMMONER_NAME, API_KEY, API_REGION
from json     import load
from buddies  import checkRune


def getSummonerInfo():
    URL = "https://" + API_REGION + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + SUMMONER_NAME + "?api_key=" + API_KEY

    return get(URL).json()

def getRankedInfo():
    URL = "https://" + API_REGION + ".api.riotgames.com/lol/league/v3/positions/by-summoner/" + SUMMONER_ID + "?api_key=" + API_KEY

    return get(URL).json()

def putTogetherAndGetRunesInfo():
    URL = "https://" + API_REGION + ".api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + SUMMONER_ID + "?api_key=" + API_KEY
    response = get(URL).json()
    primaryTree = ""
    primaryRunes = []
    secondaryTree = ""
    secondaryRunes = []

    if "gameId" not in response:
        return "Komor isn't currently in a game"

    with open("runeStyles.json") as runeStyles:
        runeStylesData = load(runeStyles)

        for runeStyle in runeStylesData:
            if runeStyle["id"] == response["participants"][0]["perks"]["perkStyle"]:
                primaryTree = runeStyle["name"]
                break

        for runeStyle in runeStylesData:
            if runeStyle["id"] == response["participants"][0]["perks"]["perkSubStyle"]:
                secondaryTree = runeStyle["name"]
                break

    with open("runes.json") as runes:
        runesData = load(runes)

        for rune in runesData:
            if checkRune(rune["id"], response["participants"][0]["perks"]["perkIds"]):
                if primaryTree in rune["iconPath"]:
                    primaryRunes.append(rune["name"])
                elif secondaryTree in rune["iconPath"]:
                    secondaryRunes.append(rune["name"])

    return primaryTree + ": " + primaryRunes[0] + ", " + primaryRunes[1] + ", " + primaryRunes[2] + ", " + primaryRunes[3] + " ||| " + secondaryTree + ": " + secondaryRunes[0] + ", " + secondaryRunes[1]
