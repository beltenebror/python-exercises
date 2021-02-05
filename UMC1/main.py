# UMC 1:
def act1A():
    for i in range(10, 21):
        print(i)


def act1B(amigos):
    for amigo in amigos:
        print("Hola " + amigo)


def act1C():
    print("Saludaremos a tus 5 amigos")
    amigos = []
    for i in range(5):
        name = input("Nombre de tu amigo \n")
        amigos.append(name)
    act1B(amigos)


def act1D():
    numero_amigos = int(input("¿Cuantos amigos quieres saludar? \n"))
    amigos = []
    for i in range(numero_amigos):
        amigo_numero = i+1;
        name = input("Nombre de tu amigo " + str(amigo_numero) + "\n")
        amigos.append(name)
    act1B(amigos)


def act2():
    incompleto = True
    while(incompleto):
        try:
            print("Calcularemos el interés compuesto")
            ci = float(input("Capital incial: "))
            i = float(input("Tasa de interés: "))
            n = float(input("Numero de años que se desean calcular: "))
            incompleto = False
        except ValueError:
            print("Error al introducir los datos, vuelva a intentarlo")
    cf = ci * (1.0 + i/100.0) ** n
    print("----------------------------------------------------------------------")
    print("El total del interés compuesto a pagar es " + str(round(cf, 2)) + "€")

def act3use(f):
    return round((f - 32) * 5 / 9,2)


def act3():
    print("Converidor de Fahrenheit a Celsius")
    datos_incorrectos = True
    while(datos_incorrectos):
        try:
            f = float(input("Introduce los grados  Fahrenheit: "))
            datos_incorrectos = False
        except ValueError:
            print("Valores incorrectos")
    c = act3use(f)
    print(str(f) + " grados Fahrenheit = " + str(c)+ " grados celsius")


def act4():
    for i in range(0, 121 ,10):
        print(str(i) + "ºF = " + str(act3use(i)) + "ºC")


def act5():
    print("Mostrar todos los números pares entre los números dados")
    n1 = int(input("Número 1: "))
    n2 = int(input("Numero 2: "))+1
    if(n1 % 2 != 0):
        n1 += 1
    for i in range(n1, n2, 2):
        print(str(i)+" ", end='')
    print()


def act6():
    suma = 0
    n = int(input("Cantidad de nñumeros triangulares que que se desean"))
    for i in range(1, n+1):
        suma += i
        print(str(i) + " - " + str(suma))


def act7():
    quantity = int(input("Número de factoriales a calcular: "))
    for i in range(quantity):
        fact = 1
        number = int(input("Número del que deseas sacar factorial: "))
        for j in range(1, number + 1): #guia se rompe cuando los numeros son de dos cifras retocar
            print(str(j) + " ", end='')
        print()
        for j in range(1, number + 1):  #factorial
            fact = fact * j
            print(str(fact) + " ", end='')
        print()

