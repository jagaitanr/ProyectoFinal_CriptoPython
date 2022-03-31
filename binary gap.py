entrada = int (input("ingrese un número entre 1 y 147.483.647: "))
"""
def convBinario (entrada):
    arreglo=''
    arreglo2=''
    cociente=int (entrada/2)
    
    while (cociente>0):
        cociente=int(entrada/2)
        residuo=int(entrada%2)
        arreglo=arreglo+str(residuo)
        entrada=cociente
    long=len(arreglo)
    for a in range(0,long):
        arreglo2=arreglo2+arreglo[long-1-a]
    return arreglo2

def contandoCeros(arregloaContar):
    long=len(arregloaContar)
    numerodeceros=0
    numerodecerosMayor=0
    for b in range(0,long-1):
        if (arregloaContar[b]=="0" and arregloaContar[b+1]=="0"):
            numerodeceros=numerodeceros+1
        elif (arregloaContar[b]=="0" and arregloaContar[b+1]=="1" and numerodeceros!=0):
            if (numerodecerosMayor<=numerodeceros):
                numerodecerosMayor=numerodeceros+1
                numerodeceros=0
    return (numerodecerosMayor)
#print ("el número en binario es:  " + (entrada))

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# write your code in Python 3.6

#entrada = int (input("ingrese un número entre 1 y 147.483.    647: "))

"""
def contandoCeros(arregloaContar):
    print (arregloaContar)
    long=len(arregloaContar)
    numerodeceros=0
    numerodecerosMayor=0
    for b in range(0,long-1):
        print (str(numerodeceros))
        if (arregloaContar[b]=="0"):
            numerodeceros=numerodeceros+1
            if (arregloaContar[b+1]=="1"):
                if (numerodecerosMayor<=numerodeceros):
                    numerodecerosMayor=numerodeceros
                numerodeceros=0
    
    return (numerodecerosMayor)
    

def solution (N):
    arreglo=''
    arreglo2=''
    cociente=int (N/2)
    entrada=N
    
    while (cociente>0):
        cociente=int(entrada/2)
        residuo=int(entrada%2)
        arreglo=arreglo+str(residuo)
        entrada = cociente
    long=len(arreglo)
    for a in range(0,long):
        arreglo2=arreglo2+arreglo[long-1-a]
    #print(arreglo2)
    arreglo = contandoCeros(arreglo2)
    return arreglo


#print ("el número en binario es:  " + solution(entrada))
#print ("secuencia más larga de ceros: "+ str(contandoCeros(solution(entrada))))

print ("secuencia más larga de ceros: "+ str(solution(entrada)))
