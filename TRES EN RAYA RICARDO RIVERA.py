import math
import random

# Tamaño del tablero
tablero_filas = 3
tablero_columnas = 3

# Inicialización del tablero
tablero = [" "] * (tablero_filas * tablero_columnas)

def coordenada(literal, inferior, superior):
    """
    Obtiene una coordenada válida del usuario.

    Parameters
    ----------
    literal : str
        Mensaje para el usuario.
    inferior : int
        Límite inferior válido.
    superior : int
        Límite superior válido.

    Returns
    -------
    coor : int
        Coordenada válida del usuario.
    """
    while True:
        valor = input(literal)
        while not valor.isnumeric():
            print("Solo se admite números entre {0} y {1}".format(inferior, superior))
            valor = input(literal)
        coor = int(valor)
        if inferior <= coor <= superior:
            return coor
        else:
            print("El valor indicado es incorrecto, solo se permite valores de {0} y {1}".format(inferior, superior))

def colocar_ficha(ficha):
    """
    Permite que un jugador coloque su ficha en el tablero.

    Parameters
    ----------
    ficha : str
        Ficha del jugador ('x' o 'o').

    Returns
    -------
    casilla : int
        Índice de la casilla en la que se colocó la ficha.
    """
    print("Dame la posición de la fila: ")
    while True:
        fila = coordenada("Fila entre [1 y 3]: ", 1, tablero_filas)
        columna = coordenada("Columna entre [1 y 3]: ", 1, tablero_columnas) - 1
        casilla = (fila - 1) * tablero_columnas + columna
        if tablero[casilla] != ' ':
            print("La casilla está ocupada")
        else:
            tablero[casilla] = ficha
            return casilla

def pintar_tablero():
    """
    Imprime el tablero en la consola.
    """
    pos = 0
    print("-" * 13)
    for fila in range(tablero_filas):
        for columna in range(tablero_columnas):
            print("|", tablero[pos], end=" ")
            pos += 1
        print("|")
        print("-" * 13)

def numeroHermanos(casilla, ficha, h, v):
    """
    Función recursiva para contar las fichas consecutivas en una dirección.

    Parameters
    ----------
    casilla : int
        Índice de la casilla actual.
    ficha : str
        Ficha del jugador ('x' o 'o').
    h : int
        Dirección horizontal (-1, 0, 1).
    v : int
        Dirección vertical (-1, 0, 1).

    Returns
    -------
    int
        Número de fichas consecutivas en la dirección dada.
    """
    f = math.floor(casilla / tablero_columnas)
    c = casilla % tablero_columnas
    fila_nueva = f + v
    if not (0 <= fila_nueva < tablero_filas):
        return 0
    columna_nueva = c + h
    if not (0 <= columna_nueva < tablero_columnas):
        return 0
    pos = (fila_nueva * tablero_columnas + columna_nueva)
    if tablero[pos] != ficha:
        return 0
    else:
        return 1 + numeroHermanos(pos, ficha, h, v)

def hemosGanado(casilla, ficha):
    """
    Verifica si un jugador ha ganado.

    Parameters
    ----------
    casilla : int
        Índice de la casilla actual.
    ficha : str
        Ficha del jugador ('x' o 'o').

    Returns
    -------
    bool
        True si el jugador ha ganado, False en caso contrario.
    """
    hermanos = numeroHermanos(casilla, ficha, -1, -1) + numeroHermanos(casilla, ficha, 1, 1)
    if hermanos == 2:
        return True
    hermanos = numeroHermanos(casilla, ficha, 1, -1) + numeroHermanos(casilla, ficha, -1, 1)
    if hermanos == 2:
        return True
    hermanos = numeroHermanos(casilla, ficha, -1, 0) + numeroHermanos(casilla, ficha, 1, 0)
    if hermanos == 2:
        return True
    hermanos = numeroHermanos(casilla, ficha, 0, -1) + numeroHermanos(casilla, ficha, 0, 1)
    return hermanos == 2

def jugar_con_amigos():
    """
    Permite a dos jugadores jugar entre ellos.
    """
    jugador1 = input("Digite el nombre del primer jugador: ")
    jugador2 = input("Digite el nombre del segundo jugador: ")
    jugar(jugador1, jugador2)

def jugar_contra_maquina():
    """
    Permite a un jugador jugar contra la máquina.
    """
    jugador = input("Digite su nombre: ")
    jugar(jugador, "Máquina", True)

def acerca_de():
    """
    Muestra información acerca del juego.
    """
    print("Acerca de:")
    print("Juego de 3 en línea desarrollado por Ricardo Rivera.")
    print("Versión 1.0 - Noviembre 2023")

def jugar(jugador1, jugador2, vs_maquina=False):
    """
    Gestiona el juego entre dos jugadores o jugador contra máquina.

    Parameters
    ----------
    jugador1 : str
        Nombre del primer jugador.
    jugador2 : str
        Nombre del segundo jugador o "Máquina" si es contra la máquina.
    vs_maquina : bool, optional
        True si es contra la máquina, False si es entre dos jugadores. 
    """
    continuar = True
    fichas_tablero = 0
    while continuar:
        pintar_tablero()
        ficha = 'x' if (fichas_tablero % 2 == 0) else 'o'
        if not vs_maquina or ficha == 'x':
            casilla
