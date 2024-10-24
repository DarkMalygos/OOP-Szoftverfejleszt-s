from jarat import Jarat


class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, ferohely, indulasi_idopont):
        super().__init__(jaratszam, celallomas, jegyar)
        self.ferohely = ferohely
        self.indulasi_idopont = indulasi_idopont
        self.foglalt_helyek_szama = 0

    def __str__(self):
        return f"Járatszám: {self.jaratszam}, célállomás: {self.celallomas}, maximális férőhely: {self.ferohely}, indulás: {self.indulasi_idopont}, jegyár: {self.jegyAr()}FT"

    def jegyAr(self):
        return self.jegyar
