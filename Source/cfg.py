HOST          = "irc.twitch.tv"
PORT          = 6667
DELAY_RATE    = 3


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
