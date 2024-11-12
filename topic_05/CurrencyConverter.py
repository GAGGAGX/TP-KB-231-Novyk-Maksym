import requests

listChoice = ['EUR', 'USD', 'PLN']

def inp():
    while True:
        per = input("EUR, USD, PLN or exit(EX)\nEnter your choice: ").upper()
        if per == "EX":
            exit(0)
        if per in listChoice:
            try:
                value = float(input("Enter amount: "))
                break
            except ValueError:
                print("It's not a number.\n")
        else:
            print("Selection error.\n")
    return per, value

def curr():
    r = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    for elem in r.json():
        match elem['cc']:
            case "EUR":
                rateEUR = elem['rate']
            case "USD":
                rateUSD = elem['rate']
            case "PLN":
                ratePLN = elem['rate']
    return rateEUR, rateUSD, ratePLN

def con(rateEUR, rateUSD, ratePLN, per, value):
    match per:
        case "EUR":
            print(f"Result of {value} in EUR to UAH = {rateEUR*value}")
        case "USD":
            print(f"Result of {value} in USD to UAH = {rateUSD*value}")
        case "PLN":
            print(f"Result of {value} in PLN to UAH = {ratePLN*value}")



r1, r2, r3 = curr()
while True:
    per, val = inp()
    con(r1, r2, r3, per, val)