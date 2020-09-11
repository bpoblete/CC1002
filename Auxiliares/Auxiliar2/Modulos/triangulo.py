import math

# esTriangulo int int int -> bool
# Verifica que la combinacion de tres valore
# Pueden formar un triangulo
# Ejemplo: esTriangulo(2,3,5) entrega True
def esTriangulo(lado1,lado2,lado3):

    if (lado1+lado2 > lado3) and (lado1+lado3 > lado2) and (lado2+lado3 > lado1):
        return True

    else:
        return False

# Test
assert esTriangulo(2,3,4)
assert not esTriangulo(8,1,2)

# perimetroTriangulo: int int int -> int
# Entrega el perimetro de un triangulo dado sus 3 lados
# Ejemplo: perimetroTriangulo(2,2,2) entrega 6
def perimetroTriangulo(lado1,lado2,lado3):

    return lado1+lado2+lado3

# Test
assert perimetroTriangulo(2,2,2) == 6
assert perimetroTriangulo(3,6,9) == 18

# areaTriangulo: int int int -> float
# Entrega el area del triangulo dado sus 3 lados
# Ejemplo areaTriangulo(1,1,math.sqrt(2)) entrega 0.5 aprox
def areaTriangulo(lado1,lado2,lado3):

    #calculo del semiperimetro
    semiPerimetro = perimetroTriangulo(lado1,lado2,lado3)/2

    #calcilando el area por el teorema de Heron

    area =(semiPerimetro*(semiPerimetro-lado1)*(semiPerimetro-lado2)*(semiPerimetro-lado3))**(1/2)
    return area

# Test
assert  0.49 <= areaTriangulo(1,1,math.sqrt(2)) <= 0.5
assert 2.9 <= areaTriangulo(2,3,4) <= 3.0


