from Tkinter import *

ventana=Tk()
cv=Canvas(ventana,width=200,height=200)
cv.pack()
cv.create_oval(20,40,100,100)
cv.create_oval(100,100,200,200,fill="black")
ventana.mainloop()
