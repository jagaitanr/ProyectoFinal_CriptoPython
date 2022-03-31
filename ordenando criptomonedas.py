from ctypes.wintypes import INT


CRIPTO1= input ("ingrese el nombre de la criptomoneda 1: ")
VALORCRIPTO1 = int (input ("Ingrese el monto en USD de " + CRIPTO1+": "))
CRIPTO2= input ("ingrese el nombre de la criptomoneda 2: ")
VALORCRIPTO2 = int (input ("Ingrese el monto en USD de " + CRIPTO2+": "))
CRIPTO3= input ("ingrese el nombre de la criptomoneda 3: ")
VALORCRIPTO3 = int (input ("Ingrese el monto en USD de " + CRIPTO3+": "))

primero = ""
segundo = ""
tercero = ""

if VALORCRIPTO1>=VALORCRIPTO2:
    if VALORCRIPTO1>=VALORCRIPTO3:
        primero = CRIPTO1 +": "+ str(VALORCRIPTO1)
        if VALORCRIPTO2 >= VALORCRIPTO3:
            segundo = CRIPTO2 +": "+ str(VALORCRIPTO2)
            tercero = CRIPTO3 +": "+ str(VALORCRIPTO3)
        else:
            tercero = CRIPTO2  +": "+ str(VALORCRIPTO2)
            segundo = CRIPTO3 +": "+ str(VALORCRIPTO3)
            
    else:
        primero = CRIPTO3 +": "+ str(VALORCRIPTO3)
        segundo = CRIPTO1 +": "+ str(VALORCRIPTO1)
        tercero = CRIPTO2 +": "+ str(VALORCRIPTO2)
elif VALORCRIPTO2>=VALORCRIPTO3:
        primero = CRIPTO2 +": "+ str(VALORCRIPTO2)
        if VALORCRIPTO1 >= VALORCRIPTO3:
            segundo = CRIPTO1 +": "+ str(VALORCRIPTO1)
            tercero = CRIPTO3 +": "+ str(VALORCRIPTO3)
        else:
            tercero = CRIPTO1  +": "+ str(VALORCRIPTO1)
            segundo = CRIPTO3 +": "+ str(VALORCRIPTO3)
        
else:
        primero = CRIPTO3 +": "+ str(VALORCRIPTO3)
        segundo = CRIPTO2 +": "+ str(VALORCRIPTO2) 
        tercero = CRIPTO1 +": "+ str(VALORCRIPTO1)
print (primero)
print (segundo)
print (tercero)

    


