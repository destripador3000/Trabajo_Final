import tkinter as tk
from tkinter import *
from tkinter import messagebox

class EliminarCuenta():

    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass
            

    def EliminarCuenta(self):
        listaCuenta = self.corresponsal.Escritor.leerArchivo()
        numero_cuenta = self.txtNumero_cuenta.get()

        respuesta = messagebox.askquestion("Confirmación", "Esta seguro que desea eliminar la cuenta" + self.txtNumero_cuenta.get())
        if respuesta == "yes":
                self.corresponsal.EliminarCuenta(listaCuenta, numero_cuenta)
                messagebox.showinfo("Mensaje", "El Usuario "+self.txtNumero_cuenta.get()+" ha sido eliminado con éxito!")
                self.Limpiar()
                self.ventana.destroy()
        else:
            messagebox.showinfo("Mensaje", "El Usuario "+self.txtNumero_cuenta.get()+"no se encontro")
            self.ventana.destroy()

    def Buscar(self):
        listaCuenta = self.corresponsal.Escritor.leerArchivo()
        numero_cuenta = self.txtNumero_cuenta.get()
        if(len(numero_cuenta) > 0 ):
            for cuenta in listaCuenta:
                if cuenta.getNumero_cuenta() == self.txtNumero_cuenta.get():
                    self.txtCedula.delete(0,END)
                    self.txtCedula.insert(0, cuenta.getCedula())
                    self.txtCedula.config(state='disabled')
                    self.txtSaldo.delete(0, END)
                    self.txtSaldo.insert(0, cuenta.getSaldo())
                    self.txtSaldo.config(state='disabled')
                    return
            else:
                messagebox.showinfo("Mensaje", "El Usuario "+self.txtNumero_cuenta.get()+" no se encontro")
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
            
            self.lblTitulo = tk.Label(self.ventana, text="Eliminar Cuenta")
            self.lblTitulo.grid(row=1, column=1)

            self.lblCedula = tk.Label(self.ventana, text="Cédula*:")
            self.lblCedula.grid(row=2, column=0)
            self.txtCedula = tk.Entry(self.ventana, width=25)
            self.txtCedula.grid(row=2, column=1)
            self.lblSaldo = tk.Label(self.ventana, text="Saldo*:")
            self.lblSaldo.grid(row=3, column=0)
            self.txtSaldo = tk.Entry(self.ventana, width=25)
            self.txtSaldo.grid(row=3, column=1)
            self.lblNumero_Cuenta = tk.Label(self.ventana, text="Numero de Cuenta*:")
            self.lblNumero_Cuenta.grid(row=4, column=0)
            self.txtNumero_cuenta= tk.Entry(self.ventana, width=25)
            self.txtNumero_cuenta.grid(row=4, column=1)
            self.btnBuscar = tk.Button(self.ventana, text="Buscar", command=lambda: self.Buscar())
            self.btnBuscar.grid(row=4, column=2)
            self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", command=lambda: self.Limpiar())
            self.btnLimpiar.grid(row=5, column=1)
        
            self.btnEliminar = tk.Button(self.ventana, text="Eliminar", command=lambda: self.EliminarCuenta())
            self.btnEliminar.grid(row=5, column=0, sticky = W)
            self.btnSalir = tk.Button(self.ventana, text="Salir", command=lambda: self.salirSistema())
            self.btnSalir.grid(row=5, column=2, sticky=E)

            self.ventana.mainloop()