# -*- coding: utf-8 -*-
# (Nota: La línea anterior es para poder usar acentos en el código. Déjenla tal cual.)
#
###############
# Módulo Fracciones
###############


import estructura
# Diseno de la estructura
# fraccion: numerador (int) denominador(int)
estructura.crear("fraccion", "numerador denominador")

# sumaFracciones: fraccion fraccion -> fraccion
# crear una nueva fraccion que corresponda a la suma de dos fracciones f1 y f2
# Ejemplo: sumaFracciones(fraccion(1,2), fraccion(3,4))
# devuelve fraccion(10,8)
def sumaFracciones(f1,f2):
    assert type(f1) == fraccion and type(f2)== fraccion
    assert f1.denominador != 0 and f2.denominador != 0
    
    num = f1.numerador*f2.denominador + f2.numerador*f1.denominador
    den = f1.denominador*f2.denominador
    return fraccion(num,den)

# Test
f12=fraccion(1,2)
f34=fraccion(3,4)
assert sumaFracciones(f12,f34) == fraccion(10,8)

# restaFracciones: fraccion fraccion -> fraccion
# resta dos fracciones y retorna otra fraccion con el resultado
# Ejemplo: restaFracciones(fraccion(1,2), fraccion(3,6))
# devuelve fraccion(-2,8)
def restaFracciones(f1,f2):
    assert type(f1)==fraccion and type(f2)==fraccion
    assert f1.denominador != 0 and f2.denominador !=0
    num = f1.numerador*f2.denominador - f1.denominador*f2.numerador
    den = f1.denominador * f2.denominador
    return fraccion(num,den)

# Test
f12=fraccion(1,2)
f34=fraccion(3,4)
assert restaFracciones(f12,f34) == fraccion(-2,8)

import math

# simplificaFracciones: fraccion -> fraccion
# entrega una fraccion nueva que es la version simplificada de f
# Ejemplo: simplificaFracciones(fraccion(10,30)) -> fraccion(1,3)
def simplificaFracciones(f):
    m = math.gcd(f.numerador,f.denominador)
    return fraccion(int(f.numerador/m), int(f.denominador/m))

# Test
assert simplificaFracciones(fraccion(10,30)) == fraccion(1,3)

# igualdadFracciones: fraccion fraccion -> bool
# Indica si las fracciones f1 y f2 son iguales (equivalentes)
# Ejemplo: igualdadFracciones(fraccion(1,2), fraccion(3,6))
# devuelve True
def igualdadFracciones(f1,f2):
    return simplificaFracciones(f1) == simplificaFracciones(f2) 

# Test
f12=fraccion(1,2)
f36=fraccion(3,6)
assert igualdadFracciones(f12,f36)

# aString: fraccion -> str
# Entrega un string que representa una fracción
# Ejemplo: aString(fraccion(1,2)) retorna "1/2"
def aString(f):
    return str(f.numerador)+"/"+str(f.denominador)

# Tests
assert aString(fraccion(1,2)) == "1/2"


