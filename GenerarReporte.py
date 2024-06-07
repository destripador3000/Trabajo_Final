import tkinter as tk
from tkinter import *
from tkinter import messagebox

class GenerarReporte():

    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "¿Está seguro de salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        
    
    def info_cuentas(self):
        listaCuenta = self.corresponsal.Escritor.leerArchivo()
        info_cuentas = []

        for cuenta in listaCuenta:
            titular = "*" + cuenta.getCedula()[-4:]
            numero_cuenta = '*' + cuenta.getNumero_cuenta()[-4:]
            saldo = cuenta.getSaldo()

            info_cuentas.append((titular, numero_cuenta, saldo))

        return info_cuentas

    def cuentas(self):
        listaCuenta = self.corresponsal.Escritor.leerArchivo()
        return len(listaCuenta)
            
    def promedio(self):
        listaCuenta = self.corresponsal.Escritor.leerArchivo()
        return self.corresponsal.SaldoPromedio(listaCuenta)

    def __init__(self, MenuCorresponsal, corresponsal):
        self.ventana = tk.Toplevel(MenuCorresponsal)
        self.ventana.title("Reporte")
        self.ventana.resizable(0, 0)
        
        self.corresponsal = corresponsal

        self.lblTitulo = tk.Label(self.ventana, text="Generar reporte")
        self.lblTitulo.grid(row=2, column=1)

        info_cuentas = self.info_cuentas()

        for i, (titular, numero_cuenta, saldo) in enumerate(info_cuentas, start=3):
            tk.Label(self.ventana, text=f"Titular: {titular}").grid(row=i, column=0)
            tk.Label(self.ventana, text=f"Cuenta: {numero_cuenta}").grid(row=i, column=1)
            tk.Label(self.ventana, text=f"Saldo: {saldo}").grid(row=i, column=2)

        tk.Label(self.ventana, text="Saldo promedio: " + str(self.promedio())).grid(row=i + 2, column=0)
        tk.Label(self.ventana, text="Total cuentas: " + str(self.cuentas())).grid(row=i + 2, column=1)

        self.btnSalir = tk.Button(self.ventana, text="Salir", command=lambda: self.salirSistema())
        self.btnSalir.grid(row=i + 2, column=3)

        self.ventana.mainloop()