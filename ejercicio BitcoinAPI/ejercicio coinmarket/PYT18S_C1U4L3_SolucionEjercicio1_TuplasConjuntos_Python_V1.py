import requests

def esmoneda(cripto):
    return cripto in monedas

monedas_list=[]
COINMARKET_API_KEY = "2448e9c9-b938-4f0e-85f1-9878a7b41c87"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
#data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",headers=headers).json()
print (data)
for cripto in data["data"]:
    monedas_list.append(cripto["symbol"])

monedas=tuple(monedas_list)

moneda=input("Indique el nombre de la moneda a verificar: ")
while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda,",moneda,"es valida porque existe en coimnmarketcap.com")
