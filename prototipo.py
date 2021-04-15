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
    j=1
    for n in range(0, len(secuencia)):
        if secuencia[n] > 0 and secuencia[n] < 8:
            soltar_ficha_en_columna(j,secuencia[n],tablero)
            n = n+1
            if j==1: j = j+1
            else: j = j-1
        else:
            print("\nSecuencia incorrecta")
            tablero = 0
            return tablero
    return tablero
            



def soltar_ficha_en_columna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return

def dibujar_tablero(tablero):
    if tablero == 0: print("Intentelo nuevamente")
    else:
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