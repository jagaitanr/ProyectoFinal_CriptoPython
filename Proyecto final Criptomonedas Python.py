import requests
import os
import json
import pprint
import ast #biblioteca para poder convertir string en diccionario
import pickle

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

def extraerIdentificador (nombreCripto): #extraer el ID para conocer precio de la moneda
    for i in range (0, len(monedas_list)):
        if nombreCripto==monedas_list[i] :
            id = i
            #print (id)
            break
    return id #id de la moneda

def validacionCriptoFondo(nombreCripto, valorEnviar):
    fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","r")
    monedas2=eval(fileW.read())
    fileW.close()
    monedaExistente=False # es True hasta que la moneda esté en la base de datos de coinmarket
    monedaPresente=False # hasta que no se demuestre que pertenece a la lista
    saldoSuficiente=False # hasta que se verifique que tiene suficiente saldo
    for i in range (len(monedas2)):
        if monedas2[i]['symbol']==nombreCripto:
            monedaPresente=True
            if monedas2[i]['cantidad']>=valorEnviar:
                saldoSuficiente=True
    return ([monedaPresente, saldoSuficiente]) #retorna arreglo verdadero o Falso tanto en  la moneda como en el saldo


    

def escribirArchivo(nombre, cantidad, codigo):
    monedas = jsonCoinMarket['data']
    monedas2=[]
    print("El precio de " + nombre +" es: ")
    id=extraerIdentificador(nombre)

    print(monedas[id]['quote']['USD']['price'])
    try:
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","r")
        monedas2=eval(fileW.read())
        #monedas2=fileW.read()
        fileW.close()
        print("en el try")
    except: #si el archivo no se puede abrir es porque no ha sido creado, entonces se procede a crear e inicializar una lista de monedas
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","w")
        primerDiccionario={'symbol':nombre,'cantidad':0,'codigo':codigo}
        monedas2.append(primerDiccionario)
        fileW.write(str(monedas2))
        fileW.close()
        print("en el except")
    monedaPresente=False # inicializa variable para agregarla o para sumar su saldo
    for i in range (0, len(monedas2)):
        print("monedas2:")
        print (monedas2[i])
        
        if monedas2[i]['symbol']==nombre:
                print ("la criptonomeda ya esta")
                posicion = i
                monedaPresente=True
    if (monedaPresente):
        monedas2[posicion]['cantidad']=monedas2[posicion]['cantidad']+cantidad
        print("nuevo valor: "+ str(monedas2[posicion]['cantidad']))
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","w")
        fileW.write(str(monedas2))
        fileW.close()
        
    else:    
        diccionarioaAñadir={'symbol':nombre,'cantidad':cantidad,'codigo':codigo}
        #print(diccionarioaAñadir)
        monedas2.append(diccionarioaAñadir)
        posicion=len(monedas2)-1 # esta sería la posición en la última lista del arreglo
        #print ("monedas2 actualizado:")
        #print(monedas2)
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","w")
        fileW.write(str(monedas2))
        fileW.close()


    #file.write(str(monedas[1]['quote']['USD']['price']))
    #print(monedas['quotes']['USD']['price'])
    return (monedas2[posicion]['cantidad'])


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
                nuevoValor=escribirArchivo(nombreCripto, cantidadRecibida, codigoRemitente)
                print("su saldo de "+ nombreCripto + " es de: " + str(nuevoValor))
                validacicionCodigo=True
                break

if opcion == "2":

    criptomonedaExiste = False
    while criptomonedaExiste == False:
        nombreCripto = input ("ingrese nombre de la criptomoneda a enviar o escriba 'salir' para abandonar la billetera : ")
        if nombreCripto in monedas_list:
            criptomonedaExiste = True
            validacion=validacionCriptoFondo(nombreCripto, 0)
            if validacion[0]==False:
                print ("ésta moneda no hace parte de su billetera,  inténtelo de nuevo")
                criptomonedaExiste = False #para que vuelva a hacer la validación
                
        elif nombreCripto == "salir":
            opcion=6
            break
        else:
            print("esta moneda no existe,  intentelo de nuevo o digite salir")
        
    if nombreCripto!= "salir":     
        valorValido = False   
        while valorValido == False:
            try: 
                cantidadEnviar=float(input ("ingrese la cantidad a enviar de " + nombreCripto + ": "))
                if cantidadEnviar<=0:
                    print ("el valor debe ser mayor a cero")
                else:
                    valorValido = True
                    validacion=validacionCriptoFondo(nombreCripto, cantidadEnviar)
                    if validacion[1]==False:
                        print("no tiene la cantidad suficiente de "+nombreCripto)
                        valorValido = False
                    
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
                cantidadEnviar=-1*(cantidadEnviar) #para que la cantidad sea reastada usando  el mismo método
                nuevoValor=escribirArchivo(nombreCripto, cantidadEnviar, codigoRemitente)
                print("su saldo de "+ nombreCripto + " es de: " + str(nuevoValor))
                validacicionCodigo=True
                break



if opcion == "3":
    criptomonedaExiste = False
    while criptomonedaExiste == False:
        nombreCripto = input ("ingrese símbolo de la criptomoneda para mostrar su balance o 'salir' para abandonar la billetera : ")
        if nombreCripto in monedas_list:
            criptomonedaExiste = True
            validacion=validacionCriptoFondo(nombreCripto, 0)
            if validacion[0]==False:
                print ("ésta moneda no hace parte de su billetera,  inténtelo de nuevo")
                criptomonedaExiste = False #para que vuelva a hacer la validación
            else:
                id=extraerIdentificador(nombreCripto)
                monedas = jsonCoinMarket['data']
                print ("el nombre de la criptomoneda es: "+ monedas[id]['name'] )
                fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","r")
                monedas2=eval(fileW.read())
                fileW.close()
                for i in range (0, len(monedas2)):
                    if monedas2[i]['symbol']==nombreCripto:
                        id2=i
                print ("la cantidad de " + monedas[id]['name'] + " que posee en su billetera es: "+str(monedas2[id2]['cantidad']))
                print ("el precio en USD de " + monedas[id]['name']+" es de "+ str(monedas[id]['quote']['USD']['price']) + " para un total en USD de " + str(monedas[id]['quote']['USD']['price']*monedas2[id2]['cantidad']) )

        elif nombreCripto == "salir":
            opcion=6
            break
        else:
            print("esta moneda no existe,  intentelo de nuevo o digite salir")
else:
    pass    

