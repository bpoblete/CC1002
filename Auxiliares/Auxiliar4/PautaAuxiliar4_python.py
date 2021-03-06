# -*- coding: utf-8 -*-
"""Pauta Auxilliar 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KKShhTKLPstAYBZl2LX3nTwIRhv-zkCb

#Auxiliar 4 - Recurrencia 

P1. Un niño está aburrido en su casa, por lo que comienza a sumar los dígitos de los número hasta llegar a un solo dígito. Viendo los resultados que obtiene le surge una duda, ¿qué tan frecuente es obtener uno de estos dígitos?. Su trabajo es resolver esta duda, para eso siga los siguientes pasos: 
 
i) Modifique la función sumaDigitos(n), vista en la auxiliar pasada, para que entregue un único dígito

ii) Cree la función contarFrecuenciasDigito(d,N) que dado un dígito d y un natural N, retorne la cantidad de números entre 0 y N, cuya suma de dígitos corresponda a d . Ejemplo: contarFrecuenciasDigito(1,100) = 12 , ya que tenemos los numeros 100, 91, 82, 73, 64, 55, 46, 37, 28, 19, 10 y 1. Al sumar los dígitos de cada uno de ellos nos va a entregar el valor 1. 

iii) Finalmente cree un programa que le solicite el dígito y un natural y le entregue la frecuencia con la que aparece el dígito entre el 0 y el natural ingresado. El programa debe preguntar si quiere volver a consultar y reiniciarse en el caso de que sí.  Para esto, use las funciones definidas anteriormente. 
 

```
Ejemplo: 
  Ingrese el dígito cuya frecuencia busca: 1
  Ingrese hasta que número se debe revisar: 100
  El dígito 1 se repite 12 veces
  ¿Volver a calcular? [s/n]: s
  Ingrese el dígito cuya frecuencia busca: 0
  Ingrese hasta que número se debe revisar: 100
  El dígito 0 se repite 1 vez 
  ¿Volver a calcular? [s/n]: n
```
"""

#sumaDigitos(n): int -> int 
#Suma los digitos de un numero hasta obtener un numero de un solo digito 
#sumaDigitos(12345) = 6

def sumaDigitos(n,sumaActual=0):
  if n<10:
    sumaActual+=n
    if sumaActual<10:
      return sumaActual
    else: return sumaDigitos(sumaActual)
  else: 
    sumaActual+=n%10
    return sumaDigitos(n//10,sumaActual)

assert sumaDigitos(12345) == 6
assert sumaDigitos(46832938744) == 4
assert sumaDigitos(12) == 3

#contarFrecuenciaDigito: int int -> int 
#Cuenta las frecuencia que aprece el dígito al sumar los digitos de los numeros desde el 0 al N entregado 
#ej: contarFrecuenciaDigito(1,100) == 12
def contarFrecuenciaDigito(d,N,frecuencia=0):
  if N==0:
    if d == 0: return frecuencia + 1
    else: return frecuencia
  else: 
    digito = sumaDigitos(N)
    if digito==d:
      return contarFrecuenciaDigito(d,N-1,frecuencia+1)
    else:
      return contarFrecuenciaDigito(d,N-1,frecuencia)

assert contarFrecuenciaDigito(1,100) == 12
assert contarFrecuenciaDigito(0,100) == 1
assert contarFrecuenciaDigito(5,120) == 13



def programa(): 
  d = int(input('Ingrese el dígito cuya frecuencia busca: '))
  N = int(input('Ingrese hasta que número se debe revisar: '))
  frecuencia = contarFrecuenciaDigito(d,N)
  if frecuencia == 1:
    print('El dígito ',d,' se repite ',frecuencia,'vez')
  else: 
    print('El dígito ',d,' se repite ',frecuencia,'veces')
    
  respuesta = input('¿Volver a calcular?  [s/n]: ')
  if respuesta=='s':
    return programa()

programa()

"""P2. Escriba la función sumaProductos(x,y) que reciba dos enteros positivos y entregue la suma de los productos de sus dígitos. 
```
Ejemplo: sumaProductos(12345,6789)=110
```

Lo que corresponde a 5x9 + 4x8 + 3x7 + 2x6 + 1x0 = 45 + 32 + 21 + 12 + 0 = 110
"""

# sumaProductos: int int -> int 
# Multiplica los digitos de los numeros entregados y los suma
# ej: sumaProductos(12345,6789) = 110

def sumaProductos(x,y):
  if x==0 and y==0:
    return 0
  else: 
    return ((x%10) * (y%10)) + sumaProductos(x//10,y//10)

assert sumaProductos(12345,6789) == 110
assert sumaProductos(93898,2) == 16
assert sumaProductos(12849,985) == 149