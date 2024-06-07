from Cuenta import Cuenta


class SerializadorCuenta():
    def __init__(self):
        self.__archivo = open("cuentas.txt", "a")

    def getArchivo(self):
        return self.__archivo
    
    #Se utiliza cuando creo objetos
    def escribirArchivo(self, texto):
        self.__archivo = open("cuentas.txt", "a")
        self.__archivo.write(texto)
        self.__archivo.close()

    #Se utiliza cuando modifico o elimino objetos
    def sobreEscribirArchivo(self, texto):
        self.__archivo = open("cuentas.txt", "w")
        self.__archivo.write(texto)
        self.__archivo.close()

    #Se utiliza cuando inicia la aplicación 
    def leerArchivo(self):
        cedula = "" # i=0
        saldo = "" # i=1
        numero_cuenta = ""
        listaCuenta = []
        i = 0
        self.__archivo = open("cuentas.txt", "r")
        for linea in self.__archivo:
            if(i==0):
                cedula  = linea.strip()
                i+=1
            elif(i==1):
                saldo = linea.strip()
                i+=1
            else:
                numero_cuenta = linea.strip()
                i=0 # Esto indica al lector que la siguiente linea es un nombre
                miCuenta = Cuenta(cedula, saldo, numero_cuenta)
                listaCuenta.append(miCuenta)
        self.__archivo.close()
        return listaCuenta