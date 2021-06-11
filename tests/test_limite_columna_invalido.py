from src.prototipo import limite_columna

def test_limite_de_columnas_invalido():
    secuencia = [0,1,2,3,4,5,6,7,8,9]

    assert limite_columna(secuencia) == False