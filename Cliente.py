from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self,nombre, apellido, cedula, telefono, email):
        Usuario.__init__(self,nombre, apellido, cedula, telefono, email)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__telefono = telefono
        self.__email = email


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