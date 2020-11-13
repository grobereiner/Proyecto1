import random
import time

alfabeto=[chr(a) for a in range(97, 123)] + [chr(b) for b in range(65,91)]+['1','2','3','4','5','6','7','8','9','0']

def resultados(puntaje, tiempo, estado):
    if estado=='G':
        print("Acerto la frase")
    else:
        print("Ha perdido")
    print("Puntaje obtenido:",puntaje)
    print("Tiempo tardado:",round(tiempo[0],2),"s")
    nombre=input("Introduce tu nombre: ")
    while len(nombre)<5:
        nombre=input("Ingresa un nombre mas largo: ")
    return nombre

def palabraSeleccionada():
    palabras=["Hola como estas","Estudio en UTEC","Impostor","UTECsino","Ay Caramba","Aquel arbolito","CS ROCKS","I like turtles","P1 esta facil","Mi iPhone es marca Samsung","Hoy saco veinte","Vaticano","Hereje","Salchipapa","Pollo a la brasa","Pan con queso","Palta brother","Ciento ocho","Todo es increible","Ironman","Chavo del ocho"]
    seleccion=palabras[random.randint(0,len(palabras)-1)]
    seleccionLista=[]
    for i in seleccion:
        if i==' ':
            seleccionLista.append('|')
        else:
            seleccionLista.append('_')
    return seleccion, seleccionLista

def palabraImprimir(lista):
    print("Frase:")
    for i in lista:
        print(i,end=' ')
    print()

def palabraCompleta(lista, original):
    for i in range(len(original)):
        if not (lista[i]==original[i] or lista[i]=='|'):
            return False
    return True

def caracterObtener(tiempo):
    tiempoInicial=time.time()
    caracter=input("Ingrese letra a adivinar: ")
    while len(caracter)!=1 or not caracter in alfabeto:
        caracter=input("Ingrese letra a adivinar: ")
    tiempoFinal=time.time()
    tiempo[0]+=(tiempoFinal-tiempoInicial)
    caracter=caracter.lower()
    return caracter

def caracterComprobar(caracter,original):
    if caracter in original or caracter.upper() in original:
        return True
    return False

def caracterReemplazar(caracter, lista, original):
    for i in range(len(original)):
        if caracter==original[i] or caracter.upper()==original[i]:
            lista[i]=original[i]

def dibujo5(errores):
    C1=["   ",' | ','/| ', '/|\\']
    C2=["   ","/  ","/ \\"]
    print("========")
    print("  +---+")
    print("  |   |")
    print("  O   |")
    print(" "+C1[3 if errores>=3 else errores]+"  |")
    print(" "+C2[0 if errores<4 else errores%3]+"  |")
    print("      |")
    print("========")

def dibujo10(errores):
    C1=['   ',' | ','/| ', '/|\\']
    C2=['     ','  |  ','/ |  ','/ | \\']
    C3=['   ','/  ','/ \\']
    C4=['     ','/    ','/   \\']
    print("============")
    print("    +------+")
    print("    |      |")
    print("    O      |")
    print("   "+C1[3 if errores>=3 else errores]+"     |")
    print("  "+C2[0 if errores<4 else (3 if errores>6 else errores-3)]+"    |")
    print("   "+C3[0 if errores<7 else (2 if errores>8 else errores%6)]+"     |")
    print("  "+C4[0 if errores<9 else errores%8]+"    |")
    print("           |")
    print("           |")
    print("============")

def dibujo15(errores):
    C1=["   "," | ","/| ","/|\\"]
    C2=["     ","  |  ","/ |  ","/ | \\"]
    C3=["       ","   |   ","/  |   ","/  |  \\"]
    C4=["   ","/  ","/ \\"]
    C5=["     ","/    ","/   \\"]
    C6=["       ","/      ","/     \\"]
    print("====================")
    print("      +-----------+")
    print("      |           |")
    print("      O           |")
    print("     "+C1[3 if errores>3 else errores]+"          |")
    print("    "+C2[0 if errores<4 else (3 if errores>6 else errores-3)]+"         |")
    print("   "+C3[0 if errores<7 else (3 if errores>9 else errores-6)]+"        |")
    print("     "+C4[0 if errores<10 else (2 if errores>11 else errores-9)]+"          |")
    print("    "+C5[0 if errores<12 else (2 if errores>13 else errores-11)]+"         |") 
    print("   "+C6[0 if errores<14 else errores-13]+"        |")
    print("                  |")
    print("                  |")
    print("                  |")
    print("====================")

def dibujoN(intentos, errores):
    if intentos==5:
        dibujo5(errores)
    elif intentos==10:
        dibujo10(errores)
    else:
        dibujo15(errores)

def ignorar():
    a=input("Ingrese cualquier tecla para continuar: ")
