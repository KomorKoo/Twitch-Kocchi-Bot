from time   import time
from random import randint
from cfg    import SUMMONER_NAME, REGION

start = int(time())


def getUpTime():
    global start

    seconds = int(time()) - start
    minutes = int(seconds / 60)
    hours   = int(minutes / 60)
    seconds = seconds - hours * 3600 - minutes * 60
    
    return "Komor's bot has been inting for: {}h {}m {}s.".format(hours, minutes, seconds)


def randomizePhrase():
    phrases = [
        "Sup sweetheart",
        "Leave me alone",
        "You can give me suggestions on what she can answer xd",
    ]
    
    return phrases[randint(0, len(phrases)-1)]


def lookForCapsLock(message):
    capsCounter = 0
    
    if len(message) > 10:
        for char in message:
            if char == char.upper():
                capsCounter += 1
        if float(capsCounter)/float(len(message)) > 0.6:
            return True
        else:
            return False
    else:
        return False


def lookForSwears(message):
    swearsCounter = 0
    swears = [
        "kurwa",
        "chuj"
    ]
    
    for element in message.split():
        for swear in swears:
            if element.lower() == swear:
                swearsCounter += 1
    if swearsCounter > 5:
        return True
    else:
        return False

    
def lookForLongMsg(message):
    if len(message) > 480:
        return True
    else:
        return False


def getOPGG():
    return "http://" + REGION+ ".op.gg/summoner/userName=" + SUMMONER_NAME


def checkRune(runeId, runeIds):
    for id in runeIds:
        if runeId == id:
            return True

    return False