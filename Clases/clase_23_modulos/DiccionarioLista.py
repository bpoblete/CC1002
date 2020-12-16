
# coding: utf-8

# Clase Diccionario
# 
# Solución utilizando listas (**list**) de Python

import estructura

# Estructura que almacena una palabra con su significado
# registro: palabra (str) significado (str)
estructura.mutable("registro","palabra significado")

# Clase Diccionario
# Almacena registros de palabras con su significado
# Campos:
#    __D: list (registro)
class Diccionario:
    # __init__ : str -> list(registro)
    #crea diccionario con palabras en archivo x
    #ejs: D=Diccionario("diccionario.txt")
    def __init__(self,x):
        assert type(x)==str 
        self.__D=[] #list()
        f=open(x)
        for linea in f:
            i=linea.index(".")
            reg=registro(linea[0:i],linea[i+1:-1])
            self.__D.append(reg)
        f.close()


    #buscar : str -> str
    def buscar(self,palabra):
        i=self.indice(palabra,self.__D)
        if i<0: 
            return None
        else:
            return self.__D[i].significado

    #cambiar : str str -> bool
    def cambiar(self,palabra,significado):
        i=self.indice(palabra,self.__D)
        if i<0: 
            return False
        else:
            self.__D[i].significado = significado
            return True


    # borrar : str -> bool
    def borrar(self,palabra):
        i=self.indice(palabra,self.__D)
        if i<0: 
            return False
        else:
            self.__D.pop(i)
        return True


    #indice: str list(registro) -> int
    #indice de primer x en L (-1 si no está)
    #L: lista ordenada y sin repeticiones
    #ej:indice(‘b’,[registro(‘a’,1),registro(‘b’,2)])==1
    def indice(self,palabra,L):
        ip=0; 
        iu=len(L)-1
        while ip<=iu:
            im=(ip+iu)//2
            if L[im].palabra == palabra: 
                return im
            if L[im].palabra<palabra:
                ip=im+1
            else:
                iu=im-1
        return -1 #no está

    #agregar : str str -> bool
    def agregar(self,palabra,significado):
        reg=registro(palabra,significado)
        for i in range(len(self.__D)):
            if self.__D[i].palabra == palabra:
                return False
            if self.__D[i].palabra > palabra:
                #insertar en índice i
                self.__D.insert(i,reg)
                return True
        #agregar al final de la lista
        self.__D.append(reg)
        return True

    # grabar: str -> None
    # efecto: graba diccionario en el archivo indicado, una palabra y significado por línea
    def grabar(self,archivo):
        assert type(archivo)==str 
        f=open(archivo,"w")
        for registro in self.__D:
            linea = registro.palabra+"."+registro.significado
            f.write(linea+"\n")
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

# Programa Principal de Prueba
# ES OPCIONAL: Lo agregamos acá para entender la clase diccionario SIN usar ventanas
if __name__ == "__main__":

    midiccionario = Diccionario("D.txt")

    print("Mini ejemplo de uso de clase diccionario")

    while (True):

        print ("Posibles operaciones:")
        print ("'A': Agregar palabra, 'B': Buscar palabra, 'C': Cambiar significado,\
               'E': Eliminar palabra, 'G': Grabar diccionario en archivo, 'F': fin")    
        
        operacion = input("Ingrese operación? ")
        if operacion == 'F':
            break

        elif operacion == "A":
            # Diálogo para agregar una palabra
            palabra = input("Ingrese palabra a agregar? ")
            significadoActual = midiccionario.buscar(palabra)
            if significadoActual != None: 
                print ("La palabra existe. Si desea puede cambiar su significado.")
                continue
            significado = input("Ingrese significado? ")
            ok = midiccionario.agregar(palabra,significado)
            if ok:
                print ("Palabra y significado agregados a diccionario.")
            else:
                print ("Error al agregar.")

        elif operacion == "B":
            # Diálogo para buscar una palabra
            palabra = input("Ingrese palabra a buscar? ")
            significado = midiccionario.buscar(palabra)
            if significado == None:
                print("La palabra ", palabra, "no está en el diccionario.")
            else:
                print(palabra, ":", significado)

        elif operacion == "C":
            # Diálogo para cambiar una palabra
            palabra = input("Ingrese palabra a cambiar su significado? ")
            significadoActual = midiccionario.buscar(palabra)
            if significadoActual == None: 
                print ("La palabra NO existe. Si desea puede agregarla y así indicar su significado.")
                continue
            print ("Significado actual: ", palabra, ": ", significado)
            significado = input("Ingrese nuevo significado? ")
            ok = midiccionario.cambiar(palabra,significado)
            if ok:
                print ("Palabra y significado cambiados en diccionario.")
            else:
                print ("Error al cambiar.")

        elif operacion == "E":
            # Diálogo para eliminar una palabra
            palabra = input("Ingrese palabra a eliminar en Diccionario? ")
            significadoActual = midiccionario.buscar(palabra)
            if significadoActual == None: 
                print ("La palabra NO existe.")
                continue
            ok = midiccionario.borrar(palabra)
            if ok:
                print ("Palabra eliminada del diccionario.")
            else:
                print ("Error al eliminar.")

        elif operacion == 'G':
            # Diálogo para grabar el diccionario a un archivo
            archivo = input("Ingrese nombre del archivo donde grabar el diccionario?")
            midiccionario.grabar(archivo)
            print ("Diccionario grabado.")
        else:
            print("Opción no exite.")

