from array import array
import string


#arreglo =  input("ingrese un arreglo de N enteros: ")
iteraciones = int (input("ingrese el número de iteraciones: "))
arreglo =  []

def solution (A , k):
    
    longitud = len(A)
    if longitud>0:
        for b in range (0, k):
            temporal=(A[longitud-1])
            for a in range(0,longitud-1):
                #print ('temporal: '+ temporal)
                A[longitud-1-a]= A[longitud-a-2]
                #print("la posicion es :" + str(longitud-1-a))
                if (longitud-2-a==0):
                    A[0]=temporal
            #print ("el arreglo despues de esta iteración es: "+ str(arreglo2))
    return A

print ("la cadena resultante es: "+ str (solution (arreglo, 3)))