import requests

def data(TOKEN,CHAT_ID,mesage):
    TOKEN = TOKEN
    CHAT_ID = CHAT_ID
    MESAJ = mesage
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": MESAJ}
    response = requests.post(url, json=payload)


def fill(TOKEN,CHAT_ID,mesage):
    TOKEN = TOKEN
    CHAT_ID = CHAT_ID
    MESAJ = mesage
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": MESAJ}
    response = requests.post(url, json=payload)
    

