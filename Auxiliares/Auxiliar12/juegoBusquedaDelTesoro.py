from tkinter import *
import random

# La busqueda del Tesoro
# Este juego consiste en ir excavando zonas habilitadas para desenterrar el tesoro perdido, usted tendra una cantidad determinadas de intentos
# si utiliza todos sus intentos habra perdido el juego y la oportunidad de llevarse el tesoro a casa


# Campos:
# intentos : int
# labels : list
class Juego():

    # constructor de la clase
    def __init__(self, intentos=0, labels=[]):
        self.intentos = intentos
        self.labels = labels
        self._lista = [] # usada para almacenar las posibles zonas a excavar
        for i in range(len(self.labels)):
            for label in labels:
                self._lista.append(label + str(i+1))
        self._copyLista = self._lista.copy() # usada para actualizar las zonas ya excavadas
        self._tesoro = self._lista[random.randint(0,len(self._lista)-1)] # ubicacion del tesoro en una de las zonas a excavar


    # metodo privado que se ejecuta luego de que el jugador ingresa su nombre
    # se encarga de darle la bienvenida al jugador y cargar una nueva casilla donde pueda ingresar su jugada
    def _inicio(self,event):
        res = self._nombre.get()
        self._saludo.config(text="Hola " + res + " bienvenido a la búsqueda del tesoro")
        self._saludo2.config(text="Tienes " +str(self.intentos) +" oportunidades para encontrar el tesoro en estra grilla de " + str(len(self.labels)) + "x" + str(len(self.labels)))
        self._saludo3.config(text="Mucha suerte! y comencemos!")
        self._text_m3.config(text="Ingresa casilla donde quieras cavar")
        self._resp_m3.bind("<Return>", self._cavar)
        self._resp_m3.pack()


    # metodo privado que se ejecuta luego que el jugador realiza una jugada
    # se encarga de verificar si se encuentra el tesoro, si se ha perdido o si puede seguir jugando
    def _cavar(self,event):
        if self.intentos == 0: # en caso de quedarse sin intentos por haber perdido o por haber ganado
            self._final.config(text="Ya no tienes más intentos! inicia otro juego")
        else:
            r = self._resp_m3.get()
            if r in self._lista: # es una zona habilitada para cavar
                self._resultado.config(text="Cavaste en " + r)
                if r == self._tesoro: # si encuentra el tesoro
                    self._veredicto.config(text="GANASTE!! ENCONTRASTE EL TESORO")
                    self._final.config(text="")
                    self.intentos = 0 # ya que gano, quitamos todos los intentos restantes para que no pueda seguir jugando el mismo juego
                else: # si no encuentra el tesoro
                    self._veredicto.config(text="No estaba ahí!")
                    self._lista.remove(r)
                    cell = self._cells[self._copyLista.index(r)]
                    cell.config(text="X")
                    self.intentos -= 1
                    if self.intentos == 0: # pierde la partida
                        self._final.config(text="Perdiste :( Te has quedado sin intentos!, el tesoro estaba en: " + self._tesoro)
                    else:
                        self._final.config(text="Te quedan " + str(self.intentos) + ". Prueba otra vez")
            else: # zona no existente o previamente cavada
                self._resultado.config(text="Cavaste donde no podias!")


    # crearJuego: None -> None
    # Funcion encargada de crear la partida y la ventana de juego
    def crearJuego(self):
        self._ventana = Tk()
        self._marco = Frame(self._ventana)
        self._marco.pack()
        self._cells = [] # servira para almacenar los componentes de la grilla de busqueda y asi poder actualizar su texto luego de ser excavado
        for i in range(len(self.labels)):
            for j in range(len(self.labels)):
                cell = Label(self._marco, text=self.labels[j] + str(i+1))
                cell.grid(row=i, column=j)
                self._cells.append(cell)

        self._marco2 = Frame(self._ventana)
        self._marco2.pack()
        self._pregunta = Label(self._marco2, text="Ingrese su nombre")
        self._pregunta.pack(side=LEFT)
        self._nombre = Entry(self._marco2)
        self._nombre.bind("<Return>", self._inicio)
        self._nombre.pack()
        self._saludo = Label(self._ventana)
        self._saludo.pack()
        self._saludo2 = Label(self._ventana)
        self._saludo2.pack()
        self._saludo3 = Label(self._ventana)
        self._saludo3.pack()
        self._marco3 = Frame(self._ventana)
        self._marco3.pack()
        self._text_m3 = Label(self._marco3)
        self._text_m3.pack(side=LEFT)
        self._resp_m3 = Entry(self._marco3)
        self._resultado = Label(self._ventana)
        self._resultado.pack()
        self._veredicto = Label(self._ventana)
        self._veredicto.pack()
        self._final = Label(self._ventana)
        self._final.pack()
        self._ventana.mainloop()

# PARA JUGAR DESCOMENTE
# juego = Juego(intentos=3, labels=['A','B','C'])
# juego.crearJuego()
