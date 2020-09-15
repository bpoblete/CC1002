#suma: int int -> int
#Calcula x + (x+1) + ... + y
#ej: suma(3,5) debe ser 12
def suma(x,y):
    assert (type(x)==int) and (type(y)==int) 
    if x>y: 
        return 0
    else:
        return suma(x,y-1) + y 

assert suma(3,5)==12 #caso general 
assert suma(3,3)==3  #caso especial 
assert suma(5,3)==0  #caso base

# fibonacci: int -> int
# calcula el n-esimo numero de la sucession de Fibonacci
# ejemplo: fibonacci(7) debe dar 13
def fibonacci(n):
    assert type(n)==int and n>=0
    if n<2:
        # caso base
        return n
    else:
        # caso recursivo
        return fibonacci(n-1) + fibonacci(n-2)

# test:
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(7) == 13

#repetir: str int -> str
#string x repetido n veces
#ej: repetir("ja",3) debe ser "jajaja“
def repetir(x,n):
    assert type(x)==str and type(n)==int and n>=0 
    if n==0: 
        return ""
    else:
        return x + repetir(x,n-1)

assert repetir("ja",3)=="jajaja" #caso general
assert repetir("ja",0)==""       #caso base
assert repetir("ja",1)=="ja"     #caso especial
