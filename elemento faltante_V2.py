

from ast import Return
from copy import copy


def solution (A):
   longitud = len (A)
   B=[]
   for b in range (0, longitud+1): # un espacio para el número que no está
       B.append(0)
   print (B)
   for a in range (0, longitud):
      temp = A[a]
      print (temp, end='')
      B[temp-1]=temp
      print (B[a], end='')  
      #print (A[a], end='')
   print (B)
   elemento = 0
   for c in range (0, longitud):
       if (B[c]!= c+1):
        elemento = c+1
        break
   if elemento == 0:
       elemento = B[longitud-1]+1
       

   return elemento

print (str(solution([2,3,1,5,4,6,7,9,8,10])))