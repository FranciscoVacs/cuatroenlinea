def tablero_vacio():
    return [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def contenido_columna(nro_columna,tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna - 1]
        columna.append(celda)
    return columna

def contenido_fila(nro_fila,tablero):
    fila = []
    for celda in tablero[nro_fila - 1]:
        fila.append(celda)
    return fila

def todas_columnas(tablero):
    array_columnas = []
    columnas = []
    for columna in range(7):
        for fila in tablero:
            celda = fila[columna]
            columnas.append(celda)
        array_columnas.append(columnas)
        columnas = []
    return array_columnas

def todas_filas(tablero):
    array_filas = []
    for fila in tablero:
        array_filas.append(fila)
    return array_filas

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
    print("\nEl tablero es:\n")
    print("+---------------+")
    for fila in tablero:
        print("|",*fila,"|")
    print("+---------------+")
    


secuencia = [1,2,3,1]
if (limite_columna(secuencia)):
    tablero = completar_tablero_en_orden(secuencia,tablero_vacio())
    dibujar_tablero(
        completar_tablero_en_orden(
            secuencia, tablero_vacio()
        )
    )
else:
    print("Secuencia Incorrecta") 

print('Contenido Columna 1:',contenido_columna(1,tablero))
print('Contenido Fila 6',contenido_fila(6,tablero))
print('El array de columnas es:',todas_columnas(tablero))
print('El array de filas es:',todas_filas(tablero))

