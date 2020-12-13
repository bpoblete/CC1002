from tkinter import *
ventana=Tk()
# objeto canvas para dibujar
ancho=200; alto=100 #pixeles
cv=Canvas(ventana,width=ancho,height=alto)
cv.pack()
#dibujar diagonales (azul y roja)
#cv.create_line(h1,v1,h2,v2,fill="color")
cv.create_line(0,0,ancho,alto,fill="blue")
cv.create_line(0,alto,ancho,0,fill="red")
ventana.mainloop()
