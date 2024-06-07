class Cuenta():
    def __init__(self, cedula, saldo, numero_cuenta):
        self.cedula = cedula
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta
    
    def getCedula(self):
        return self.cedula
    def getSaldo(self):
        return self.saldo
    def getNumero_cuenta(self):
        return self.numero_cuenta

    def setCedula(self, cedula):
        self.cedula = cedula
    def setSaldo(self,saldo):
        self.saldo = saldo
    def setNumero_cuenta(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta
