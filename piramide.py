base = int (input("ingrese la base de la pirámide: "))
for  i in range (base):
    
    for j in range (i, base):
        if (j==base-1) :
            for k in range (i+1):
                print ("█ ", end='')
            if (k==i):
                print('')    
        else:
            print (" ",end='')
