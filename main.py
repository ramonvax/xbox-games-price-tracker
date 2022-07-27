from bs4 import BeautifulSoup
import requests
import json

def linhas():
    print(81*"-")


games_link = {
    "Mafia 3": "https://www.xbox.com/pt-BR/games/store/mafia-iii-definitive-edition/BVZLS7XZ68KF/0001",
    "Mafia Trilogy": "https://www.xbox.com/pt-br/games/store/mafia-trilogy/9NKG0X1MGQTX",    
    "The Witcher 2": "https://www.xbox.com/pt-BR/games/store/the-witcher-2/BTGZWQCD01JC/0001",
    "Cyberpunk 2077": "https://www.xbox.com/pt-BR/games/store/cyberpunk-2077/BX3M8L83BBRW/0001",
    "Elder Ring": "https://www.xbox.com/pt-BR/games/store/elden-ring/9P3J32CTXLRZ/0010",
    "Diablo 2": "https://www.xbox.com/pt-BR/games/store/diablo-prime-evil-collection/9N9LJ3N3TRZX/0010",
    "Dying Light Definitive Edition": "https://www.xbox.com/pt-BR/games/store/dying-light-definitive-edition/9N06V8XJ5G7L/0010",
    "Far Cry Primal":  "https://www.xbox.com/pt-BR/games/store/far-cry-primal-apex-edition/BZGBDSSP6G2J/0001",    
    "Red Dead Redemption 2": "https://www.xbox.com/pt-BR/games/store/red-dead-redemption-2/9N2ZDN7NWQKV/0010",
    "Red Dead Redemption 2 DEFINITIVE": "https://www.xbox.com/pt-br/games/store/red-dead-redemption-2-edicao-definitiva/9ph339l3z99c",    
    "Watch Dogs Legion": "https://www.xbox.com/pt-BR/games/store/watch-dogs-legion/C1WRX8ZD77M9/0001",
    "Watch Dogs Legion GOLD": "https://www.xbox.com/pt-BR/games/store/watch-dogs-legion-gold-edition/9N5V65564VWJ/0010",
    "Commandos 2 - HD Remaster": "https://www.xbox.com/pt-br/games/store/commandos-2-hd-remaster/9p1rhdkbn6qc"
}

try:
    with open("price.json", "r") as file:
        file = file.read()
        price = json.loads(file)
except:
    with open("price.json", "w") as file:
        price = {}
        for _ in games_link:            
            price[_] = 0.0
        file.write(json.dumps(price))


for game in games_link:
    page = requests.get(games_link[game])
    soup = BeautifulSoup(page.content, 'html.parser')
    value = soup.find_all(
        class_="Price-module__boldText___34T2w Price-module__moreText___1FNlT Price-module__listedDiscountPrice___2vqMe")
    if len(value) <= 0:
        value = soup.find_all(
        class_="Price-module__srOnly___2mBg_")
    value_str = str(value)
    value_clear = (
        (value_str.split(">")[-2]).split("<")[-2]).replace(",", ".")
    if value_clear[len(value_clear)-1] == "+":
        value_clear = value_clear.replace("+", "")
    linhas()
    print(f"O jogo {game} esta de {value_clear}")
    print(games_link[game])
    if game not in price.keys():
        price[game] = 0.0
    if price[game] == 0.0:            
        price[game] = value_clear    
    print(f"Menor valor ja registrado foi de R${price[game]}")


with open("price.json", "w") as file:
    file.write(json.dumps(price))

linhas()
print("|"+32*"-"+"FIM DO PROGRAMA"+32*"-"+"|")
linhas()
