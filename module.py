import requests
from bs4 import BeautifulSoup

DefaultConfig = {
    "Collection": 
    {
        "Game": "va-11-hall-a",
        "Product": "va-11-hall-a-complete-sound-collection-box-set"
    },
    "Notification":
    {
        "DiscordWebhook": "",
        "CustomRequest": ""
    },
    "Misc":
    {
        "CheckOnTimer": 120,
        "Motd": True,
        "ConfigVer": 1
    }
}

IsDebug = True

def dprint(*a):
    if(IsDebug):
        print(*a)

def DecompileCollectionData(CollectionData):
    return f"/collections/{CollectionData['Game']}/products/{CollectionData['Product']}"

def CompileURL(CollectionData):
    return f"https://www.fangamer.com{DecompileCollectionData(CollectionData)}"

def CheckExistance(CollectionData):
    _dURI = CompileURL(CollectionData)
    dprint(_dURI)

    _testSub = requests.get(_dURI)
    
    if _testSub.status_code == 404: return False
    else: return _testSub.content
    
def GetContent(URL):
    return requests.get(URL).content

def GetProductName(html):
    return BeautifulSoup(html, 'html.parser').title.text.split(' - Fangamer')[0]

def GetAvailabilityData(html):
    soup = BeautifulSoup(html, 'html.parser')

    _meta = soup.select('meta[itemprop="availability"]')
    
    return _meta[0].attrs['content']

def IsAvailableToBuy(MetaValue):
    return MetaValue.lower() == "instock"

def AnnounceAvailability(NotificationData, ProductName, CollectionData):

    if(NotificationData['DiscordWebhook'] != ""):
        dprint("Sending notification to discord webhook...")
        requests.post(NotificationData['DiscordWebhook'], {
        "content": f"{ProductName} is available on Fangamer now!!\n\n{CompileURL(CollectionData)}"})

    if(NotificationData['CustomRequest'] != ""):
        requests.post(NotificationData['CustomRequest'], {"available": True, "product": CollectionData})

    return