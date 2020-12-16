# -*- coding: utf-8 -*-


from tkinter import *
from DiccionarioLista import *

# Variable global
# (Nota: no se requiere agregar una línea 'global D' dentro de cada función que usa D porque
# D fue definido primero *fuera* de todas las funciones. Sólo se necesita cuando la variable es definida
# primero dentro de una función.) )
D=Diccionario("diccionario.txt")

#metodo para boton buscar
def buscar():
    s=D.buscar(palabra.get())
    if s==None:
        responder("no existe")
    else:
        significado.delete(0,END) #limpiar
        significado.insert(0,s)
        responder("encontrado")

#metodo para boton agregar
def agregar():
    p=palabra.get()
    if D.agregar(p,significado.get()):
        responder("agregado")
    elif D.buscar(p) != None: 
        responder("ya existe")
    else: 
        responder("no hay espacio")

#metodo para boton borrar
def borrar():
    if D.borrar(palabra.get()):
        responder("borrado")
    else: 
        responder("no existe")

#metodo para boton cambiar
def cambiar():
    if D.cambiar(palabra.get(),significado.get()):
        responder("cambiado")
    else: 
        responder("no existe")

#metodo para boton grabar
def grabar():
    D.grabar("diccionario.txt")
    responder("grabado")

#método para mostrar mensaje de respuesta    
def responder(x):
    respuesta.config(text=x)

# Creamos la interfaz
v=Tk()
f1=Frame(v)
f2=Frame(v) 
f3=Frame(v)

Label(f1,text="palabra:").pack(side=LEFT)
palabra=Entry(f1)
palabra.pack()

Label(f2,text="significado:").pack(side=LEFT)
significado=Entry(f2)
significado.pack()

Button(f3,text="buscar",command=buscar).pack(side=LEFT)
Button(f3,text="agregar",command=agregar).pack(side=LEFT)
Button(f3,text="borrar",command=borrar).pack(side=LEFT)
Button(f3,text="cambiar",command=cambiar).pack(side=LEFT)
Button(f3,text="grabar",command=grabar).pack()

respuesta=Label(v)

f1.pack(); f2.pack(); f3.pack(); respuesta.pack()

# Iniciamos procesamiento de eventos
v.mainloop()
