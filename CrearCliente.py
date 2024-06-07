import tkinter as tk
from tkinter import *
from tkinter import messagebox

class CrearCliente():

    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def CrearCliente(self):
        listaClientes = self.corresponsal.escritor.leerArchivo()
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        cedula = self.txtCedula.get()
        telefono = self.txtTelefono.get()
        email = self.txtEmail.get()
        for cliente in listaClientes:
            if cliente.getCedula() == self.txtCedula.get():
                messagebox.showinfo("Mensaje", "El Usuario "+self.txtCedula.get()+" ya existe!")
                self.ventana.destroy()
                return

        else:
            if(len(cedula) > 0 and len(nombre) > 0 and len(apellido) > 0 and len(telefono) > 0 and len(email) > 0):
                self.corresponsal.crearCliente(listaClientes, cedula, nombre, apellido, telefono, email)
                messagebox.showinfo("Confirmación", "Cliente creado exitosamente!")
                self.Limpiar()
            else:
                messagebox.showwarning("Advertencia", "Los campos son obligatorios.")

    def Limpiar(self):
        self.txtCedula.delete(0, END)
        self.txtNombre.delete(0,END)
        self.txtApellido.delete(0, END)
        self.txtTelefono.delete(0, END)
        self.txtEmail.delete(0, END)
    

    def __init__(self, MenuCorresponsal, corresponsal):
        self.ventana = tk.Toplevel(MenuCorresponsal)
        self.ventana.title("Gestionar Usuario")
        self.ventana.resizable(0,0)#Esta función bloquea el aspecto o tamaño de la ventana
        
        self.corresponsal = corresponsal
        
        self.lblTitulo = tk.Label(self.ventana, text="Crear Usuario")
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
        self.txtApellido = tk.Entry(self.ventana, width=25)
        self.txtApellido.grid(row=4, column=1)
        self.lblTelefono = tk.Label(self.ventana, text="Telefono*:")
        self.lblTelefono.grid(row=5, column=0)
        self.txtTelefono = tk.Entry(self.ventana, width=25)
        self.txtTelefono.grid(row=5, column=1)
        self.lblEmail = tk.Label(self.ventana, text="Email*:")
        self.lblEmail.grid(row=6, column=0)
        self.txtEmail = tk.Entry(self.ventana, width=25)
        self.txtEmail.grid(row=6, column=1)
        self.btnGuardar = tk.Button(self.ventana, text="Guardar", command=lambda: self.CrearCliente())
        self.btnGuardar.grid(row=7, column=0, sticky=W)
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", command=lambda: self.Limpiar())
        self.btnLimpiar.grid(row=7, column=1)
        self.btnSalir = tk.Button(self.ventana, text="Salir", command=lambda: self.salirSistema())
        self.btnSalir.grid(row=7, column=2, sticky=E)

    
        self.ventana.mainloop()

    