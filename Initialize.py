from Socket import sendMessage

def joinRoom(s):
    """Ensures that the bot successfully joined the room"""
    readBuffer = ""
    loading = True
    while loading:
        readBuffer = readBuffer + s.recv(1024).decode("UTF-8")
        temp = readBuffer.split("\n")
        readBuffer = temp.pop()

        for line in temp:
            print(line)
            loading = loadingComplete(line)
            
    sendMessage(s, "Successfully joined chat")

def loadingComplete(line):
    """Helper function for joinRoom, checks whether the joining has ended"""
    return "End of /NAMES list" not in line
