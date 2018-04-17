def getSettings():
    return getHost(), getPort(), getPass(), getNick(), getChannel()

def getHost():
    infile = open("Settings.ini", "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        if line.startswith("HOST"):
            return line.strip().split(" ")[2]
        
def getPort():
    infile = open("Settings.ini", "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        if line.startswith("PORT"):
            return int(line.strip().split(" ")[2])
        
def getPass():
    infile = open("Settings.ini", "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        if line.startswith("PASS"):
            return line.strip().split(" ")[2]
        
def getNick():
    infile = open("Settings.ini", "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        if line.startswith("NICK"):
            return line.strip().split(" ")[2]
        
def getChannel():
    infile = open("Settings.ini", "r")
    lines = infile.readlines()
    infile.close()
    for line in lines:
        if line.startswith("CHANNEL"):
            return line.strip().split(" ")[2]
