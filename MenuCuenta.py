import tkinter as tk
from tkinter import *
from tkinter import messagebox

class MenuCuenta():
    def salirApp(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def __init__(self, loggin, cuenta):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.geometry("400x450")
        self.ventana.focus_set() #Esta función asigna el foco a la ventana secundaria
        self.ventana.title("Menu Principal")
        self.ventana.resizable(0,0)

        self.cuenta = cuenta

        self.menu = tk.Menu(self.ventana)#Creamos barra de herramientas y ubicamos en ventana
        self.ventana.config(menu=self.menu)
        menuTransacciones = tk.Menu(self.menu)#Creamos opcion de menu y ubicamos en la barra
        self.menu.add_cascade(label="Gestionar Transacciones", menu=menuTransacciones)
        menuTransacciones.add_command(label="Realizar Retiro")
        menuTransacciones.add_separator()
        menuTransacciones.add_command(label="Realizar Depósito")

        salirMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=salirMenu)
        salirMenu.add_command(label="Salir", command=lambda: self.salirApp())

        messagebox.showinfo("Saludo", "Bienvenido "+self.cliente.getNombre()+" "+self.cliente.getApellido())

        self.ventana.mainloop()
