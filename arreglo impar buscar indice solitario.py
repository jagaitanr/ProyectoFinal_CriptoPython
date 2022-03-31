def solution (A):
    longitud = len(A)
    impar = True
    while impar :
        #print ("longitud: "+str(longitud)) 
        longitud = len(A)
        comparar=A[0]
        for a in range (1,longitud):
            #print ("comparar: "+str (comparar))
            #print ("A["+ str(a) +"]: " +str (A[a]))
            if (comparar==A[a]):
                del A[a]
                del A[0]
                longitud = longitud-2
                break
            if a == longitud-1:
                impar = False
            
        #print("el arreglo quedo "+ str(A))
        if longitud == 1:
            comparar=A[0]
            impar = False

    return comparar

print ("el valor impar es: "+ str(solution([9,3,9,3,9,7,9])))
