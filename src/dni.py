from src.tabla_letras import tabla_letras
class dni:
    longitud_dni = 9
    def __init__(self,dni_entero):
        self.dni_entero = str(dni_entero)
        
    def verificar_longitud_dni(self):
        if len(self.dni_entero) == dni.longitud_dni:
            return false
        else:
            return "Error: El DNI no cumple las condiciones necesarias, demasiado largo o demasiado corto, vuelva a intentarlo"