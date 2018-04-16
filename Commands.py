# MAKE SURE YOUR COMMANDS ARE DEFINED AT THE TOP OF THIS FILE
# ALSO MAKE SURE TO ADD EACH COMMAND INTO THE commandList AT THE BOTTOM

"""Example command that could be added:
def keyboard():
    msg = "Cooler Master CM Storm QuickFire XT Slim Keyboard with Cherry MX \
Browns"
    return msg
"""

#External command to perform one of the functions in the commandList
def doComm(c):
    return commandDict[c]()

#Initialization of the dictionary of commands
def makeDict():
    for c in commandList:
        commandDict[c.__name__] = c

#List of exported commands
#If you have a command called keyboard() and a command called subscribe(), 
#the list should be [keyboard, subscribe]
commandList = [] #FILL THIS UP WITH ALL COMMANDS YOU ADD AS STRINGS

#Dictionary for executing commands and exported list of command strings
commandDict = {}
makeDict()
commandStrings = [c.__name__ for c in commandList]
