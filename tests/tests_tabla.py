from src.dni import dni

def test_validar_longitud_dni():
    assert dni('41569305').verificar_longitud_dni() == True
    assert dni('41567873829305').verificar_longitud_dni() == False
def test_validar_formato():
    assert dni('41569305').validacion_formato() == True
    assert dni('41567873829305').validacion_formato() == False
def test_calculo_letra():
    assert dni('26861694').calculo_letra() == 'V'
    assert dni('66714505').calculo_letra() == 'S'
def test_añadir_letra():
    assert dni('41509405').asignacion_letra() == '41509405V'
    assert dni('72376173').asignacion_letra() == '72376173A'