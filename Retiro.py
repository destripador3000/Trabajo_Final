from tkinter import messagebox
import tkinter as tk
from tkinter import *



class Retiro():
    
    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()

    def realizarRetiro(self, listacuenta):
            numero_cuenta = input("Ingrese el número de cuenta: ")
            for cuenta in listacuenta:
                if cuenta.getNumeroCuenta() == numero_cuenta:
                    monto = int(input("Ingrese el valor que desea retirar: "))
                    if 0 < monto <= cuenta.getSaldo():
                        cuenta.setSaldo(cuenta.getSaldo() - monto)
                        messagebox.showinfo("Retiro exitoso", "El saldo ha sido retirado con éxito!")
                    else:
                        messagebox.showwarning("Error", "Monto no válido o insuficiente saldo.")
        
        
    def __init__(self, MenuCorresponsal, corresponsal):
        self.ventana=tk.Toplevel(MenuCorresponsal)
        self.ventana.focus_set()
        self.ventana.title("Realizar Retiro")
        self.ventana.resizable(0,0)

        self.corresponsal = corresponsal
        
        self.lblTitulo=tk.Label(self.ventana, text="Retiro")
        self.lblTitulo.grid(row=1, column=1)
        self.lblNumeroC = tk.Label(self.ventana, text="Número de Cuenta*:")
        self.lblNumeroC.grid(row=2, column=0)
        
        self.lblTransaccion =tk.Label(self.ventana, text="Número de Transacción*:")
        self.lblTransaccion.grid(row=3, column=0)
        self.lblMonto = tk.Label(self.ventana, text="Monto*: ")
        self.lblMonto.grid(row=4, column=0)
        self.lblCedula = tk.Label(self.ventana, text="Cédula Titular*: ")
        self.lblCedula.grid(row=5, column=0)        
        self.txtNumeroC =tk.Entry(self.ventana, width=25)
        self.txtNumeroC.grid(row=2, column=1)
        self.txtNumeroT =tk.Entry(self.ventana,width=25)
        self.txtNumeroT.grid(row=3, column=1)
        self.txtMonto = tk.Entry(self.ventana, width=25)
        self.txtMonto.grid(row=4, column=1)
        self.txtCedulaT =tk.Entry(self.ventana, width=25)
        self.txtCedulaT.grid(row=5,column=1)
        self.btnAgregar = tk.Button(self.ventana, text="Agregar",command="")
        self.btnAgregar.grid(row=6, column=0)
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", command="")
        self.btnLimpiar.grid(row=6, column=1)
        self.btnSalir=tk.Button(self.ventana, text="Salir", command="")
        self.btnSalir.grid(row=6, column=2)
        self.btnBuscar=tk.Button(self.ventana, text="Buscar", command="")
        self.btnBuscar.grid(row=7, column=2)

        self.ventana.mainloop()