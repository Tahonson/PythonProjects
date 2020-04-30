
import http.cookiejar
import requests
import json
from bs4 import BeautifulSoup as BS

KeysOfPlays = []
ValueOfResaults = []
SumBet = 0
Link = ""
Bets = []

####### cookie
cookie = {
    "__cfduid": "d05215d9087bd1c4bedc6c712fd423c8a1585849850",
    "express.sid": "s%3Ar0yi7P4wIkj1jdkO_zexh1fIjlKMnI6x.6JPXTM10YeiZHbOVOM%2BmlXvDeAO3Ebh1S8Ya3WY%2BiCM",
    "_ga": "GA1.2.510722999.1585849893"
}
####### cookie
response = requests.get('https://csgo500.com/crash/history/before/', cookies=cookie)
JsonHistory = json.loads(response.text)

for element in JsonHistory:
    KeysOfPlays.append(element["roundId"])
    Data = element["endDate"]
    # нужна проверка наличия  в базе (также подключить mysql ,  к примеру. чтобы вести записи, но пока просто на вывод).
    Link = 'https://csgo500.com/crash/history/single/' + str(element["roundId"])
    ResponseBet = requests.get(Link, cookies=cookie)
    JsonBets = json.loads(ResponseBet.text)
    print(JsonBets)
    #Если посмотреть данные ссылки типа
    # 'https://csgo500.com/crash/history/single/' + str(element["roundId"])
    # можно заметить, что внутри json имеется некий массив "bets". Однако в python он не виден.
    for BetTime in JsonBets:
        RoundID = BetTime['roundId']
        CrashValue = BetTime['crashValue']
        Bets = BetTime['bets']

        for Bet in Bets:
             SumBet = SumBet + Bet['profit']

    #print(Data)
    #print(CrashValue)
    #print(SumBet)

# ResponseBet = requests.get('https://csgo500.com/crash/history/single/')
# JsonBets = json.loads(ResponseBet.text)
# for BetEl in JsonBets:
#     RoundID = BetEl['roundId']
#     BetUsers = BetEl['bets']
#     for BetUser in BetUsers:
#         Profit = BetUser['profit']


#soup = BS(r.content, 'html.parser')
#content = soup.find('div', class_='highlight if-highlighted-green')
#print(content)



