from src.prototipo import limite_columna

def test_limite_de_columnas():
    secuencia = [1,2,3,4,5,6,7]

    assert limite_columna(secuencia) == True