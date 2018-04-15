from Socket import sendMessage

#Ensures that the bot successfully joined the room and notifies the user
def joinRoom(s):
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


#Helper function for joinRoom, checks whether the joining has ended
def loadingComplete(line):
    if ("End of /NAMES list" in line):
        return False
    else:
        return True
