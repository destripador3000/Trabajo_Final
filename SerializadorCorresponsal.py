from Corresponsal import Corresponsal

class SerializadorCorresponsal():
    def __init__(self):
        self.__archivo = open("corresponsales.txt", "a")

    def getArchivo(self):
        return self.__archivo
    
    #Se utiliza cuando creo objetos
    def escribirArchivo(self, texto):
        self.__archivo = open("corresponsales.txt", "a")
        self.__archivo.write(texto)
        self.__archivo.close()

    #Se utiliza cuando modifico o elimino objetos
    def sobreEscribirArchivo(self, texto):
        self.__archivo = open("corresponsales.txt", "w")
        self.__archivo.write(texto)
        self.__archivo.close()

    #Se utiliza cuando inicia la aplicación 
    def leerArchivo(self):
        nombre = "" 
        apellido = "" 
        cedula = ""
        telefono = ""
        email = ""
        listaCorresponsal = []
        i = 0
        self.__archivo = open("corresponsales.txt", "r")
        for linea in self.__archivo:
            if(i==0):
                nombre= linea.strip()
                i+=1
            elif(i==1):
                apellido = linea.strip()
                i+=1
            elif(i==2):
                cedula = linea.strip()
                i+=1
            elif(i==3):
                telefono = linea.strip()
                i+=1
            else:
                email = linea.strip()
                i=0 
                miCorresponsal = Corresponsal(nombre, apellido, cedula, telefono, email)
                listaCorresponsal.append(miCorresponsal)
        self.__archivo.close()
        return listaCorresponsal