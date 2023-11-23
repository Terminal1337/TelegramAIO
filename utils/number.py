import httpx,requests
import json

with open('./config.json') as f:
    settings = json.load(f)
    f.close()
if settings['5sim']['active']:
    api_name = '5sim'
    key = settings['5sim']['key']
elif settings['sms-activate']['active']:
    api_name= "sms-activate"
def getBalance():
    # print(api_name)
    if api_name == "5sim":
        headers = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',}
        balance = requests.get('https://5sim.net/v1/user/profile', headers=headers).json()
        # print(balance)
        return balance
def getNumber():
    if api_name == "5sim":
        headers = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',}
        
        ph = requests.get(f"https://5sim.net/v1/user/buy/activation/{settings['5sim']['country']}/{settings['5sim']['provider']}/telegram", headers=headers)
        if "no free phones" in ph.text:
            print(ph.text)
            return False
        else:
            return ph.json()
def getCode(id):
    if api_name == "5sim":
        headers = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',}
        
        check = requests.get(f"https://5sim.net/v1/user/check/"+str(id), headers=headers).json()
        # print(check)
        return check

def Cancel(id):
    if api_name == "5sim":
        headers = {
        'Authorization': 'Bearer ' + key,
        'Accept': 'application/json',}
        
        cancelled = requests.get('https://5sim.net/v1/user/cancel/' + str(id), headers=headers).json()
        if cancelled['status'] != "CANCELED":
            return False
        else:
            return True
