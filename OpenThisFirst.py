def main():
    """configuring the settings for the twitch bot"""
    pw = input("Paste the Oauth token generated for your bot's account from \
https://twitchapps.com/tmi/ (may have to right click to paste): ")
    nick = input("What your bot's name (All lowercase is recommended)? ")
    chan = input("What is the name of the channel your bot will be in? ")
    
    outfile = open("Settings.ini", "w")
    outfile.write("HOST = irc.twitch.tv\n")
    outfile.write("PORT = 6667\n")
    outfile.write("PASS = {a}\n".format(a=pw))
    outfile.write("NICK = {a}\n".format(a=nick))
    outfile.write("CHANNEL = {a}\n".format(a=chan))
    outfile.close()

if __name__ == "__main__":
    main()
