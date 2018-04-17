from Socket import openSocket, closeSocket, sendMessage, sysMessage
from Initialize import joinRoom
from Commands import getDict
from Settings import CHANNEL
import re

def getUser(line):
    """obtains the username from the given line"""
    separate = line.split(":")
    user = separate[1].split("!")[0]
    return user

def getMessage(line):
    """obtains the message from the given line"""
    separate = line.split(":")
    message = separate[2]
    return message

def recognize(s, c, cd):
    """attempts to recognize a command given by the user"""
    if c not in cd:
        return
    msg = cd[c]()
    sendMessage(s, msg)
    return

def main():
    s = openSocket()
    joinRoom(s)
    p = re.compile("!([a-zA-Z]+)") #Setting up pattern to match commands
    cd = getDict()

    readBuffer, user, message = "", "", "" #Initializing needed variables
    while True:
        readBuffer = readBuffer + s.recv(1024).decode("UTF-8")
        temp = readBuffer.split("\n")
        readBuffer = temp.pop()

        for line in temp:
            if "PING :tmi.twitch.tv" in line:
                if "PING :tmi.twitch.tv" == line[:19]:
                    print(line)
                    sysMessage(s, (line.replace("PING", "PONG")))
                else:
                    sendMessage(s, "Nice try.") #Preventing shennanigans
            else:
                user = getUser(line)
                message = getMessage(line)
                print(user + " typed :" + message)
                m = p.match(message) #Pattern matching for commands
                if m:
                    recognize(s, m.group(1), cd)
                #Checking if the broadcaster called for the bot to quit
                if "!quit" in message and user == CHANNEL:
                    closeSocket(s)
                    return

if __name__ == "__main__":
    main()
