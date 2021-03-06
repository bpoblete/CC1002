
# coding: utf-8

# Clase Diccionario
# Campos:
# __D : dict de items palabra(str):significado(str)
class Diccionario:
    
    # __init__ : None -> dict
    #crea diccionario con palabras en archivo x
    #ej: D=Diccionario("diccionario.txt")
    def __init__(self,x):
        assert type(x)==str
        self.__D={} #dict()
        f=open(x)
        for linea in f:
            i=linea.index(".")
            palabra=linea[0:i]
            significado=linea[i+1:-1]
            self.__D[palabra] = significado
        f.close()

    #buscar: str -> str
    #entrega significado de palabra x 
    #None si x no está
    #ej: D.buscar(x)
    def buscar(self,x):
        if x in self.__D: 
            return self.__D[x]
        else: 
            return None

    #agregar: str str -> bool
    #agrega palabra x con significado y 
    #True si ok y False si x ya existe
    #ej: D.agregar(x,y)
    def agregar(self,x,y):
        if x in self.__D:
            return False
        else:
            self.__D[x]=y 
            return True

        
    #borrar: str -> bool
    #borra palabra x 
    #True si ok y False si x no existe
    #ej: D.borrar(x)
    def borrar(self,x):
        if x in self.__D:
            del self.__D[x]
            return True
        else: 
            return False

        
    #cambiar: str str -> bool
    #y a significado de palabra x 
    #True si ok y False si x no existe
    #ej: D.cambiar(x,y)
    def cambiar(self,x,y):
        if x in self.__D: 
            self.__D[x]=y
            return True
        else:
            return False


    #grabar: str -> None
    #graba diccionario en archivo de nombre x
    #ej: D.grabar("diccionario.txt")
    def grabar(self,x):
        f=open(x,"w")
        for palabra in self.__D:
            significado=self.__D[palabra] 
            f.write(palabra+"."+significado+"\n")
        f.close() 



# Test diccionario

class TestDiccionario:
    def __init__(self):  
        a=open("D.txt","w")
        a.write("hola.hi\n")
        a.close()
        self.__D=Diccionario("D.txt")
    
    def test(self):
        assert self.__D.buscar("hola")=="hi"
        assert self.__D.cambiar("hola","hello")
        assert self.__D.buscar("hola")=="hello"
        assert self.__D.borrar("hola")
        assert self.__D.buscar("hola")==None
        assert self.__D.agregar("hola","hi")
        assert self.__D.buscar("hola")=="hi"
        self.__D.grabar("D.txt")
    
        for l in open("D.txt"): 
            assert l=="hola.hi\n" 

TestDiccionario().test()    

