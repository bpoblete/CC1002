from tkinter import *

#metodo que se ejecuta en caso de ingresar un nombre
def saludar():
  respuesta.bind("<Return>",saludarEspanol)
  pregunta.config(text="Cual es tu nombre?")
  
def saludarEspanol(x):
  r=respuesta.get()  #obtener respuesta
  saludo.config(text="hola "+r)

def greet():
  respuesta.bind("<Return>",greetEnglish)
  pregunta.config(text="What is your name?")

def greetEnglish(x):
  r=respuesta.get()  #obtener respuesta
  saludo.config(text="hello "+r)
    
#programa que saluda
ventana = Tk()

marco1=Frame(ventana)
marco1.pack()

#boton "espanol", al hacer click ejecuta saludar()
boton1 = Button(marco1,text="espanol",command=saludar)
boton1.pack(side=LEFT)  #ubica boton en la ventana
#boton "english", al hacer click ejecuta greet()
boton2 = Button(marco1,text="english",command=greet)
boton2.pack()  #ubica boton en la ventana

marco2=Frame(ventana)
marco2.pack()

pregunta = Label(marco2)
pregunta.pack(side=LEFT)

#componente para ingresar nombre
respuesta = Entry(marco2)
respuesta.pack()

#componente para mostrar saludo
saludo=Label(ventana)
saludo.pack()
ventana.mainloop()
    
