from cfg import initSocket
from bot import readMessage

sock = initSocket()
message = ""

while True:
    for line in str(sock.recv(1024)).split('\\r\\n'):
        parts = line.split(':')

        if len(parts) < 3:
            continue

        if line[0] == "PING":
            sock.send(bytes("PONG {}\r\n".format(line[1])), "UTF-8")

        elif "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]

        usernameSplit = parts[1].split("!")
        username      = usernameSplit[0]

        readMessage(sock, message, username)
