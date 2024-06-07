from Usuario import Usuario
from Cliente import Cliente
from SerializadorCliente import SerializadorCliente
from Cuenta import Cuenta
from SerializadorCuenta import SerializadorCuenta


class Corresponsal(Usuario):
    def __init__(self, nombre, apellido, cedula, telefono, email):
        Usuario.__init__(self, nombre, apellido, cedula, telefono, email)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__telefono = telefono
        self.__email = email
        self.escritor = SerializadorCliente()
        self.Escritor= SerializadorCuenta()

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCedula(self):
        return self.__cedula
    def getTelefono(self):
        return self.__telefono
    def getEmail(self):
        return self.__email
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setApellido(self, apellido):
        self.__apellido = apellido
    def setCedula(self, cedula):
        self.__cedula = cedula
    def setTelefono(self, telefono):
        self.__telefono = telefono
    def setEmail(self, email):
        self.__email = email


    def crearCliente(self, listaClientes, nombre, apellido, cedula, telefono, email):
        miCliente = Cliente(nombre, apellido, cedula, telefono, email)
        listaClientes.append(miCliente)
        self.escritor.escribirArchivo(nombre+"\n")
        self.escritor.escribirArchivo(apellido+"\n")
        self.escritor.escribirArchivo(cedula+"\n")
        self.escritor.escribirArchivo(telefono+"\n")
        self.escritor.escribirArchivo(email+"\n")


    def EliminarCliente(self, listaClientes, cedula):
        for cliente in listaClientes:
            if(cliente.getCedula() == cedula):
                listaClientes.remove(cliente)
                
                texto = ""
                for cliente in listaClientes:
                    texto = texto+cliente.getCedula()+"\n"
                    texto = texto+cliente.getNombre()+"\n"
                    texto = texto+cliente.getApellido()+"\n"
                    texto = texto+cliente.getTelefono()+"\n"
                    texto = texto+cliente.getEmail()+"\n"
                self.escritor.sobreEscribirArchivo(texto)
  
       
    def CrearCuenta(self, listaCuenta, cedula, numero_cuenta):
        saldo = 0.0
        cuenta = Cuenta(cedula, saldo, numero_cuenta)
        listaCuenta.append(cuenta)  
        self.Escritor.escribirArchivo(cedula+"\n")
        self.Escritor.escribirArchivo(str(saldo)+"\n")
        self.Escritor.escribirArchivo(numero_cuenta+"\n")
        
    def EliminarCuenta(self, listaCuenta, numero_cuenta):
       for cuenta in  listaCuenta:
         if(cuenta.getNumero_cuenta() == numero_cuenta):
                listaCuenta.remove(cuenta)
                
                texto = ""
                for cuenta in listaCuenta:
                    texto = texto+cuenta.getCedula()+"\n"
                    texto = texto+cuenta.getSaldo()+"\n"
                    texto = texto+cuenta.getNumero_cuenta()+"\n"
                self.Escritor.sobreEscribirArchivo(texto)

    
    def SaldoPromedio(self, listaCuenta):
        total_saldo = sum(float(cuenta.getSaldo()) for cuenta in listaCuenta)
        total = total_saldo / len(listaCuenta)  
        return (total)
        
