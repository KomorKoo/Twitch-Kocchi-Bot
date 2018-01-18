HOST          = "irc.twitch.tv"
PORT          = 6667
NICK          = #<bot's twitch nickname>
PASS          = #<twitch authorization code>
CHANNEL       = #<channel>
DELAY_RATE    = 3

SUMMONER_NAME     = #<lol nickname>
SUMMONER_ID       = #<lol summoner id>
API_KEY           = #<riot's API key>
API_REGION        = #<i. e. eun1, not eune>
REGION            = #<region>

import socket
from bot import sendMessage

def initSocket():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send(bytes("PASS "  + PASS    + "\r\n", "UTF-8"))
    sock.send(bytes("NICK "  + NICK    + "\r\n", "UTF-8"))
    sock.send(bytes("JOIN #" + CHANNEL + "\r\n", "UTF-8"))
    sendMessage(sock, "Connected")
    print("KocchiBot has connected")

    return sock