import juego
import os
from pandas import read_csv

def opcionValidar(opciones):
    opcion=input("Ingresar opcion: ")
    while not opcion in opciones:
        opcion=input("Opcion incorrecta, intente de nuevo: ")
    return opcion

def menuPrincipal(opciones, intentos):
    os.system("cls")
    while opciones[2]==0:
        print("1. Jugar\n2. Configuracion\n3. Highscores\n4. Salir")
        opcionPrincipal=opcionValidar(["1","2","3","4"])
        if opcionPrincipal == "1":
            menuJugar(opciones, intentos)
        elif opcionPrincipal == "2":
            menuConfiguracion(opciones, intentos)
        elif opcionPrincipal == "3":
            resultadosLeer()
            print("1. Regresar")
            regresar=opcionValidar(['1'])
            os.system("cls")
        else:
            opciones[2]=1
    os.system("cls")

def menuJugar(opciones, intentos):
    os.system("cls")
    while opciones[2]==0 and opciones[0]==0:
        print("1. Un jugador\n2. Dos jugadores\n3. Regresar\n4. Salir")
        opcionJugar=opcionValidar(["1","2","3","4"])
        if opcionJugar=="1":
            resultados=juego.juegoUnJugador(int(intentos[0]))
            resultadosGrabar(resultados)
        elif opcionJugar=="2":
            os.system("cls")
            print("En construccion\n1. Regresar")
            regresar=opcionValidar(['1'])
            os.system("cls")
        elif opcionJugar=="3":
            opciones[0]=1
        else:
            opciones[2]=1
    opciones[0]=0
    os.system("cls")

def menuConfiguracion(opciones, intentos):
    os.system("cls")
    while opciones[2]==0 and opciones[1]==0:
        print("1. Configurar intentos\n2. Regresar\n3. Salir")
        opcionConfig=opcionValidar(["1","2","3"])
        if opcionConfig == "1":
            os.system("cls")
            print("Cantidad de intentos para el juego (solo puede ser 5, 10 o 15):")
            intentos[0] = opcionValidar(["5", "10", "15"])
            os.system("cls")
        elif opcionConfig == "2":
            opciones[1] = 1
        elif opcionConfig == "3":
            opciones[2] = 1
    opciones[1]=0
    os.system("cls")

def resultadosGrabar(resultados):
    archivo = open("resultados.csv", "a")
    for i in range(len(resultados)-1):
        archivo.write(str(resultados[i])+", ")
    archivo.write(str(resultados[len(resultados)-1])+"\n")
    archivo.close()

def resultadosLeer():
    os.system("cls")
    archivo = read_csv("resultados.csv")
    print(archivo)
    del archivo
