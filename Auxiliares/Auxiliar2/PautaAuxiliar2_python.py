#Aux 2

# P1

# Importamos el modulo triangulo
import triangulo


# triangulo int int int -> bool
# Entrega el perimetro y area de un triangulo si los 3
# Lados pueden formar un triangulo
# Ejemplo: datosTriangulo(3,3,5)
def datosTriangulo(lado1,lado2,lado3):

  # Verificamos que sea un triangulo
  if triangulo.esTriangulo(lado1,lado2,lado3):

    # Calculamos su perimetro y area, entregando los dos
    perimetro = triangulo.perimetroTriangulo(lado1,lado2,lado3)
    area = triangulo.areaTriangulo(lado1,lado2,lado3)
    print("perimetro: " + str(perimetro))
    print("area: " + str(area))
    return True

  # Caso donde no es un triangulo
  else:

    print("no es un triangulo")
    return False

# Test
assert datosTriangulo(3,3,5)


#-------------------------------------------------------------
# P2

# diminutivo: int, int -> int
# Imprime en pantalla si a es diminutivo de b, en caso de no serlo indica cual digito
# No cumple con la condicion
# Ejemplo: diminutivo(123,456) debe imprimir correcto! y retornar un 1  

def diminutivo(a, b):

  # Sacamos cada digito de los numeros
  unidad_a = a % 10 
  decena_a =(a//10)%10
  centena_a =( a//100)%10 
  unidad_b = b % 10 
  decena_b =(b//10)%10
  centena_b =(b//100)%10

  # realizamos las comparaciones para unidad 
  if unidad_a >= unidad_b:
    print ('incorrecto!', unidad_a, 'es mayor o igual que', unidad_b) 
    return 0 

   # realizamos las comparaciones para decena 
  elif decena_a >= decena_b: 
    print ('incorrecto!' + str(decena_a) + 'es mayor o igual que' + str(decena_b)) 
    return 0 # finalmente comparamos la centena 

  elif centena_a >= centena_b:
    print ('incorrecto!' + str(centena_a) + 'es mayor o igual que' + str(centena_b))
    return 0 

  # Cumple la condicion de ser diminutivo 
  else:
    print ('correcto!') 
    return 1

# Test 
assert diminutivo(123, 333) == 0
assert diminutivo(123, 456) == 1
assert diminutivo(745, 689) == 0
assert diminutivo(444, 222) == 0


#--------------------------------------------------------------
# P3

#a)

import math


# distancia: float float float float -> float
# Calcula la distancia entre 2 puntos
# Ejemplo: distancia(0,0,0,5) debe entregar un 5
def distancia(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

assert distancia(0,0,0,5) == 5.0
assert distancia(5,4,5,1) == 3.0

# tiempo: float -> float
# Calcula la cantidad de minutos que demora en recorrer cierta distancia
# Ejemplo: tiempo(5.0) entrega 20
def tiempo(distancia):

  # Pasamos km/h a km/minutos
  velocidad = 15/60
  return distancia/velocidad

assert tiempo(5.0) == 20

#b)

# Pedimos las ubicaciones
ubicacion_x = input("Su ubicacion x? ")
ubicacion_y = input("Su ubicacion y? ")
amigo_x = input("Amigo x? ")
amigo_y = input("Amigo y? ")
abuela_x = input("Abuela x? ")
abuela_y = input("Abuela y? ")

# Calculamos cada distancia por separado
distancia_amigo = distancia(int(ubicacion_x), int(ubicacion_y), int(amigo_x), int(amigo_y))
distancia_abuela = distancia(int(ubicacion_x), int(ubicacion_y), int(abuela_x), int(abuela_y))

# Si el amigo se encuentra mas cerca
if distancia_amigo <= distancia_abuela:

  # Calculamos el tiempo que demora en ir donde el amigo
  tiempo_amigo = tiempo(distancia_amigo)
  print("Menor distancia: amigo")
  print("Tiempo:" + str(tiempo_amigo))
  if tiempo_amigo <= 30:
    print("Lo logra")
  else:
    print("No lo logra")

 # Si la abuela se encuentra mas cerca 
else:

  # Calculamos el tiempo que demora en ir donde la abuela
  tiempo_abuela = tiempo(distancia_abuela)
  print("Menor distancia: abuela")
  print("Tiempo:" + str(tiempo_abuela))
  if tiempo_abuela <= 30:
    print("Lo logra")
  else:
    print("No lo logra")
  

#---------------------------------------------------
# p4)
import random # Importamos el modulo random!!

# caracola: str -> str
# entrega una respuesta con un Si!, No! o No lo he entendido a las preguntas que 
# se le entregan
# Ejemplo: caracola("¿Pasare el ramo?") el 45% de la veces entrega un Si! como respuesta
def caracola(pregunta):
  # la idea es tomar un numero al azar del 1 al 100 y ver entre cuales numeros está 
  n=random.randint(1,100)

  # 45% responde un Si!
  if n>=1 and n<=45: 
    return "Si!" 

  # 35% responde un No!
  if n>45 and n<=75: 
    return "No!" 

  # El resto del 20% responde No lo he entendido
  else:
    return "No lo he entendido"

#Test
test = caracola("¿Soy cool?")
assert test == "Si!" or test == "No!" or test == "No lo he entendido"


pregunta = input("Cual es la pregunta:")
respuesta = caracola(pregunta)
print("Respuesta: " + respuesta )
