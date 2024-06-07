class Usuario():
    def __init__(self,nombre, apellido,  cedula,  telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.email = email



    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getCedula(self):
        return self.cedula
    def getTelefono(self):
        return self.telefono
    def getEmail(self):
        return self.email
    
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def setCedula(self, cedula):
        self.cedula = cedula
    def setTelefono(self, telefono):
        self.telefono = telefono
    def setEmail(self, email):
        self.email = email