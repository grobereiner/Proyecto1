import funcJuego
import os

def juegoUnJugador(intentos):
    palabra, palabraMuestra = funcJuego.palabraSeleccionada()
    errores = 0
    puntaje = 0
    tiempo = [0]

    while not errores==intentos:
        os.system("clear")
        funcJuego.dibujoN(intentos, errores)
        funcJuego.palabraImprimir(palabraMuestra)

        if funcJuego.palabraCompleta(palabraMuestra, palabra):
            nombre=funcJuego.resultados(puntaje, tiempo, 'G')
            funcJuego.ignorar()
            os.system("clear")
            return [nombre[:5], puntaje, round(tiempo[0],2), "Gano",  intentos,  errores]
      
        letra=funcJuego.caracterObtener(tiempo)
        
        if funcJuego.caracterComprobar(letra, palabra):
            if not ((letra.lower() in palabraMuestra) or (letra.upper() in palabraMuestra)):
                puntaje+=1
            funcJuego.caracterReemplazar(letra, palabraMuestra, palabra)   
        else:
            errores+=1
    else:
        os.system("clear")
        funcJuego.dibujoN(intentos, errores)
        funcJuego.palabraImprimir(palabraMuestra)
        nombre=funcJuego.resultados(puntaje, tiempo, 'P')
        funcJuego.ignorar()
        os.system("clear")
        return [nombre[:5], puntaje, round(tiempo[0],2), "Perdio",  intentos,  intentos]
