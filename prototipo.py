def tablero_vacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def limite_columna(secuencia):
    for i in (secuencia):
        if i < 1 or i > 7:
            return False
    return True

def completar_tablero_en_orden(secuencia, tablero):
    j=1
    for n in range(0, len(secuencia)):
        soltar_ficha_en_columna(j,secuencia[n],tablero)
        n = n+1
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
if (limite_columna(secuencia)):
    dibujar_tablero(
        completar_tablero_en_orden(
            secuencia, tablero_vacio()
        )
    )
else:
    print("Secuencia Incorrecta") 