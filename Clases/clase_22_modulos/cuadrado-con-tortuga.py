#dibujar con Tortuga
from tkinter import *
from Tortuga import *

def dibujar():
    #ubicar tortuga al centro de cv
    t=Tortuga(ancho/2,alto/2,cv)
    #girar la tortuga en angulo alfa
    t.girar(45)
    #repetir 4 veces
    for i in range(4):
        #avanzar tortuga en L(dibujando linea)
        t.avanzar(50)
        #girar tortuga en 90º
        t.girar(90)

v=Tk()
b=Button(v,text="cuadrado",command=dibujar)
alto=400
ancho=400
cv=Canvas(v,width=ancho,height=alto) 
b.pack()
cv.pack()

            

v.mainloop()

