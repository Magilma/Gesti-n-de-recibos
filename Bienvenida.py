from tkinter import *
from tkinter import messagebox

#----------Configuracion frame principal---------

raiz=Tk()
raiz.title("Gestión de recibos - Calzados Catedral")
raiz.iconbitmap()
raiz.geometry("300x300")
raiz.config(bg="#D6D2D1")
raiz.config(bd=10)
raiz.config(relief="ridge")

#----------Etiquetas-----------------------------

tituloLabel=Label(raiz, text="Gestión de recibos", font=(400), bg="#D6D2D1", fg="green", padx=10, pady=10)
tituloLabel.grid(row=0, column=0, columnspan=3)
tituloLabel.config(justify="center")
#tituloLabel.pack()

presentacionLabel=Label(raiz, text="Bienvenido al programa de gestión \n de recibos de Calzados Catedral", fg="blue", bg="#D6D2D1", padx=10, pady=10)
presentacionLabel.grid(row=1, column=0, columnspan=3)
#presentacionLabel.pack()

usuarioLabel=Label(raiz, text="Usuario: ", bg="#D6D2D1")
usuarioLabel.grid(row=2, column=1, sticky="e")
#usuarioLabel.pack()

passLabel=Label(raiz, text="Contraseña: ", bg="#D6D2D1")
passLabel.grid(row=3, column=1, sticky="e")
#passLabel.pack()

imagenLabel=Label(raiz)
imagenLabel.grid(row=3, column=0)

autorLabel=Label(raiz, text="@Magilma 2020 - Versión 1.0", bg="#D6D2D1")
autorLabel.grid(row=4, column=0, padx=10, pady=10)

#----------Entrada de datos-----------------------------

usuarioTexto=Entry(raiz, fg=("red"))
usuarioTexto.grid(row=2, column=2)

passTexto=Entry(raiz, fg=("red"))
passTexto.grid(row=3, column=2)
passTexto.config(show="*")

botonEntrar=Button(raiz, text="Entrar")
botonEntrar

raiz.mainloop()

