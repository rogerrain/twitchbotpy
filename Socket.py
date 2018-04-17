import socket
from Settings import getChannel, getSettings

def toBytes(message):
    """transforms a string into bytes digestible by sockets"""
    return bytes(message, "UTF-8")

def openSocket():
    """opens a socket given the defined settings int he Settings.py file"""
    host, port, pw, nick, channel = getSettings()
    s = socket.socket()
    s.connect((host, port))
    sysMessage(s, "PASS " + pw)
    sysMessage(s, "NICK " + nick)
    sysMessage(s, "JOIN #" + channel)
    return s

def sendMessage(s, message):
    """sends a message over the given socket to a channel"""
    channel = getChannel()
    temp = "PRIVMSG #" + channel + " :" + message
    s.send(toBytes(temp + "\r\n"))
    print("Sent: " + temp)

def sysMessage(s, message):
    """sends a message over the given socket to the server"""
    s.send(toBytes(message + "\r\n"))

def closeSocket(s):
    """closes the socket connection gracefully"""
    channel = getChannel()
    sendMessage(s, "Goodbye!")
    sysMessage(s, "PART " + channel)
    s.close()
