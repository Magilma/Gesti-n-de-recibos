import tkinter
from tkinter import *
from tkinter import messagebox


       
def bienvenida(): #Esta es la función que crea la pantalla de bienvenida

    #----------Configuracion frame principal---------
    global raiz
    raiz=Tk()
    raiz.title("Gestión de recibos - Calzados Catedral")
    raiz.iconbitmap("logo_sin_fondo.ico")
    raiz.geometry("300x275+400+200")
    raiz.config(bg="white", bd=5, relief="ridge")

    #----------Etiquetas-----------------------------

    global tituloLabel
    global comentarioLabel
    global botonEntrar

    logo=PhotoImage(file="logo_pequeño.gif")
    Label(raiz, image=logo, width=80, height=80, bd=0).pack()
    
    tituloLabel=Label(raiz, text="Seguros y Suministros", font=("Times", "20", "bold"), bg="white", fg="green").pack()
    
    comentarioLabel=Label(raiz, text="Bienvenido al programa de gestión \n de seguros y suministros \n de Calzados Catedral\n", fg="blue", bg="white").pack()
  
    botonEntrar=Button(raiz, text="Entrar", width=15, height=2, pady=1, command=entrar).pack()
         
    autorLabel=Label(raiz, text="\n \n                                                    @Magilma 2020 - Versión 1.0", bg="white", justify="left")
    autorLabel.config(justify="left", font=("Calibri", "7"), pady=3)
    autorLabel.pack()

    raiz.mainloop() 

def entrar(): #Esta es la función que crea la pantalla de  Inicio de Sesión
    
    #----------Configuracion frame ---------
    global iniciosesion
    iniciosesion=Toplevel(raiz)
    iniciosesion.title("Identificación")
    iniciosesion.iconbitmap("logo_sin_fondo.ico")
    iniciosesion.geometry("250x130+400+200")
    iniciosesion.config(bg="light blue", bd=5, relief="ridge")
    raiz.iconify()

    #----------Etiquetas-----------------------------
    global usuarioLabel
    global passLabel
    
    usuarioLabel=Label(iniciosesion, text="Usuario: ", bg="light blue", width=15, height=2)
    usuarioLabel.grid(row=1, column=1, sticky="e")

    passLabel=Label(iniciosesion, text="Contraseña: ", bg="light blue", width=15, height=2)
    passLabel.grid(row=2, column=1, sticky="e")

    #----------Entrada de datos-----------------------------
    global usuarioTexto
    global pwdbox
    
    usuarioTexto=Entry(iniciosesion, fg=("red"), bd=3)
    usuarioTexto.grid(row=1, column=2)

    pwdbox=Entry(iniciosesion, show="*", fg=("red"), bd=3)
    pwdbox.grid(row=2, column=2) 

    botonAceptar=Button(iniciosesion, text="Aceptar", width=10, height=2, pady=1, command=verificar)
    botonAceptar.grid(row=3, column=1, columnspan=2)

 
def verificar(): #Esta es la función que verifica el login y crea la pantalla de selección de suminstros

    usuario=usuarioTexto.get()
    password=pwdbox.get()
    usuarioTexto.delete(0, END)
    pwdbox.delete(0, END)
    
    if usuario == "Manolo" and password == "Catedral":   
          
        seleccionar()     
        messagebox.showinfo("Perfecto","Datos correctos,bienvenido")
        
    else:
        messagebox.showwarning("Error","Datos incorrectos, pruebe de nuevo")

def seleccionar():
            
        #----------Configuracion frame ---------
        global seleccion
        seleccion=Toplevel(raiz)
        seleccion.title("Selecion de suministro")
        seleccion.iconbitmap("logo_sin_fondo.ico")
        seleccion.geometry("370x250+400+200")
        seleccion.config(bg="#D6D2D1", bd=5, relief="ridge")
        
        #----------Etiquetas---------------------

        global seleccionLabel
        global autorLabel

        seleccionLabel=Label(seleccion, text="¿Sobre que suministro desea operar?", font=("Times", 14, "bold"), bg="#D6D2D1", fg="red")
        seleccionLabel.grid(row=0, column=0, columnspan=2)

        autorLabel=Label(seleccion, text="@Magilma 2020 - Versión 1.0", bg="#D6D2D1")
        autorLabel.grid(row=3, column=0, padx=5, pady=3)
        autorLabel.config(justify="left", font=("Calibri", "7"))

        #----------Botones-----------------------

        botonSeguros=Button(seleccion, text="Seguros", width=18, height=4, bd=5, fg="green", font=("Times", 10, "bold"))
        botonSeguros.grid(row=1, column=0, padx=16, pady=10)

        botonLuz=Button(seleccion, text="Luz", width=18, height=4, bd=5, fg="green", font=("Times", 10, "bold"))
        botonLuz.grid(row=1, column=1, padx=16, pady=10)

        botonAgua=Button(seleccion, text="Agua", width=18, height=4, bd=5, fg="green", font=("Times", 10, "bold"))
        botonAgua.grid(row=2, column=0, padx=16, pady=10)

        botonGas=Button(seleccion, text="Gas", width=18, height=4, bd=5, fg="green", font=("Times", 10, "bold"))
        botonGas.grid(row=2, column=1, padx=16, pady=10)

   
    


bienvenida()
