
#distancia: num num num num -> float 
#distancia entre puntos (x0,y0) y (x1,y1) 
#ej: distancia(1,0,4,0) debe ser 3.0
def distancia(x0,y0,x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    return (dx**2 + dy**2)**0.5

#Tests
assert distancia(1,0,4,0)==3.0

#resultado con 4 decimales de precisión 
assert abs(distancia(0,1,1,0)-1.4142)< 0.0001


# cerca: num num num -> bool
# retorna True si x es igual a y con
# precision epsilon
def cerca(x, y, epsilon):
    diff = x - y
    return abs(diff) < epsilon


