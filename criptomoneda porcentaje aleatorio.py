import random

criptomoneda = input("ingrese el nombre de la criptomoneda: ")
monto = int (input("ingrese el valor en USD de la criptomoneda: "))

def aleatorio ():
    a = random.randrange(0,60,1)
    if (a<30):
            a=a/10*-1
    else:
            a=(a-30)/10
    return (a/100)
        

for j in range (1,8,1):

      
        if (j==1):
            a = aleatorio()
            montodia1=monto + monto*a
            print ("el porcentaje del lunes fue de :" + str(a) + " ,la utilidad fue de " + str(monto*a) + " el valor de cierre de la criptomoneda es de : " + str(montodia1)) 
        if (j==2):
            a = aleatorio()
            montodia2=montodia1 + montodia1*a
            print ("el porcentaje del martes fue de :" + str(a) + " ,la utilidad fue de " + str(montodia1*a) + " el valor de cierre de la criptomoneda es de : " + str(montodia2)) 
        if (j==3):
            a = aleatorio()
            montodia3=montodia2 + montodia2*a
            print ("el porcentaje del miércoles fue de :" + str(a) + " ,la utilidad fue de " + str(montodia2*a) + " el valor de cierre de la criptomoneda es de : " + str(montodia3)) 
        if (j==4):
            a = aleatorio()
            montodia4=montodia3 + montodia3*a
            print ("el porcentaje del jueves fue de :" + str(a) + " ,la utilidad fue de " + str(montodia3*a) + " el valor de cierre de la criptomoneda es de : " + str(montodia4)) 
        if (j==5):
            a = aleatorio()
            montodia5=montodia4 + montodia4*a
            print ("el porcentaje del viernes fue de :" + str(a) + " ,la utilidad fue de " + str(montodia4*a) + " el valor de cierre de la criptomoneda es de : " + str(montodia5)) 
        if (j==6):
            a = aleatorio()
            montodia6=montodia5 + montodia5*a
            print ("el porcentaje del sabado fue de :" + str(a) + " ,la utilidad fue de " + str(montodia5*a) + " el valor de cierre de la criptomoneda es de : " + str(montodia6)) 
        if (j==7):
            a = aleatorio()
            montodia7=montodia6 + montodia6*a
            print ("el porcentaje del domingo fue de :" + str(a) + " ,la utilidad fue de " + str(montodia6*a) + " el valor de cierre de la criptomoneda es de : " + str(montodia7)) 
        
print (" la ganancia total fue de:$ " + str(montodia7-monto))