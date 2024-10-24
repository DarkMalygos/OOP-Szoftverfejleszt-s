class LegiTarsasag:
    def __init__(self, nev):
        self._nev = nev
        self._jaratok = []

    @property
    def nev(self):
        return self._nev

    @property
    def jaratok(self):
        for jarat in self._jaratok:
            print(
                f"Járatszám: {jarat.jaratszam}, célállomás: {jarat.celallomas}, férőhely: {jarat.ferohely}, indulás: {jarat.indulasi_idopont}, jegyár: {jarat.jegyAr()}FT"
            )

    @jaratok.setter
    def jaratok(self, uj_jarat):
        self._jaratok.append(uj_jarat)
