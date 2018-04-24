from Socket import openSocket, closeSocket, sendMessage, sysMessage
from Initialize import joinRoom
from Commands import getDict, getLims, follow
from Settings import getChannel
import re
import time

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

def checkTime(c, td, ld):
    """takes a command c, a time dictionary td, and a time limit dictionary
        ld to see if the command can be run yet"""
    current = time.time()
    if current - td[c] >= ld[c]:
        td[c] = current
        return td, True
    else:
        return td, False

def checkFollow(s, followtime):
    """sends a follow message periodically"""
    current = time.time()
    msg, limit = follow()
    if current - followtime >= limit:
        followtime = current
        sendMessage(s, msg)
    return followtime

def recognize(s, c, cd, td, ld):
    """attempts to recognize a command given by the user"""
    if c not in cd:
        return td
    td, ok = checkTime(c, td, ld)
    if ok:
        msg = cd[c]()[0]
        sendMessage(s, msg)
    return td

def main():
    s = openSocket()
    joinRoom(s)
    channel = getChannel()
    p = re.compile("!([a-zA-Z]+)") #Setting up pattern to match commands
    cd = getDict() #Dictionary of Commands
    td = {c: 0 for c in cd} #Initializing dictionary of most recent commands
    ld = getLims() #Dictionary of time limits for commands
    followtime = time.time()

    readBuffer, user, message = "", "", "" #Initializing needed variables
    try:
        while True:
            readBuffer = readBuffer + s.recv(1024).decode("UTF-8")
            temp = readBuffer.split("\n")
            readBuffer = temp.pop()
            followtime = checkFollow(s, followtime)

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
                        td = recognize(s, m.group(1), cd, td, ld)
                    #Checking if the broadcaster called for the bot to quit
                    if "!quit" in message and user == channel:
                        return
    finally:
        closeSocket(s)
        return

if __name__ == "__main__":
    main()
