from datetime import datetime


def sampleResponse(input_text):

    userMessage = str(input_text).lower()

    if userMessage in ("/hello", "/hi", "/whatsup",):
        return "nedi ala ne mazq elemisen ?"
    if userMessage in ("/help"):
        return "contract, whitepaper, website , social,  buyanis,"

    if userMessage in ("/contract", "//contract", "/whatsup",):
        return "#Network:\nBinance Smart Chain (#BSC)\n\n#Contract Adress:Also add the contract adress 👇 👇\n0xc7a66f9362c467e0e86459a34fa88605A0077Cda\n\n#Token Name:\nANIS\n\n#Symbol / Ticker:\nANIS\n\n#Decimal:6"


    if userMessage in ("/whitepaper", "//whitepaper", "///whitepaper","/whitelist",):
        return "https://www.aniscoin.finance/white-paper/"
    
    
    if userMessage in ("/website", "//website", "///website ",):
        return "https://www.aniscoin.finance/"


    if userMessage in ("/social", "///social", "///social",):
        return "Instagram:\nhttps://instagram.com/aniscoin?utm_medium=copy_link\n\nTwitter:\nhttps://twitter.com/ANIS_coin?t=oT8EgP3RHYRIL8LIa3ZYyQ&s=09\n\nTiktok:\nhttps://vm.tiktok.com/ZSe43ejS3/"
    
    
    if userMessage in ("/buy", "/BUY", "/buyanis",):
        return "BUY ANIS COIN👇\nhttps://cointool.app/ido/exchange?id=236b24272b2a2a202025222526262b7523772a2726272321202b7527217220252026575272502a5655526f2625"
    
    if userMessage in ("/NFT", "/nft", "",):
        return "BUY ANIS NFT👇\nhttps://opensea.io/collection/anis-nft"



    if userMessage in ("/time", "/time?", "/what is the time?", "/saat?"):
        now=datetime.now()
        dateTime=now.strftime("%d/%m/%y, %H:%M:%S")

        return str(dateTime)
