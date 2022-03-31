class Criptomoneda(object):
    def __init__(self, nombre,  saldo, cotizacion):
        self.nombre = nombre
        self.saldo = saldo
        self.cotizacion = cotizacion
    
    def indicarNombre(self, nombre):
        self.nombre=nombre
    
    def indicarCotizacion(self, cotizacion):
        self.cotizacion=cotizacion
    
    def indicarSaldo(self, saldo):  
        self.saldo=saldo
    
    def mostrarNombre(self):
        return self.nombre
    
    def imostrarCotizacion(self): 
        return self.cotizacion
    
    def mostrarSaldo(self):  
        return  self.saldo
    
    def calcularSaldo(self, moneda):  
        if moneda== "USD":
            return self.saldo*self.cotizacion
        else:
            return self.saldo
print ("Billetera de Criptomonedas tipo DESKTOP \n Menú:")
print ("1. Recibir cantidad")
print ("2. transferir monto")
print ("3. Mostrar balance de una moneda")
print ("4. Mostrar balance general")
print ("5. Mostrar histórico de transacciones")
print ("6. Salir del programa")
opcion = input ("ingrese opción: ")

if opcion == "1":
    nombreCripto = input ("ingrese nombre de la criptomoneda: ")
    cantidadRecibiro = input ("ingrese la cantidad a recibir de " + nombreCripto + ": ")
    codigoRemitente = input ("ingrese el código del remitente: ")

if opcion == "2":
    nombreCripto = input ("ingrese nombre de la criptomoneda a enviar: ")
    cantidadEnviar = input ("ingrese el monto a enviar: ")
    codigoDestinatario = input ("ingrese el código del destinatario: ")

if opcion == "3":
    nombreCripto = input ("ingrese nombre de la criptomoneda para mostrar su balance: ")

else:
    pass    

