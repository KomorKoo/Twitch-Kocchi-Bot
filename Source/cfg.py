HOST          = "irc.twitch.tv"
PORT          = 6667
NICK          = "kocchibot"
PASS          = "oauth:f0poxer58r8997acjj28e2u0d4l6ac"
CHANNEL       = "komor_"
DELAY_RATE    = 3

SUMMONER_NAME     = "AloeKing"
SUMMONER_ID       = "25333756"
API_KEY           = "RGAPI-3be23697-fad6-4ab9-b922-23c9f1c1194f"
API_REGION        = "eun1"
REGION            = "eune"

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