from src.tabla import tabla_letras

def test_dni():
    assert 'C' == tabla_letras(45699019).calculo_letra()
    assert 'L' == tabla_letras(26450640).calculo_letra()
    assert 'S' == tabla_letras(18032682).calculo_letra()