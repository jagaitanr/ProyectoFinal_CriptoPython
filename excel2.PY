from ast import Return


columnaletras = input("ingrese la columna en letras mayusculas: ")
#if (columna>456976):
# print ("ingrese un numero menor a 456976")  
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#j=0

def verificacion(valoraVerificar): #verifica que hayan solo letras mayusculas
    verificacion = False
    
    for revision in columnaletras:
        for j in range (0,25):
            if revision==abecedario[j]:
                verificacion=True
            #l=l+1    
    if (verificacion):
        print ("la columna es  la número: " + str(valoraVerificar))
    else:
        print("debe ingresar solo letras mayusculas de la A a la Z")
    return   


def conversion():
    i=0
    valor = 0
    longitud = len(columnaletras)
    while (longitud>0):
        caracter=columnaletras[longitud-1] 
        #j=j+1
        k=1 #enumerar del 1 al 26 el abecedario para sumarlo después de elevarlo por i
        for caracter2 in abecedario:
            if (caracter == caracter2):
                valor=valor + (26**i)*k
        k=k+1
        i=i+1 #elevar a la potencia
        longitud=longitud-1
    return valor
       
    
valor1 = conversion ()
verificacion(valor1)
