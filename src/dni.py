from src.tabla import tabla_letras
class dni:
    
    def __init__(self,dni_entero):
        self.dni_entero = str(dni_entero)
        
    def verificar_longitud_dni(self):
        if len(self.dni_entero) == tabla_letras.longitud_numero:
            return True
        else:
            return False
        
    def validacion_formato(self):
        if dni.verificar_longitud_dni(self) == True and self.dni_entero.isdigit():
            return True
        else:
            return False
    
    def calculo_letra(self):
        resto_calculo_letra = int(self.dni_entero)%(len(tabla_letras.letras))
        letra = tabla_letras.letras[resto_calculo_letra]
        return letra
    
    def asignacion_letra(self):
        if dni.validacion_formato(self) == True:
            dni_letra = self.dni_entero + dni.calculo_letra(self)
            return dni_letra
        else:
            return False
        print ("Error: Los datos nos son válidos")