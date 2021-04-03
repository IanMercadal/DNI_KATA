from src.tabla import tabla_letras
class dni:
    longitud_dni = 9
    def __init__(self,dni_entero):
        self.dni_entero = str(dni_entero)
        
    def verificar_longitud_dni(self):
        if len(self.dni_entero) == dni.longitud_dni:
            return False
        else:
            return "Error: El DNI no cumple las condiciones necesarias, demasiado largo o demasiado corto, vuelva a intentarlo"
        
    def verificar_letra_dni(self):
        if self.dni_entero[-1].isalpha() == True:
            letra_correspondiente = tabla_letras(self.dni_entero[0:-1]).calculo_letra()
            if letra_correspondiente == self.dni_entero[-1]:
                return self.dni_entero
        else:
            return False
        if self.dni_entero[0].isalpha() == True:
            letra_correspondiente = tabla_letras(self.dni_entero[1:]).calculo_letra()
            if letra_correspondiente == self.dni_entero[0]:
                return self.dni_entero
            else:
                return False
        else:
                return dni_entero + tabla_letras(self.dni_entero).calculo_letra()
            
    def crear_dni(self):
        if dni.verificar_longitud_dni(self) != True:
            return dni.verificar_longitud_dni(self)
        resultado = dni.verificar_letra_dni(self)
        if resultado == False:
            return "Error: la letra no es correcta"
        else:
            return self.dni_entero