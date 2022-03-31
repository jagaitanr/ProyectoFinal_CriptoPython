#import string


columna = int(input("ingrese el número de columna: "))

def buscarUltimo (residuo):
  if residuo == 0:
    residuo=26
  m=1
  abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for a in abecedario:
    if (m==residuo):
      caracter = a
      break
    else:
      m=m+1
  return caracter

def ordenar(valoraOrdenar):
  largo=len(valoraOrdenar)
  resultado = ''
  for m in range  (0,largo):
    resultado= resultado + valoraOrdenar[largo-1-m]
  return resultado

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cociente = int (0)
residuo = int (0)
j=0
arreglo = ''
dividendo = columna
cociente = columna
residuo = int (cociente%26)
print("antes del while")
if 0 < dividendo <= 26 :
  print ("la columna en letras es:: "+ buscarUltimo(dividendo))
else:
  while cociente>0:
    residuo = int (dividendo%26)
    cociente = int (dividendo/26)
    arreglo = arreglo+buscarUltimo(residuo)
    if residuo==0: # en caso de que el residuo sea 0 se requiere que el cociente baje una unidad por ejemplo para que el 52 no sea BZ si no AZ y así todos los múltiplos del 26
      dividendo=cociente-1
    else:
      dividendo = cociente
  print ("la columna en letras es: " + ordenar(arreglo))
