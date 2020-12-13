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
    
#saludador bilingue
ventana = Tk()

pregunta = Label(ventana,text="Seleccione idioma")
#boton "espanol", al hacer click ejecuta saludar()
boton1 = Button(ventana,text="espanol",command=saludar)
boton1.pack()  #ubica boton en la ventana
#boton "english", al hacer click ejecuta greet()
boton2 = Button(ventana,text="english",command=greet)
boton2.pack()  #ubica boton en la ventana
pregunta.pack()

#componente para ingresar nombre
respuesta = Entry(ventana)
respuesta.pack()

#componente para mostrar saludo
saludo=Label(ventana)
saludo.pack()
ventana.mainloop()
    
