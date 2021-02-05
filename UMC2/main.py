#UMC 2


#actividad 1
def hms_seg(hour, minutes, second):
    return hour*3600 + minutes*60 + second


def seg_hms(seconds):
    my_seconds = seconds
    hour = my_seconds//3600
    my_seconds = my_seconds%3600
    minutes = my_seconds//60
    my_seconds = my_seconds%60
    return hour, minutes, my_seconds


#actividad 2
def suma_horas():
    print("Sumaremos 2 horas:")

    print("Hora 1: ")
    hora1 = int(input("horas: "))
    minutos1 = int(input("minutos: "))
    segundos1 = int(input("segundos: "))

    print("Hora 2: ")
    hora2 = int(input("horas: "))
    minutos2 = int(input("minutos: "))
    segundos2 = int(input("segundos: "))

    suma_total = hms_seg(hora1,minutos1,segundos1)+hms_seg(hora2,minutos2,segundos2)
    return seg_hms(suma_total)


#actividad 3
def suma2mayores(n1, n2, n3, n4):
    numeros = [n1, n2, n3, n4]
    max1 = numeros[0]
    for numero in numeros:
        if numero > max1:
            max1 = numero
    numeros.remove(max1)
    max2 = numeros[0]
    for numero in numeros:
        if numero > max2:
            max2 = numero
    return max1 + max2


#actividad 4 area de un triangulo en vase a sus puntos

def norma_vector(x, y):
    return x**2 + y**2

def resta_vectores(x1, y1, x2, y2):
    return (x1-x2), (y1-y2)

def distancia_vertores(x1, y1, x2, y2):
    return norma_vector(resta_vectores(x1, y1, x2, y2))

def verctor_unitario(x1, y1):
    norma = norma_vector(x1, y1)
    return (x1/norma), (y1/norma)

def proyección(x, y, dx, dy, cx, cy):
    px, py = resta_vectores(x, y, cx, cy)
    p11 = dx * dx
    p12 = dx * dy
    p21 = p12
    p22 = dy * dy
    rx = p11 * px + p12 * py
    ry = p21 * px + p22 * py
    rx += cx
    ry += cy
    return (rx, ry)

def area_triangulo(b, h):
    return b*h/2

def area_proyeccion(x1, y1, x2, y2, x3, y3):
    base = distancia_vertores(x1, y1, x3, y3)
    (dx, dy) = verctor_unitario(x1, y1, x3, y3)
    (px, py) = proyección(x2, y2, dx, dy, x3, y3)
    altura = distancia_vertores(x2, y2, px, py)
    return area_triangulo(base, altura)