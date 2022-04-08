import requests
import os
import json
import pprint
import ast #biblioteca para poder convertir string en diccionario

def reescribirArchivo():
    file = open("I:/NEXTU/PYTHON/billetera.txt","r")
    print("se creo el archivo")
    fileString= str(file.read())
    #file.write("Primera línea" + os.linesep)
    #file.write("Segunda línea")
    print ("el contenido del archivo es: " + fileString)
    fileLista=eval(fileString)
    print(fileLista[1])
    return

COINMARKET_API_KEY = "91392076-e2b2-409b-814e-8302fee335f1"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}
parametros = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
}
_url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
jsonCoinMarket=requests.get(_url, params=parametros, headers=headers, ).json()
monedas_list=[]
for cripto in jsonCoinMarket["data"]:
    monedas_list.append(cripto["symbol"])
print (monedas_list)

"""def esmoneda(cripto):
    return cripto in monedas"""
"""def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))
"""

class Criptomoneda(object):
    def __init__(self, nombre,  saldo, cotizacion):
        self.nombre = nombre
        self.saldo = saldo
        self.cotizacion = cotizacion
    
    def indicarNombre(self, nombre):
        self.nombre=nombre
    
    def indicarCotizacion(self, cotizacion):
        self.cotizacion=cotizacion
    
    def indicarSaldo(self, saldo):  
        self.saldo=saldo
    
    def mostrarNombre(self):
        return self.nombre
    
    def imostrarCotizacion(self): 
        return self.cotizacion
    
    def mostrarSaldo(self):  
        return  self.saldo
    
    def calcularSaldo(self, moneda):  
        if moneda== "USD":
            return self.saldo*self.cotizacion
        else:
            return self.saldo

def escribirArchivo(nombre, cantidad, codigo):
    monedas = jsonCoinMarket['data']
    print("El precio de " + nombre +" es: ")
    print(monedas[1]['quote']['USD']['price'])
    try:
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","r")
        fileW.close()
    except: #si el archivo no se puede abrir es porque no ha sido creado, entonces se procede a crear e inicializar una lista de monedas
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","w")
        fileW.write("{'symbol':'"+nombre+"','cantidad':0,'codigo':'NULL'}")
        fileW.close()
    fileString=open("I:/NEXTU/PYTHON/inventarioMonedas.txt",'r')
    lista=fileString.read()
    lista2=lista.split()
    for i in lista2:
        print(i)
    fileString.close()
    
    a=len(lista2)
    print (str(a))

    for linea in range (0, a):
        lista2[linea]=ast.literal_eval(lista2[linea])
        if lista2[0]["symbol"]==nombre:
            print ("la criptonomeda ya esta")
        else:
            lista2.append('{"symbol":'+nombre+', "cantidad": '+str(cantidad)+ ', "codigo": '+ codigo+'}')
            fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","w")
            fileW.write(str(lista2))
            fileW.close()
    #file.write(str(monedas[1]['quote']['USD']['price']))
    #print(monedas['quotes']['USD']['price'])
    return


print ("Billetera de Criptomonedas tipo DESKTOP \n Menú:")
print ("1. Recibir cantidad")
print ("2. transferir monto")
print ("3. Mostrar balance de una moneda")
print ("4. Mostrar balance general")
print ("5. Mostrar histórico de transacciones")
print ("6. Salir del programa")
#reescribirArchivo()
opcion = input ("ingrese opción: ")

if opcion == "1":
    criptomonedaExiste = False
    while criptomonedaExiste == False:
        nombreCripto = input ("ingrese nombre de la criptomoneda: ")
        if nombreCripto in monedas_list:
            criptomonedaExiste = True
        elif nombreCripto == "salir":
            opcion=6
            break
        else:
            print("esta moneda no existe,  intentelo de nuevo o digite salir")
        
    if nombreCripto!= "salir":     
        valorValido = False   
        while valorValido == False:
            try: 
                cantidadRecibida=float(input ("ingrese la cantidad a recibir de " + nombreCripto + ": "))
                if cantidadRecibida<=0:
                    print ("el valor debe ser mayor a cero")
                else:
                    valorValido = True
            
            except: print ("El valor debe ser un número" )
        validacionCodigo = False
        while validacionCodigo == False:  
            codigoRemitente = input ("ingrese el código del remitente: ")
            print (COINMARKET_API_KEY)
            if codigoRemitente == "salir":
                validacicionCodigo = True # para poder salir del while
                break # sale del while
            elif codigoRemitente == COINMARKET_API_KEY:
                print ("el código del remitente NO puede ser igual al código del destinatario,  verifique por favor,  o digite salir")
            else :
                escribirArchivo(nombreCripto, cantidadRecibida, codigoRemitente)
                validacicionCodigo=True

if opcion == "2":
    nombreCripto = input ("ingrese nombre de la criptomoneda a enviar: ")
    cantidadEnviar = input ("ingrese el monto a enviar: ")
    codigoDestinatario = input ("ingrese el código del destinatario: ")

if opcion == "3":
    nombreCripto = input ("ingrese nombre de la criptomoneda para mostrar su balance: ")

else:
    pass    

