import requests
import os
import json
import pprint
import ast #biblioteca para poder convertir string en diccionario
import pickle
from tabulate import tabulate 


    
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
#print (jsonCoinMarket["data"])
monedas_list=[]
for cripto in jsonCoinMarket["data"]:
    monedas_list.append(cripto["symbol"])
#print (monedas_list)


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

def validacionCriptoFondo(nombreCripto, valorEnviar): # recibe el symbol de la criptomoneda y valor a enviar para revisar tanto la existencia en la billetera como los fondos suficientes
    try:
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","r")
        monedas2=eval(fileW.read())
        fileW.close()
        #monedaExistente=False # es True hasta que la moneda esté en la base de datos de coinmarket
        monedaPresente=False # hasta que no se demuestre que pertenece a la lista
        saldoSuficiente=False # hasta que se verifique que tiene suficiente saldo
        for i in range (len(monedas2)):
            if monedas2[i]['symbol']==nombreCripto:
                monedaPresente=True
                if monedas2[i]['cantidad']>=valorEnviar:
                    saldoSuficiente=True
    except:
        print("No existe el archivo,  revise la existencia del mismo o verifique que ya tenga Criptomonedas para poder enviar")
        return([False, False])
    return ([monedaPresente, saldoSuficiente]) #retorna arreglo verdadero o Falso tanto en  la moneda como en el saldo


    

def escribirArchivo(nombre, cantidad, codigo): # en esta función se reescribe el archivo
    monedas = jsonCoinMarket['data']
    monedas2=[]
    print("\nEl precio de " + nombre +" es: ")
    id=extraerIdentificador(nombre)
    print(monedas[id]['quote']['USD']['price'])
    try:
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","r")
        monedas2=eval(fileW.read())
        fileW.close()

        
    except: #si el archivo no se puede abrir es porque no ha sido creado, entonces se procede a crear e inicializar una lista de monedas
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","w")
        primerDiccionario={'symbol':nombre,'cantidad':0,'codigo':codigo}
        monedas2.append(primerDiccionario)
        fileW.write(str(monedas2))
        fileW.close()
        #print("en el except")

    monedaPresente=False # inicializa variable para agregarla o para sumar su saldo
    for i in range (0, len(monedas2)):
        if monedas2[i]['symbol']==nombre:
                #print ("la criptonomeda ya esta")
                posicion = i
                monedaPresente=True
    if (monedaPresente):
        id=extraerIdentificador(nombre) # traer el ID del data de coinmarket
        fecha=monedas[id]['quote']['USD']['last_updated']
        valor=monedas[id]['quote']['USD']['price']
        if (cantidad>=0):
            transaccion='recibido'
            monto=cantidad*valor
        else:
            transaccion='enviado'
            monto=-cantidad*valor # como la cantidad viene negativa se debe dejar positiva para el monto
        
        agregarTransaccion(fecha, nombre, transaccion, codigo,  cantidad, monto )
        monedas2[posicion]['cantidad']=monedas2[posicion]['cantidad']+cantidad
        #print("nuevo valor: "+ str(monedas2[posicion]['cantidad']))
        fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","w")
        fileW.write(str(monedas2))
        fileW.close()
        
    else:
        id=extraerIdentificador(nombre) # traer el ID del data de coinmarket
        fecha=monedas[id]['quote']['USD']['last_updated']
        valor=monedas[id]['quote']['USD']['price']
        if (cantidad>=0):
            transaccion='recibido'
            monto=round(cantidad*valor,2)
        else:
            transaccion='enviado'
            monto=round(-cantidad*valor,2) # como la cantidad viene negativa se debe dejar positiva para el monto
        
        agregarTransaccion(fecha, nombre, transaccion, codigo,  cantidad, monto ) # esta función envía la información para guardarla en el respectivo archivo
        
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

def agregarTransaccion(fecha,symbol, tipoTransaccion, codigo,  cantidad, monto): #función para agregar la transacción
    try: 
        transacciones=[]
        fileW2=open("I:/NEXTU/PYTHON/historicoTransacciones.txt","r")
        transacciones=eval(fileW2.read())
        #print(transacciones)
        fileW2.close()
        diccionarioaAñadir2={'Fecha y hora':fecha,'Symbol':symbol,  'Tipo': tipoTransaccion, 'codigo (API-key)': codigo, 'cantidad':cantidad, 'valor en ese momento':monto}
        transacciones.append(diccionarioaAñadir2)
        fileW2=open("I:/NEXTU/PYTHON/historicoTransacciones.txt","w")
        fileW2.write(str(transacciones))
        fileW2.close()
        
        
    except: #si el archivo aun no existe se debe crear
        fileW2=open("I:/NEXTU/PYTHON/historicoTransacciones.txt","w")
        primerDiccionario2={'Fecha y hora ':fecha,'Symbol':symbol,  'Tipo': tipoTransaccion, 'codigo (API-key)': codigo, 'cantidad':cantidad, 'valor en ese momento':monto}
        transacciones=[]
        transacciones.append(primerDiccionario2)
        fileW2.write(str(transacciones))
        fileW2.close()
        #print("en el except")
    return

def menú ():
    while (True):
        print ("\n************-----------------***************")
        print ("Billetera de Criptomonedas tipo DESKTOP \n Menú:")
        print ("1. Recibir cantidad")
        print ("2. transferir monto")
        print ("3. Mostrar balance de una moneda")
        print ("4. Mostrar balance general")
        print ("5. Mostrar histórico de transacciones")
        print ("6. Salir del programa")

        opcion = input ("ingrese opción: ")
        salir = menu2(opcion)
        if salir == 'salir':
            print ('cerrando Billetera \n ¡gracias!')
            break
    return

def menu2(opcion):
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
                #print (COINMARKET_API_KEY)
                if codigoRemitente == "salir":
                    #validacicionCodigo = True # para poder salir del while
                    break # sale del while
                elif codigoRemitente == COINMARKET_API_KEY:
                    print ("el código del remitente NO puede ser igual al código del destinatario,  verifique por favor,  o digite salir")
                else :
                    nuevoValor=escribirArchivo(nombreCripto, cantidadRecibida, codigoRemitente)
                    print("su saldo de "+ nombreCripto + " es de: " + str(nuevoValor))
                    validacicionCodigo=True
                    break
        return ('no salir')

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
                codigoRemitente = input ("ingrese el código del destinatario: ")
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
        return ('no salir')


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
                    print ("\nEl nombre de la criptomoneda es: "+ monedas[id]['name'] )
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
        return ('no salir')

    if opcion=="4":
        monedas3=[]
        temp={}
        try:
            fileW=open("I:/NEXTU/PYTHON/inventarioMonedas.txt","r")
            monedas2=eval(fileW.read())
            fileW.close()
            monedas3=monedas2.copy()
            for i in range (0, len(monedas3)):
                monedas = jsonCoinMarket['data']
                id=extraerIdentificador(monedas3[i]['symbol'])
                monedas3[i]['valor']=str(round((monedas[id]['quote']['USD']['price']*monedas3[i]['cantidad']),2)) #agrega un nuevo key/valor a cada diccionario del arreglo monedas3
                monedas3[i]['nombre']=monedas[id]['name']
            print ("***Balance General de Criptomonedas***")
            print(tabulate(monedas3, headers='keys'))
            totalUSD=0
            for list in monedas3:
                totalUSD=totalUSD+float(list['valor'])
            print ("saldo total: "+ str(round(totalUSD,2)) + " USD")        
        except:
            print("error al abrir el archivo, puede que lo hayan  borrado o que aún no se haya creado, tiene que recibir una moneda para crear el archivo")
        return ('no salir')

    if opcion=='5':
        try:
            fileW2=open("I:/NEXTU/PYTHON/historicoTransacciones.txt","r")
            transacciones=eval(fileW2.read())
            fileW2.close()
            print(tabulate(transacciones, 'keys'))

        except:
            print("el archivo no ha sido creado, debe realizar mínimo una transacción")
        return ('no salir')

    else:
        pass
    if opcion =='6':
        return ('salir')
menú() #rutina principal
