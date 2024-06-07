import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Retiro import Retiro
from Deposito import Deposito
class MenuCliente():
    def salirApp(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
    def Deposito(self):
        depositar = Deposito(self.ventana)
    def Retiro(self):
        retiro = Retiro(self.ventana)

    def __init__(self, loggin, cliente):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.geometry("250x250")
        self.ventana.focus_set() #Esta función asigna el foco a la ventana secundaria
        self.ventana.title("Menu Principal")
        self.ventana.resizable(0,0)

        self.cliente = cliente

        self.menu = tk.Menu(self.ventana)#Creamos barra de herramientas y ubicamos en ventana
        self.ventana.config(menu=self.menu)
        menuTransacciones = tk.Menu(self.menu)#Creamos opcion de menu y ubicamos en la barra
        self.menu.add_cascade(label="Gestionar Transacciones", menu=menuTransacciones)
        menuTransacciones.add_command(label="Realizar Retiro",command=lambda:self.Retiro())

        menuTransacciones.add_separator()
        menuTransacciones.add_command(label="Realizar Depósito")
        

        salirMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=salirMenu)
        salirMenu.add_command(label="Salir", command=lambda: self.salirApp())

        self.lblTitulo = tk.Label(self.ventana, text="Bienvenido "+self.cliente.getNombre()+" "+ self.cliente.getApellido())
        self.lblTitulo.grid(row=3, column=6)

        self.ventana.mainloop()