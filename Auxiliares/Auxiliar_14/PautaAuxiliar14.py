from tkinter import *
import random

# Campos:
# intentos: int
# labels: list
# lista: list (opcional)
# copyLista: list (opcional)


class Juego():

    # Constructor
    def __init__(self, intentos, labels):
        self.intentos = intentos
        self.labels = labels  # ['A', 'B', 'C']

        self.lista = []

        # self.lista = ["A1", "B1", "C1", "A2"... "C3"]
        for i in range(len(self.labels)):
            for label in labels:
                self.lista.append(label + str(i+1))

        # Para saber que zonas ya estan excavadas
        self.copyLista = self.lista.copy()

        # Ubicación del tesoro
        self.tesoro = self.lista[random.randint(0, len(self.lista) - 1)]

    # inicio: None -> None
    # Configura los marcos y labels para el saludo y ejecutar jugadas
    def inicio(self, event):
        res = self.nombre.get()
        self.saludo.config(text="Hola " + res +
                           " bienvenido a la búsqueda del tesoro")
        self.saludo2.config(text="Tienes " + str(self.intentos) +
                            " oportunidades para encontrar el tesoro en la grilla de tamaño " + str(len(self.labels)) + "x" + str(len(self.labels)))
        self.saludo3.config(text="Mucha suerte y comencemos!")
        self.text_m3.config(text="Ingresa casilla donde quieras cavar")
        self.resp_m3.bind("<Return>", self.cavar)
        self.resp_m3.pack()

    # cavar: None -> None
    # Se encarga de la lógica del juego y de avisar al jugador las etapas
    def cavar(self, event):
        if self.intentos == 0:
            self.final.config(
                text="Ya no tienes mas intentos! Inicia otro juego")

        else:
            jugada = self.resp_m3.get()
            if jugada in self.lista:
                self.resultado.config(text="Cavaste en " + jugada)
                if jugada == self.tesoro:
                    self.veredicto.config(
                        text="Ganaste! Encontraste el tesoro")
                    self.final.config(text="")
                    self.intentos = 0
                else:
                    self.veredicto.config(text="No estaba ahí el tesoro")
                    self.lista.remove(jugada)
                    cell = self.cells[self.copyLista.index(jugada)]
                    cell.config(text="X")
                    self.intentos -= 1
                    if self.intentos == 0:
                        self.final.config(
                            text="Perdiste :(, te quedaste sin intentos. El tesoro estaba en " + str(self.tesoro))
                    else:
                        self.final.config(
                            text="Te quedan " + str(self.intentos) + " intentos")
            else:
                self.resultado.config(text="No puedes cavar ahí")
    # crearjuego: None -> None
    # Función crea el juego y se encarga de crear los objetos de la interfaz

    def crearJuego(self):
        self.ventana = Tk()
        self.marco = Frame(self.ventana)
        self.marco.pack()

        self.cells = []

        # self.labels = ["A", "B", "C"]

        for i in range(len(self.labels)):
            for j in range(len(self.labels)):
                cell = Label(self.marco, text=self.labels[j] + str(i+1))
                cell.grid(row=i, column=j)
                self.cells.append(cell)

        self.marco2 = Frame(self.ventana)
        self.marco2.pack()
        self.pregunta = Label(self.marco2, text="Ingreso su nombre")
        self.nombre = Entry(self.marco2)
        self.nombre.bind("<Return>", self.inicio)
        self.pregunta.pack(side=LEFT)
        self.nombre.pack()

        self.saludo = Label(self.ventana)
        self.saludo.pack()

        self.saludo2 = Label(self.ventana)
        self.saludo2.pack()

        self.saludo3 = Label(self.ventana)
        self.saludo3.pack()

        self.marco3 = Frame(self.ventana)
        self.marco3.pack()

        self.text_m3 = Label(self.marco3)
        self.text_m3.pack(side=LEFT)

        self.resp_m3 = Entry(self.marco3)

        self.resultado = Label(self.ventana)
        self.resultado.pack()

        self.veredicto = Label(self.ventana)
        self.veredicto.pack()

        self.final = Label(self.ventana)
        self.final.pack()

        self.ventana.mainloop()


juego = Juego(3, ["A", "B", "C"])
juego.crearJuego()
