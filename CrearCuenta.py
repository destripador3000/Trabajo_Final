import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import randint
class CrearCuenta():

    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def CrearCuenta(self):
        listaCuenta = self.corresponsal.Escritor.leerArchivo()
        cedula = self.txtCedula.get()
        numero_cuenta = self.txtNumero_cuenta.get()
        if(len(cedula) > 0 ):
            self.corresponsal.CrearCuenta(listaCuenta, cedula, numero_cuenta)
            messagebox.showinfo("Confirmación", "Cuenta  creada exitosamente!")
            self.Limpiar()

        else:
            messagebox.showwarning("Advertencia", "Los campos son obligatorios.")

    


    def Buscar(self):
        listaCuenta = self.corresponsal.Escritor.leerArchivo()
        cedula = self.txtCedula.get()
        if(len(cedula) > 0 ):
            for cuenta in listaCuenta:
                if cuenta.getCedula() == self.txtCedula.get():
                    messagebox.showinfo("Mensaje", "El Usuario "+self.txtCedula.get()+" ya tiene una cuenta")
                    self.ventana.destroy()
            else: 
                numero_cuenta = [randint(1000000000, 9999999999) for i in range(0, 1)]
                for cuenta in listaCuenta:
                    if cuenta.getNumero_cuenta() == numero_cuenta[0]:
                        while numero_cuenta == cuenta.getNumero_cuenta():
                            numero_cuenta = randint(1000000000, 9999999999)
                    else: 
                        pass
                self.txtSaldo.delete(0,END)
                self.txtSaldo.insert(0, "0")
                self.txtSaldo.config(state='disabled')
                self.txtNumero_cuenta.delete(0, END)
                self.txtNumero_cuenta.insert(0, numero_cuenta)
                self.txtNumero_cuenta.config(state='disabled')
                return
        else:
            messagebox.showwarning("Advertencia", "Los campos son obligatorios.")

    def Limpiar(self):
        self.txtCedula.delete(0, END)
        self.txtSaldo.config(state='normal')
        self.txtSaldo.delete(0,END)
        self.txtNumero_cuenta.config(state='normal')
        self.txtNumero_cuenta.delete(0, END)

    

    def __init__(self, MenuCorresponsal, corresponsal):
            self.ventana = tk.Toplevel(MenuCorresponsal)
            self.ventana.title("Gestionar Usuario")
            self.ventana.resizable(0,0)
            
            self.corresponsal = corresponsal
            
            self.lblTitulo = tk.Label(self.ventana, text="Crear cuenta")
            self.lblTitulo.grid(row=1, column=1)
            self.lblCedula = tk.Label(self.ventana, text="Cédula*:")
            self.lblCedula.grid(row=2, column=0)
            self.txtCedula = tk.Entry(self.ventana, width=25)
            self.txtCedula.grid(row=2, column=1)
            self.lblSaldo = tk.Label(self.ventana, text="Saldo*:")
            self.lblSaldo.grid(row=3, column=0)
            self.txtSaldo = tk.Entry(self.ventana, width=25)
            self.txtSaldo.grid(row=3, column=1)
            self.lblNumero_cuenta = tk.Label(self.ventana, text="Numero de cuenta*:")
            self.lblNumero_cuenta.grid(row=4, column=0)
            self.txtNumero_cuenta = tk.Entry(self.ventana, width=25)
            self.txtNumero_cuenta.grid(row=4, column=1)
            self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", command=lambda: self.Limpiar())
            self.btnLimpiar.grid(row=5, column=2)
            self.btnBuscar = tk.Button(self.ventana, text="Buscar", command=lambda: self.Buscar())
            self.btnBuscar.grid(row=2, column=2)
            self.btnEliminar = tk.Button(self.ventana, text="Crear", command=lambda: self.CrearCuenta())
            self.btnEliminar.grid(row=5, column=0, sticky = W)
            self.btnSalir = tk.Button(self.ventana, text="Salir", command=lambda: self.salirSistema())
            self.btnSalir.grid(row=5, column=3, sticky=E)

            self.ventana.mainloop()