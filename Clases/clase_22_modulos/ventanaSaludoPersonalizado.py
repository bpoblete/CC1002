from tkinter import *
#metodo que se ejecuta en caso de ingresar un nombre
def saludar(x):
  r=respuesta.get()  #obtener respuesta
  saludo.config(text="hola "+r)
    
#programa que saluda
ventana = Tk()
pregunta = Label(ventana,text="Cual es tu nombre?")
pregunta.pack()

#componente para ingresar nombre
respuesta = Entry(ventana)
respuesta.pack()
respuesta.bind("<Return>",saludar)

#componente para mostrar saludo
saludo=Label(ventana)
saludo.pack()
ventana.mainloop()
    
