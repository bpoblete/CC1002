# potencia: num int -> num
# calcula el valor de una potencia de base elevado a exponente
# para exponentes enteros positivos
# ejemplo: potencia (4,5) debe dar 1024
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base*(potencia(base, exponente-1))

# test
assert potencia(4,5) == 1024
assert potencia(2,4) == 16
assert potencia(-1,5) == -1
assert potencia(3,0) == 1



#digitos: int->int
#cuenta digitos de un número entero 
#ej: dígitos(245) debe ser 3
#ej: digitos(4) debe ser 1
def digitos(n):
    if abs(n) < 10 :
        return 1
    else:
        return 1 + digitos(n//10)
# tests
assert digitos(245)==3
assert digitos(-4)==1

digitos(-2456)


# factorial: int -> int
# calcula el valor factorial de n
# ejemplo: factorial(4) debe dar 24
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 
    

# test
assert factorial(4) == 24
assert factorial(2) == 2
assert factorial(8) == 40320


# factorial: int -> int
# calcula el valor factorial de n
# ejemplo: factorial(4) debe dar 24
def factorial(n):
    assert (type(n)==int) and (n>=0), "Factorial no esta definido para n no entero, ni n negativo." 
    if n == 0:
        return 1
    else:
        return n*(factorial(n-1))

# test
assert factorial(4) == 24
assert factorial(2) == 2
assert factorial(8) == 40320


#calculaListaFactoriales: None -> None
#calcular factorial de lista de numeros ingresada por el teclado
#  (la lista termina con el valor "fin")
#ej: factoriales()  

def calculaListaFactoriales():
    respuesta=input('n ?')
    if respuesta=="fin":
      return 

    # caso no es igual a fin
    n = int(respuesta)
    factorial_n = factorial(n)
    print(str(n)+'!='+str(factorial_n))
    calculaListaFactoriales()




# hanoi: int -> int
# calcula el numero de movimientos necesarios para mover 
# una torre de n discos desde una vara a otra
# usando 3 varas y siguiendo las restricciones del puzzle de hanoi
# ejemplo: hanoi(0) debe dar 0, hanoi(1) debe dar 1, hanoi(2) debe dar 3
def hanoi(n):   
    if n<2:
        return n
    else:
        return 1+2*hanoi(n-1)
# test
assert hanoi(0)==0
assert hanoi(1)==1
assert hanoi(2)==3
assert hanoi(4)==15
assert hanoi(5)==31



# Programa principal
# Usa funciones definidas arriba

print("potencia(-2,7) es ",str(potencia(-2,7)))


print("factorial de 0 es ",str(factorial(0)))
print("factorial de 10 es ",str(factorial(10)))

# Descomentar lo siguiente si quieren probar el assert dentro de la funcion factorial
#print("El factorial de -1 es... (lo siguiente debe dar error!)... ")
#print(str(factorial(1)))

print("El factorial de 4 es ",str(factorial(4)))
      
print ("Calcular lista de factoriales")
calculaListaFactoriales()

print("hanoi(4) es ",str(hanoi(4)))



