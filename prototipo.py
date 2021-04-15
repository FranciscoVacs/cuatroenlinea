def tablero_vacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def completar_tablero_en_orden(secuencia, tablero):
    i = len(secuencia)
    n=0
    j=1
    for ficha in range(0, i):
        soltar_ficha_en_columna(j,secuencia[n],tablero)
        n= n+1
        if j==1: j = j+1
        else: j = j-1
    return tablero
        



def soltar_ficha_en_columna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return

def dibujar_tablero(tablero):
    print("\nEl tablero es:")
    for i in tablero:
        for j in i:
            print(j, end=" ")
        print()
       


secuencia = [1,2,3,1]
dibujar_tablero(
    completar_tablero_en_orden(
        secuencia, tablero_vacio()
    )
) 