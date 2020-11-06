import utilJuego
import os

def juegoUnJugador(intentos):
    palabra, palabraMuestra = utilJuego.palabraSeleccionada()
    errores = 0
    puntaje = 0
    tiempo = [0]

    while not errores==intentos:
        os.system("cls")
        utilJuego.dibujoN(intentos, errores)
        utilJuego.palabraImprimir(palabraMuestra)

        if utilJuego.palabraCompleta(palabraMuestra, palabra):
            nombre=utilJuego.resultados(puntaje, tiempo, 'G')
            utilJuego.ignorar()
            os.system("cls")
            return [nombre[:5], puntaje, round(tiempo[0],2), "Gano",  intentos,  errores]
      
        letra=utilJuego.caracterObtener(tiempo)
        
        if utilJuego.caracterComprobar(letra, palabra):
            if not letra in palabraMuestra:
                puntaje+=1
            utilJuego.caracterReemplazar(letra, palabraMuestra, palabra)   
        else:
            errores+=1
    else:
        os.system("cls")
        utilJuego.dibujoN(intentos, errores)
        utilJuego.palabraImprimir(palabraMuestra)
        nombre=utilJuego.resultados(puntaje, tiempo, 'P')
        utilJuego.ignorar()
        os.system("cls")
        return [nombre[:5], puntaje, round(tiempo[0],2), "Perdio",  intentos,  intentos]
