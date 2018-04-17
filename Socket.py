import socket
from Settings import HOST, PORT, PASS, NICK, CHANNEL

def toBytes(message):
    """transforms a string into bytes digestible by sockets"""
    return bytes(message, "UTF-8")

def openSocket():
    """opens a socket given the defined settings int he Settings.py file"""
    s = socket.socket()
    s.connect((HOST, PORT))
    sysMessage(s, "PASS " + PASS)
    sysMessage(s, "NICK " + NICK)
    sysMessage(s, "JOIN #" + CHANNEL)
    return s

def sendMessage(s, message):
    """sends a message over the given socket to a channel"""
    temp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send(toBytes(temp + "\r\n"))
    print("Sent: " + temp)

def sysMessage(s, message):
    """sends a message over the given socket to the server"""
    s.send(toBytes(message + "\r\n"))

def closeSocket(s):
    """closes the socket connection gracefully"""
    sendMessage(s, "Goodbye!")
    sysMessage(s, "PART " + CHANNEL)
    s.close()
