def solution (A):
    long=len(A)
    f=[] # creación de una lista
    for a in range (0, long-1):
        c = 0
        d = 0
        for b in range (0, a+1):
            c=c + A[b]
            print ("c: " + str (c))
        for b in range (a+1, long):    
            d=d + A[b]
            
            print ("d: "+ str (d)) 
        e=abs(d-c)

        f.append(e) #agregamos el valor de la diferencia en la ultima posicion de la lista
        g = min (f)
        if d == 0:
                break
    return (g)
solution ([6, 8, 4, 2, 3, 1, 9, 5])