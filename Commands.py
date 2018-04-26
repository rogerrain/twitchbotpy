import inspect, sys

def getDict():
    """creating a dictionary of commands"""
    cd = {}
    fs = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    for c, f in fs:
        if "getDict" not in c:
            cd[c] = f
    return cd

def getLims():
    """creating a dictionary of time limits for each function"""
    ld = {}
    cd = getDict()
    for c in cd:
        ld[c] = cd[c]()[1]
    return ld

def commands():
    #TODO: make this command whisper instead of type in chat
    """creates a list of commands and sends them as the message"""
    comms = getDict()
    msg = "Commands: "
    for c in comms:
        msg += "!" + c + " "
    limit = 30 #Default of 30 seconds, feel free to change
    return msg, limit

"""Example command that could be added:
def keyboard():
    msg = "Cooler Master CM Storm QuickFire XT Slim Keyboard with Cherry MX \
Browns"
    limit = 30 #time restriction in seconds for the command
    return msg, limit
"""

def follow():
    """reminder for follows - not a generic exported command"""
    msg = "If you've been enjoying the stream, make sure to hit that follow \
button! c:"
    limit = 1200 #20 min by default, set to sys.maxsize if you don't want
                 #any follow notification
    return msg, limit
