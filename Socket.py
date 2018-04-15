import socket
from Settings import HOST, PORT, PASS, NICK, CHANNEL

#Transforms a string into bytes digestible by sockets
def toBytes(message):
    return bytes(message, "UTF-8")

#Opens a socket given the defined settings int he Settings.py file
def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    sysMessage(s, "PASS " + PASS)
    sysMessage(s, "NICK " + NICK)
    sysMessage(s, "JOIN #" + CHANNEL)
    return s

#Sends a message over the given socket to a channel
def sendMessage(s, message):
    temp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(toBytes(temp + "\r\n"))
    print("Sent: " + temp)

#Sends a message over the given socket to the server
def sysMessage(s, message):
    s.send(toBytes(message + "\r\n"))

def closeSocket(s):
    sendMessage(s, "Goodbye!")
    sysMessage(s, "PART " + CHANNEL)
    s.close()
