#UMD 3
from colorama import init, Fore
init()
init(autoreset=True)

#Ejercicio 01
def es_par(n):
    devolver = False
    if n % 2 == 0:
        devolver = True
    return devolver

def es_primo(n):
    devolver = True
    for i in range(n-1,1,-1):
        if(n%i==0):
            devolver = False
            break
    return devolver


#Ejercicio 02

def abs(n):
    if n < 0:
        n = n * -1
    return n


#Ejercicio 03
def media_notas():
    seguir = True
    notas = []
    while(seguir):
        try:
            nota = float(input("Introduzca nota, -1 para parar: "))
            if nota == -1:
                seguir = False
            else:
                notas.append(nota)
        except ValueError:
            print("Valor incorrecto, debe meter solo números")

    suma = 0
    for nota in notas:
        suma +=nota

    return "La media de tus notas es " + str(suma / len(notas))


#Ejercicio 5
def login():
    contrasenna = "CintiaLaMejor"
    reintentar = True
    while reintentar:
        intento = input( "Introduzca contraseña: ")
        if intento == contrasenna:
            reintentar= False
        else:
            print(Fore.RED + "Contraseña erronea")
    print(Fore.GREEN + "LOGUEADO CON EXITO")

def login_intentos(n):
    contrasenna = "cintia"
    reintentar = True
    logueado = False
    intentoNumero = 1
    while reintentar:
        if intentoNumero <= 3:
            intento = input("Introduzca contraseña, intento número " + str(intentoNumero) +": ")
            intentoNumero +=1
            if intento == contrasenna:
                reintentar = False
                logueado = True
            else:
                print(Fore.RED + "Contraseña erronea")
        else:
            reintentar = False
            print(Fore.YELLOW + "Has excedido el número máximo de intentos.")
    if logueado:
        print(Fore.GREEN + "LOGUEADO CON EXITO")


#Ejercicio 6
from random import randint
def adivina_numero(n):
    random_number = randint(1, n)
    se_equivoco = True
    while se_equivoco:
        intento = int(input("Adivina el número del 1 al " + str(n)) + ": ")
        if intento == random_number:
            print(Fore.GREEN + "ACERTASTE")
            se_equivoco = False
        else:
            print(Fore.YELLOW + ":( Te has equivocado :(  ", end='')
            if intento > random_number:
                print("El número es menor a tu intento")
            else:
                print("El número es mayor a tu intento")


#Ejercicio 7
def max_comun_divisor(n, m):
    if m < n:
        temporal = m
        m = n
        n = temporal
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return  n


#Ejercico 8a
def es_potencia_de_dos(n):
    if n >= 2:
        devolver = True
    else:
        devolver = False
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            devolver = False
            break
    return devolver


#Ejercicio 8b
def suma_potencias_de_2(n1, n2):
    suma = 0
    for n in range(n1, n2+1):
        if es_potencia_de_dos(n):
            suma += n
    return suma