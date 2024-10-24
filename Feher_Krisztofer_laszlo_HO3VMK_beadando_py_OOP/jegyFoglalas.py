from datetime import date


class JegyFoglalas:
    def __init__(self):
        self._foglalasok = []

    def foglalasHozzaadasa(self, utas_id, utas_nev, jarat):
        flag = False
        for foglalas in self._foglalasok:
            if foglalas["szemelyi_szam"] == utas_id:
                flag = True
                break
        if flag:
            return f"{utas_id} személyi számmal már foglaltak jegyet!\n"
        if jarat.foglalt_helyek_szama >= jarat.ferohely:
            return f"A {jarat.jaratszam} járatra a helyek beteltek. Válasszon másikat vagy várjon a következőre!\n"
        jelenlegi_ido = str(date.today())
        if jelenlegi_ido >= jarat.indulasi_idopont:
            return f"A {jarat.jaratszam} járatra már nem lehet foglalni, mivel már elindult!\n"
        jarat.foglalt_helyek_szama += 1
        foglalas = {"szemelyi_szam": utas_id, "utas_neve": utas_nev, "jarat": jarat}
        self._foglalasok.append(foglalas)
        return f"Sikeresen foglalt jegyet a {jarat.jaratszam} járatra. A jegy ára: {jarat.jegyAr()}FT\n"

    def foglalasTorlese(self, torles_id):
        int_torles_id = int(torles_id)
        for foglalas in self._foglalasok:
            if foglalas["szemelyi_szam"] == int_torles_id:
                jarat = foglalas["jarat"]
                jarat.foglalt_helyek_szama -= 1
                self._foglalasok.remove(foglalas)
                return f"A {torles_id} ID-val rendelkező foglalás sikeresen törölve!\n"
        return f"A {torles_id} ID-val rendelkező foglalással nem rendelkezünk!\n"

    @property
    def foglalasokListazasa(self):
        if not self._foglalasok:
            return "Nem rendelkezünk foglalásokkal!"
        else:
            print("Foglalásaink:")
            for foglalas in self._foglalasok:
                szemelyi_szam = foglalas["szemelyi_szam"]
                jarat = foglalas["jarat"]
                print("Foglalás ID:", szemelyi_szam, "-", jarat)
