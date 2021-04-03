from src.dni import dni
from src.tabla import tabla_letras

def test_validar_longitud_dni():
    assert dni('41569305').verificar_longitud_dni() == True