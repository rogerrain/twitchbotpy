from Socket import openSocket, closeSocket, sendMessage, sysMessage
from Initialize import joinRoom
from Commands import commandList, doComm
from Settings import CHANNEL
import re

#Obtains the username from the given line
def getUser(line):
    separate = line.split(":")
    user = separate[1].split("!")[0]
    return user

#Obtains the message from the given line
def getMessage(line):
    separate = line.split(":")
    message = separate[2]
    return message

#Attempts to recognize a command given by the user
def recognize(s, comm):
    if comm not in commandList:
        return
    c = comm + "()"
    msg = doComm(c) #Executes the command corresponding to comm
    sendMessage(s, msg)
    return

def main():
    s = openSocket()
    joinRoom(s)
    p = re.compile("!([a-zA-Z]+)") #Setting up pattern to match commands

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
                    recognize(s, m.group(1))
                #Checking if the broadcaster called for the bot to quit
                if "!quit" in message and user == CHANNEL:
                    closeSocket(s)
                    return

if __name__ == "__main__":
    main()
