lista=[]
dict1={'symbol':'BTC', 'cantidad':500}
dict2={'symbol':'ETH', 'cantidad':450}
dict3={'symbol':'PAR', 'cantidad':0.25}
lista=[dict1,dict2,dict3]
print (lista)
print (lista[2])
print (lista[2]['symbol'])
fileW=open("I:/NEXTU/PYTHON/pruebasDiccionarioListas.txt","w")
fileW.write(str(lista))
fileW.close()

fileX=open("I:/NEXTU/PYTHON/pruebasDiccionarioListas.txt","r")
lista2=[]
lista2=eval(fileX.read())
print("la lista 2 es: ")
print (lista2)
dict4={'symbol':'COM', 'cantidad':-0.55}
lista2.append(dict4)
print(lista2)
print(lista2[3]['cantidad'])
print("valor actual: ")
print(lista2[3]['cantidad'])
lista2[3]['cantidad']=lista2[3]['cantidad']+100.5
print(lista2[3]['cantidad'])