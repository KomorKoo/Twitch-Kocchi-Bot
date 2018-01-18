from cfg      import *
from buddies  import *
from riot_api import *

timePassed = 0

def sendMessage(sock, message):
    sock.send(bytes("PRIVMSG #" + CHANNEL + " :" + message + "\r\n", "UTF-8"))

    
def respondToCommand(sock, message):
    if "@kocchibot" in message.lower():
        sendMessage(sock, randomizePhrase())
        
    elif message == "!commands":
        sendMessage(sock, "Available commands: !rank, !playlist, !commands, !uptime, !lvl, !opgg")
        
    elif message == "!playlist":
        sendMessage(sock, "Current playlist (radio): https://www.pandora.com/station/play/3461770720952515429")
        
    elif message == "!uptime":
        sendMessage(sock, getUpTime())

    elif message == "!rank":
        rankedInfo = getRankedInfo()

        if "rank" not in rankedInfo:
            sendMessage(sock, "Haven't finished placements yet")

    elif message == "!lvl":
        summonerInfo = getSummonerInfo()

        sendMessage(sock, "Account level: " + str(summonerInfo["summonerLevel"]))

    elif message == "!opgg":
        sendMessage(sock, getOPGG())

def readMessage(sock, message, username):
    '''
    if lookForCapsLock(message):
        sendMessage(sock, ".timeout {} 60".format(username))
        sendMessage(sock, "@{}, don't abuse CapsLock! (timeout for 60 seconds)".format(username))
        
    elif lookForSwears(message):
        sendMessage(sock, ".timeout {} 60".format(username))
        sendMessage(sock, "@{}, don't curse that much! (timeout for 60 seconds)".format(username))
        
    elif lookForLongMsg(message):
        sendMessage(sock, ".timeout {} 60".format(username))
        sendMessage(sock, "@{}, don't put walls of text! (timeout for 60 seconds)".format(username))
        
    else:
	
    if "jd" in message.lower():
        sendMessage(sock, ".ban {} 3600".format(username))
        sendMessage(sock, ":))))))")
	'''

    global timePassed
    if time() - timePassed > DELAY_RATE:
        respondToCommand(sock, message)
        timePassed = time()