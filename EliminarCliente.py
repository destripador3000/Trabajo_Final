import tkinter as tk
from tkinter import *
from tkinter import messagebox

class EliminarCliente():

    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass
            

    def EliminarCliente(self):
        listaClientes = self.corresponsal.escritor.leerArchivo()
        cedula = self.txtCedula.get()
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro que desea eliminar al cliente " + self.txtCedula.get())
        if respuesta == "yes":
            self.corresponsal.EliminarCliente(listaClientes, cedula)
            messagebox.showinfo("Mensaje", "El Usuario "+self.txtCedula.get()+" ha sido eliminado con éxito!")
            self.Limpiar()
            self.ventana.destroy()

    def Buscar(self):
        listaClientes = self.corresponsal.escritor.leerArchivo()
        cedula = self.txtCedula.get()
        if(len(cedula) > 0 ):
            for cliente in listaClientes:
                if cliente.getCedula() == self.txtCedula.get():
                    self.txtNombre.delete(0,END)
                    self.txtNombre.insert(0, cliente.getNombre())
                    self.txtNombre.config(state='disabled')
                    self.txtApellido.delete(0, END)
                    self.txtApellido.insert(0, cliente.getApellido())
                    self.txtApellido.config(state='disabled')
                    self.txtTelefono.delete(0, END)
                    self.txtTelefono.insert(0, cliente.getTelefono())
                    self.txtTelefono.config(state='disabled')
                    self.txtEmail.delete(0, END)
                    self.txtEmail.insert(0, cliente.getEmail())
                    self.txtEmail.config(state='disabled')
                    return
            else:
                messagebox.showinfo("Mensaje", "El Usuario "+self.txtCedula.get()+" no se encontro")
        else:
            messagebox.showwarning("Advertencia", "Los campos son obligatorios.")


    def Limpiar(self):
        self.txtCedula.delete(0, END)
        self.txtNombre.config(state='normal')
        self.txtNombre.delete(0,END)
        self.txtApellido.config(state='normal')
        self.txtApellido.delete(0, END)
        self.txtTelefono.config(state='normal')
        self.txtTelefono.delete(0, END)
        self.txtEmail.config(state='normal')
        self.txtEmail.delete(0, END)

    

    def __init__(self, MenuCorresponsal, corresponsal):
            self.ventana = tk.Toplevel(MenuCorresponsal)
            self.ventana.title("Gestionar Usuario")
            self.ventana.resizable(0,0)
            
            self.corresponsal = corresponsal
            
            self.lblTitulo = tk.Label(self.ventana, text="Eliminar usuario")
            self.lblTitulo.grid(row=1, column=1)
            self.lblCedula = tk.Label(self.ventana, text="Cédula*:")
            self.lblCedula.grid(row=2, column=0)
            self.txtCedula = tk.Entry(self.ventana, width=25)
            self.txtCedula.grid(row=2, column=1)
            self.lblNombre = tk.Label(self.ventana, text="Nombres*:")
            self.lblNombre.grid(row=3, column=0)
            self.txtNombre = tk.Entry(self.ventana, width=25)
            self.txtNombre.grid(row=3, column=1)
            self.lblApellido = tk.Label(self.ventana, text="Apellidos*:")
            self.lblApellido.grid(row=4, column=0)
            self.txtApellido= tk.Entry(self.ventana, width=25)
            self.txtApellido.grid(row=4, column=1)
            self.lblTelefono = tk.Label(self.ventana, text="Telefono*:")
            self.lblTelefono.grid(row=5, column=0)
            self.txtTelefono = tk.Entry(self.ventana, width=25)
            self.txtTelefono.grid(row=5, column=1)
            self.lblEmail = tk.Label(self.ventana, text="Email*:")
            self.lblEmail.grid(row=6, column=0)
            self.txtEmail = tk.Entry(self.ventana, width=25)
            self.txtEmail.grid(row=6, column=1)
            self.btnBuscar = tk.Button(self.ventana, text="Buscar", command=lambda: self.Buscar())
            self.btnBuscar.grid(row=2, column=2)
            self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", command=lambda: self.Limpiar())
            self.btnLimpiar.grid(row=7, column=1)
            self.btnEliminar = tk.Button(self.ventana, text="Eliminar", command=lambda: self.EliminarCliente())
            self.btnEliminar.grid(row=7, column=0, sticky=W)
            self.btnLimpiar = tk.Button(self.ventana, text="Limpiar")
            self.btnSalir = tk.Button(self.ventana, text="Salir", command=lambda: self.salirSistema())
            self.btnSalir.grid(row=7, column=3, sticky=W)

            self.ventana.mainloop()

