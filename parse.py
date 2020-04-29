

import requests
import json
from bs4 import BeautifulSoup as BS

KeysOfPlays = []
ValueOfResaults = []
SumBet = 0
Link = ""
Bets = []
response = requests.get('https://csgo500.com/crash/history/before/')
JsonHistory = json.loads(response.text)

for element in JsonHistory:
    KeysOfPlays.append(element["roundId"])
    Data = element["endDate"]
    # нужна проверка наличия  в базе (также подключить mysql ,  к примеру. чтобы вести записи, но пока просто на вывод).
    Link = 'https://csgo500.com/crash/history/single/' + str(element["roundId"])
    ResponseBet = requests.get(Link)
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



