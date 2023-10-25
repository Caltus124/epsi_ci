class ConvertisseurNombresRomains:
    @classmethod
    def convertir(cls, nombre_arabe):
        if nombre_arabe == 1:
            return "I"
        elif nombre_arabe == 2:
            return "II"
        elif nombre_arabe == 3:
            return "III"
