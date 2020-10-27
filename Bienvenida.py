from tkinter import *
from tkinter import messagebox
#import os


def aceptar():
    
    usuario=usuarioTexto.get()
    password=pwdbox.get()
    usuarioTexto.delete(0, END)
    pwdbox.delete(0, END)
    
    if usuario == "Manolo":
           
        if password == "6352":            
            raiz.destroy
            messagebox.showinfo("Perfecto","Datos correctos,bienvenido")
        else:
            messagebox.showwarning("Error","Datos incorrectos, pruebe de nuevo")
         

#----------Configuracion frame principal---------

raiz=Tk()
raiz.title("Gestión de recibos - Calzados Catedral")
raiz.iconbitmap()
raiz.geometry("370x250")
raiz.config(bg="#D6D2D1", bd=5, relief="ridge")

#----------Etiquetas-----------------------------

tituloLabel=Label(raiz, text="Gestión de recibos")
tituloLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
tituloLabel.config(justify="center", font=("Times", "24", "bold"), bg="#D6D2D1", fg="green")

presentacionLabel=Label(raiz, text="Bienvenido al programa de gestión \n de recibos de Calzados Catedral", fg="blue", bg="#D6D2D1")
presentacionLabel.grid(row=1, column=0, columnspan=3)
presentacionLabel.grid(padx=10, pady=10)

usuarioLabel=Label(raiz, text="Usuario: ", bg="#D6D2D1")
usuarioLabel.grid(row=2, column=1, sticky="e")

passLabel=Label(raiz, text="Contraseña: ", bg="#D6D2D1")
passLabel.grid(row=3, column=1, sticky="e")

imagenLabel=Label(raiz)
imagenLabel.grid(row=3, column=0)

autorLabel=Label(raiz, text="@Magilma 2020 - Versión 1.0", bg="#D6D2D1")
autorLabel.grid(row=5, column=0, padx=10, pady=10)
autorLabel.config(justify="left", font=("Calibri", "7"), pady=3)

#----------Entrada de datos-----------------------------

usuarioTexto=Entry(raiz, fg=("red"))
usuarioTexto.grid(row=2, column=2)

pwdbox=Entry(raiz, show="*", fg=("red"))
pwdbox.grid(row=3, column=2)


botonEntrar=Button(raiz, text="Aceptar", command=aceptar)
botonEntrar.grid(row=4, column=2, padx=10, pady=10)


raiz.mainloop()

