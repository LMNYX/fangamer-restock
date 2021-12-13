import yaml, time, requests, os
from module import *

if (not os.path.exists("config.yml")):
    ConfigStream = open("config.yml", 'w')
    yaml.dump(DefaultConfig, ConfigStream)
ConfigStream = open("config.yml", 'r+')
ConfigObject = yaml.safe_load(ConfigStream.read())

if (ConfigObject['Misc']['ConfigVer'] < DefaultConfig['Misc']['ConfigVer']):
    print("[WARNING]: Your config is out of date! Please look into updating it.")

if(ConfigObject['Misc']['Motd']):
    print("\n" +
        "Hey!! Thanks for using Fangamer Restock Scraper, that I made just to get my hands on Vallhalla's Vinyl set." + "\n"
        + "I hope you'll get something yourself too and will enjoy the merch :)" + "\n"
        + "- mishashto (or LMNYX) <3" + "\n")
    time.sleep(1)

print("Checking if product specified in the config actually exists.")

_ExistenceOrHTML = CheckExistance(ConfigObject['Collection'])

if(_ExistenceOrHTML == False):
    print("Product doesn't exist. Stopping the sequence...")
    os._exit(0)

_pName = GetProductName(_ExistenceOrHTML)

print("Starting the loop...")

_URL = CompileURL(ConfigObject['Collection'])

_LoopTimer = 0
IsFinallyAvailable = False
Time = int(ConfigObject['Misc']['CheckOnTimer'])
while(not IsFinallyAvailable):
    try:
        _tAvailability = IsAvailableToBuy(GetAvailabilityData(GetContent(_URL)))
        if(_tAvailability):
            dprint(f"[loop{_LoopTimer}] Available now!")
            IsFinallyAvailable = True
            AnnounceAvailability(ConfigObject['Notification'], _pName, ConfigObject['Collection'])
        else:
            dprint(f"[loop{_LoopTimer}] Still not available.")
    except Exception as e:
        dprint("Error: "+str(e))

    _LoopTimer += 1
    time.sleep(Time)
