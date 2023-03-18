import requests
import json

def SendMessage(TOKEN,kanalid,Message):
    headers={
        'Authorization':TOKEN
    }
    Message={
        'content':Message
    }


    r=requests.post(f'https://discord.com/api/v9/channels/{kanalid}/messages',headers=headers,data=Message)
    return r

def RetrieveMessage(Kanalid,Token):
    header={
    'Authorization': Token
    }
    r=requests.get(f'https://discord.com/api/v9/channels/{Kanalid}/messages',headers=header)
    jsonn=json.loads(r.text)
    for deger in jsonn:
        return deger['content']

def MadenKontrol(Token,Kanalid):
    header={
    'Authorization': Token
    }
    r=requests.get(f'https://discord.com/api/v9/channels/{Kanalid}/messages',headers=header)
    jsonn=json.loads(r.text)
    for deger in jsonn:
        if(deger['content']==""):
            if((deger['embeds'][0]['fields'][0]['name'])==("**Madende şunları buldun:**")):
                return True
    return False

def Kazmakontrol(Token,Kanalid):
    header={
    'Authorization': Token
    }
    r=requests.get(f'https://discord.com/api/v9/channels/{Kanalid}/messages',headers=header)
    jsonn=json.loads(r.text)
    for deger in jsonn:
        if ('Kazman kırıldı!'in deger['content']):
            return True
        return False



