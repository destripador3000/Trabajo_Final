import tkinter as tk
from tkinter import *
from tkinter import messagebox

from CrearCliente import CrearCliente
from EliminarCliente import EliminarCliente
from GenerarReporte import GenerarReporte
from CrearCuenta import CrearCuenta
from EliminarCuenta import EliminarCuenta
from Retiro import Retiro
from Deposito import Deposito

class MenuCorresponsal():
    def salirApp(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    
    def CrearCliente(self):
        registrar = CrearCliente(self.ventana, self.corresponsal)

    def EliminarCliente(self):
        eliminar = EliminarCliente(self.ventana, self.corresponsal)

    def GenerarReporte(self):
        generar = GenerarReporte(self.ventana, self.corresponsal)

    def CrearCuenta(self):
        crear = CrearCuenta(self.ventana, self.corresponsal)
  
    def EliminarCuenta(self):
        eliminar = EliminarCuenta(self.ventana, self.corresponsal)
    
    def Deposito(self):
        depositar = Deposito(self.ventana, self.corresponsal)

    def Retiro(self):
        retiro = Retiro(self.ventana, self.corresponsal)


    def __init__(self, loggin, corresponsal):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.geometry("550x200")
        self.ventana.focus_set() #Esta función asigna el foco a la ventana secundaria
        self.ventana.title("Menu Principal")
        self.ventana.resizable(0,0)

        self.corresponsal = corresponsal

        self.menu = tk.Menu(self.ventana)#Creamos barra de herramientas y ubicamos en ventana
        self.ventana.config(menu=self.menu)

        menuCliente = tk.Menu(self.menu)#Creamos opcion de menu y ubicamos en la barra
        self.menu.add_cascade(label="Gestionar Clientes", menu=menuCliente)
        menuCliente.add_command(label="Registrar Cliente", command=lambda: self.CrearCliente())
        menuCliente.add_separator()
        menuCliente.add_command(label="Eliminar Cliente", command=lambda: self.EliminarCliente())
        menuCliente.add_separator()

        menuCuentas = tk.Menu(self.menu)#Creamos opcion de menu y ubicamos en la barra
        self.menu.add_cascade(label="Gestionar Cuentas", menu=menuCuentas)
        menuCuentas.add_command(label="Crear cuenta", command=lambda: self.CrearCuenta())
        menuCuentas.add_separator()
        menuCuentas.add_command(label="Eliminar cuenta", command=lambda: self.EliminarCuenta())
        menuCuentas.add_separator()

        menuTransacciones = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Transacciones", menu=menuTransacciones) 
        menuTransacciones.add_command(label="Realizar retiro", command=lambda: self.Deposito())
        menuTransacciones.add_separator()
        menuTransacciones.add_command(label="Realizar deposito", command=lambda: self.Retiro())
        menuTransacciones.add_separator()

        menuConsultas = tk.Menu(self.menu)
        self.menu.add_cascade(label="Consultar Información", menu=menuConsultas)
        menuConsultas.add_command(label="Generar Reporte", command=lambda: self.GenerarReporte())
        menuConsultas.add_separator()

        salirMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label= "Salir", menu = salirMenu)
        salirMenu.add_command(label= "Salir", command=lambda: self.salirApp())

        self.lblTitulo = tk.Label(self.ventana, text="Bienvenido Corresponsal "+self.corresponsal.getNombre()+" "+ self.corresponsal.getApellido())
        self.lblTitulo.grid(row=3, column=6)
        self.ventana.mainloop()