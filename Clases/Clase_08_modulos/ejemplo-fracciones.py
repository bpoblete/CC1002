from fracciones import *

# pruebaSuma: none -> none
# procedimiento para usar en el programa principal
# pide numerador y denominador de dos funciones y después la suma y muestra en pantalla
def pruebaSuma():
    print("suma de fracciones a/b y c/d")
    
    a=int(input("a?"))   # Ojo, si hacen a = input("a?"), denominador sera str pero debiera ser int  
    b=int(input("b?"))
    f1=fraccion(a,b)
    
    f2=fraccion(int(input("c?")),int(input("d?")))
    f3=sumaFracciones(f1,f2)

    f3simplificada = simplificaFracciones(f3)
    print("suma=" + aString(f3))
    print("suma (simplificada)=" + aString(f3simplificada))

# Programa principal ejemplo de uso de fracciones
pruebaSuma()
