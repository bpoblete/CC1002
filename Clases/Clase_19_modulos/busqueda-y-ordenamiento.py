# -*- coding: utf-8 -*-
#Clase_19_Caso-de-Estudio-III_Busqueda-y-Ordenamiento_2020

# Busqueda Secuencial

# busquedaSecuencial: list(int) int -> int o None
# devuelve el indice de la lista donde se encuentra valor haciendo una
# busqueda secuencial, o devuelve None si no esta
# ejemplo: busquedaSecuencial([258, 45, 99, 14, 102, 75, 128], 14) devuelve 3
def busquedaSecuencial(lista, valor):
    for indice in range(len(lista)):
        if lista[indice] == valor:
            # se encontro el valor
            return indice
    # valor no fue encontrado
    return None

# Test
lista = [258, 45, 99, 14, 102, 75, 128]
assert busquedaSecuencial(lista, 14) == 3
assert busquedaSecuencial(lista, 20) == None

lista = [258, 45, 99, 14, 102, 75, 128]
busquedaSecuencial(lista, 102)

# Busqueda Binaria

# busquedaBinariaRec: list(int) int int int -> int o None
# devuelve el indice de la lista donde se encuentra valor haciendo una
# busqueda binaria en el rango [ip,iu], o devuelve None si no esta
# Requiere que la lista este ordenada ascendentemente
# ejemplo: busquedaBinariaRec([14, 45, 75, 99, 102, 128, 258], 45, 0, 6) devuelve 1
def busquedaBinariaRec(listaOrdenada, valor, ip, iu):
    # Caso base: valor no fue encontrado
    if ip > iu:
        return None
    im = (ip + iu) // 2 # indice del medio
    # Caso base: valor esta al medio de la lista
    if listaOrdenada[im] == valor:
        return im
    # Llamados recursivos
    elif valor < listaOrdenada[im]:
        return busquedaBinariaRec(listaOrdenada, valor, ip, im - 1)
    else: # valor > listaOrdenada[im]
        return busquedaBinariaRec(listaOrdenada, valor, im + 1, iu)

# busquedaBinaria: list(int) int -> int o None
# Hace la primera invocacion a busquedaBinariaRec
def busquedaBinaria(listaOrdenada, valor):
    return busquedaBinariaRec(listaOrdenada, valor, 0, len(listaOrdenada) - 1)

# Test
lista = [14, 45, 75, 99, 102, 128, 258]
assert busquedaBinaria(lista, 45) == 1
assert busquedaBinaria(lista, 20) == None

#listaOrdenada = [14, 45, 75, 99, 102, 128, 258]
#busquedaBinaria(lista, 102)


## Mergesort

# mezclarListas: list(in) list(in) -> list(any)
# Recibe dos listas de enteros, cada una de ellas ordenada
# y retorna una sola lista ordenada compuesta por los elementos de las dos listas.
def mezclarListas (L1, L2):
  assert type(L1)==list and type(L2)==list
  L = []
  while len(L1)>0 and len(L2)>0:
    if L1[0]<=L2[0]:
      primerElemento = L1.pop(0)
      L.append(primerElemento)
    else: # cao L2[0]<L1[0]
      primerElemento = L2.pop(0)
      L.append(primerElemento)
  # Al terminar el while una de las listas (L1 o L2) es vacia
  # Pero la otra podria NO ser vacia, hay que copiarla a L
  if len(L1)==0:
    L.extend(L2)
  else: # caso len(L1)==0
    L.extend(L1)
  return L

# Tests
L1 = [14, 16, 22, 22, 30, 44, 55]
L2 = [5, 7, 18, 22, 23, 25, 29]
L = [5, 7, 14, 16, 18, 22, 22, 22, 23, 25, 29, 30, 44, 55]
assert mezclarListas(L1,L2) == L

# mergesort: list(int) -> list(int)
# Ordena ascendemente la lista usando el algoritmo Mergesort
# ejemplo: mergesort([258, 45, 99, 14, 102, 75, 128]) retorna una nueva lista
# [14, 45, 75, 99, 102, 128, 258]
def mergesort(lista):
    assert type(lista)==list
    # Si la lista es de tamano 1 o 0, nada que hacer: ya esta ordenada!
    largo = len(lista)
    if largo<=1: 
      return lista 
    # Dividir en dos listas
    puntoMedio = largo//2
    listaIzq = lista[0:puntoMedio]
    listaDer = lista[puntoMedio:]
    listaIzqOrdenada = mergesort(listaIzq) 
    listaDerOrdenada = mergesort(listaDer)
    listaOrdenada = mezclarListas(listaIzqOrdenada,listaDerOrdenada)
    return listaOrdenada

# Test
lista = [258, 45, 99, 14, 102, 75, 128]
listaOrdenada = mergesort(lista)
assert listaOrdenada == [14, 45, 75, 99, 102, 128, 258]

# Ejemplo de uso
import random
L = []
for i in range(0,30):
  L.append(random.randint(1,100))
print("Lista L =",L)
print("Lista L ordenada =",mergesort(L))


# Bubblesort

# bubblesort: list(int) -> None
# efecto: ordena ascendemente la lista usando el algoritmo Bubblesort
# ejemplo: bubblesort([258, 45, 99, 14, 102, 75, 128]) modifica la lista
# y la deja en el estado [14, 45, 75, 99, 102, 128, 258]
def bubblesort(lista):
    k = len(lista)
    while k > 1:
        # hacer una pasada sobre lista[0], ..., lista[k - 1]
        for j in range(k-1):
            if lista[j] > lista[j + 1]:
                # intercambiar a[j] con a[j+1]
                # sintaxis para swap con listas de Python
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        # disminuir k
        k = k - 1

# Test
lista = [258, 45, 99, 14, 102, 75, 128]
bubblesort(lista)
assert lista == [14, 45, 75, 99, 102, 128, 258]

## Quicksort


import random

# particionar: list(int) int int -> int
# escoge aleatoriamente un pivote y devuelve la posicion donde queda el pivote
# luego de particionar la lista en el rango [ip,iu]
# efecto: deja todos los valores menores que el pivote a la izquierda de este
# y todos los valores mayores que el pivote a la derecha de este
# ejemplo: particionar([258, 45, 99, 14, 102, 75, 128], 0, 6) y el pivote es 99
# entonces la lista queda como [45, 14, 75, 99, 258, 102, 128] y devuelve 3
def particionar(lista, ip, iu):
    # Pre-condicion: ip < iu
    assert ip < iu
    # se escoge pivote aleatoriamente
    pivote = random.randint(ip, iu)
    # se intercambia con el primero del segmento de lista
    lista[ip], lista[pivote] = lista[pivote], lista[ip]
    # se particiona usando el pivote
    i = ip
    for j in range(ip + 1, iu + 1):
        if lista[j] < lista[ip]: # recordar que pivote esta en ip
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    # lista[i] contiene el ultimo valor que es menor que el pivote
    lista[ip], lista[i] = lista[i], lista[ip]
    return i

# Test
lista = [258, 45, 99, 14, 102, 75, 128]
pivote = particionar(lista, 0, 6)
for indice in range(0, pivote - 1):
    assert lista[indice] < lista[pivote]
for indice in range(pivote + 1, len(lista)):
    assert lista[indice] > lista[pivote]

# qsort: list(int) int int -> None
# efecto: ordena ascendemente la lista usando el algoritmo Quicksort
# en el rango [ip,iu]
# ejemplo: qsort([258, 45, 99, 14, 102, 75, 128], 0, 6) modifica la lista
# y la deja en el estado [14, 45, 75, 99, 102, 128, 258]
def qsort(lista, ip, iu):
    # si ip >= iu no se hace nada
    if ip < iu:
        pivote = particionar(lista, ip, iu)
        qsort(lista, ip, pivote - 1)
        qsort(lista, pivote + 1, iu)

# Test
lista = [258, 45, 99, 14, 102, 75, 128]
qsort(lista, 0, 6)
assert lista == [14, 45, 75, 99, 102, 128, 258]

# Quicksort

# quicksort: list(int) -> None
# efecto: ordena ascendemente la lista usando el algoritmo Quicksort
# ejemplo: quicksort([258, 45, 99, 14, 102, 75, 128]) modifica la lista
# y la deja en el estado [14, 45, 75, 99, 102, 128, 258]
def quicksort(lista):
    qsort(lista, 0, len(lista) - 1)

# Test
lista = [258, 45, 99, 14, 102, 75, 128]
quicksort(lista)
assert lista == [14, 45, 75, 99, 102, 128, 258]
lista = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
quicksort(lista)
assert lista == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
