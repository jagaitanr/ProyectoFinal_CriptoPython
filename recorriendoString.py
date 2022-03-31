cadena = input ("ingrese una cadena de carácteres: ")
caracter = input ("ingrese el carácter a ser contado: ")
cantidad = 0
for x in cadena:
    if (x==caracter):
        cantidad = cantidad+1
if (cantidad>0):
    print ("la letra '"+ caracter + "' se repite "+str(cantidad)+ " veces")        
else:
    print("la letra "+ caracter + " no se encuentra en la cadena escrita")