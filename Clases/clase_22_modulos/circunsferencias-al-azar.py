#circunferencias al azar
from tkinter import *
import random 
def dibujar():
    x=random.randint(0,ancho)
    y=random.randint(0,alto)
    r=random.randint(1,min(alto,ancho))/2
    cv.create_oval(x-r,y-r,x+r,y+r)

v=Tk()
b=Button(v,text="circunferencia",command=dibujar)
alto=200
ancho=200
cv=Canvas(v,width=ancho,height=alto) 
b.pack()
cv.pack()
v.mainloop()

