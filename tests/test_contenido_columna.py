from src.prototipo import contenido_columna

def test_contenido_columna():
    tablero = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
    ]

    assert [2, 1, 2, 2, 2, 1] == contenido_columna(3,tablero)