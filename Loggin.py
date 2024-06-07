import tkinter as tk
from tkinter import *
from tkinter import messagebox

from SerializadorCliente import SerializadorCliente
from SerializadorCorresponsal import SerializadorCorresponsal
from MenuCliente import MenuCliente
from MenuCorresponsal import MenuCorresponsal

class Loggin():
    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def validarIngreso(self):
        usuario = self.txtUsuario.get()
        password = self.txtPassword.get()
        if(len(usuario) >= 8 and len(password) >= 8):
            miSerializadorCliente = SerializadorCliente()
            listaClientes = miSerializadorCliente.leerArchivo()
            encontrado = False
            for cliente in listaClientes:
                if(cliente.getNombre()+"."+cliente.getApellido() == usuario and cliente.getCedula() == password):
                    miMenu = MenuCliente(self.ventana, cliente)
                    encontrado = True

                    
            if(encontrado == False):
                miSerializadorCorresponsal = SerializadorCorresponsal()
                listaCorresponsales = miSerializadorCorresponsal.leerArchivo()
                for corresponsal in listaCorresponsales:
                    if(corresponsal.getNombre()+"."+corresponsal.getApellido() == usuario and corresponsal.getCedula() == password):
                        miMenu = MenuCorresponsal(self.ventana, corresponsal)
                        encontrado = True

                        
                if(encontrado == False):
                    messagebox.showwarning("Advertencia", "Usuario y/o Password incorrectos, verifique de nuevo.")
        else:
            messagebox.showwarning("Advertencia", "El Usuario y Contraseña deben terner mínimo 8 caracteres.")
            
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesión")
        self.ventana.resizable(0,0)#Esta función bloquea el aspecto o tamaño de la ventana
        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión")
        self.lblTitulo.grid(row=1, column=1)
        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.grid(row=2, column=0)
        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.grid(row=3, column=0)
        self.txtUsuario = tk.Entry(self.ventana, width=25)
        self.txtUsuario.grid(row=2, column=1)
        self.txtPassword = tk.Entry(self.ventana, width=25, show='*')
        self.txtPassword.grid(row=3, column=1)
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", command=lambda: self.validarIngreso())
        self.btnIngresar.grid(row=4, column=1)
        self.btnSalir = tk.Button(self.ventana, text="Salir", command=lambda: self.salirSistema())
        self.btnSalir.grid(row=4, column=2)

        self.ventana.mainloop()