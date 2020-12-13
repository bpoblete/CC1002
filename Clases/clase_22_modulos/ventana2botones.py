from tkinter import *

#metodos que se ejecutan en caso de click en botones 
def saludar():
  saludo.config(text="hola")
def greet(): 
  saludo.config(text="hello")

#ventana
ventana = Tk()
#boton "espanol", al hacer click ejecuta saludar()
boton1 = Button(ventana,text="espanol",command=saludar)
boton1.pack()  #ubica boton en la ventana
#boton "english", al hacer click ejecuta greet()
boton2 = Button(ventana,text="english",command=greet)
boton2.pack()  #ubica boton en la ventana
#componente para mostrar saludo 
saludo= Label(ventana)
saludo.pack() #ubica Label debajo
#loop para clicks en botones (hasta cerrar ventana)
ventana.mainloop()
