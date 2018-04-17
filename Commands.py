import inspect, sys

def getDict():
    """creating a dictionary of commands"""
    cd = {}
    fs = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    for c, f in fs:
        if "getDict" not in c:
            cd[c] = f
    return cd

"""Example command that could be added:
def keyboard():
    msg = "Cooler Master CM Storm QuickFire XT Slim Keyboard with Cherry MX \
Browns"
    return msg
"""
