from belfoldiJarat import BelfoldiJarat
from nemzetkoziJarat import NemzetkoziJarat
from legiTarsasag import LegiTarsasag
from jegyFoglalas import JegyFoglalas

# Légitársaság létrehozása
legiTarsasag1 = LegiTarsasag("Sky Airlines")

# 3 db. járat objektum létrehozása
belfoldiJarat1 = BelfoldiJarat("JS1", "Budapest", 1000, 3, "2024-12-01")
belfoldiJarat2 = BelfoldiJarat("JS2", "Debrecen", 2000, 4, "2024-11-20")
nemzetkoziJarat1 = NemzetkoziJarat("JS3", "Seoul", 15000, 2, "2024-11-05")

# 3 db. járat hozzáadása a légitársasághoz
legiTarsasag1.jaratok = belfoldiJarat1
legiTarsasag1.jaratok = belfoldiJarat2
legiTarsasag1.jaratok = nemzetkoziJarat1

# A légitársaság járatainak a kiírása:
# legiTarsasag1.jaratok


# Foglalás objektum létrehozása
foglalas = JegyFoglalas()

# 6 db. foglalás hozzáadása a foglalás objektumhoz
foglalas.foglalasHozzaadasa(1, "Laura", belfoldiJarat1)
foglalas.foglalasHozzaadasa(2, "Kozsó", belfoldiJarat2)
foglalas.foglalasHozzaadasa(3, "Balázs", nemzetkoziJarat1)
foglalas.foglalasHozzaadasa(4, "Dávid", belfoldiJarat1)
foglalas.foglalasHozzaadasa(5, "Messi", nemzetkoziJarat1)
foglalas.foglalasHozzaadasa(6, "LeBron James", belfoldiJarat2)


def felhasznaloi_interfesz():
    while True:
        print(f"Üdvözli Önt a {legiTarsasag1.nev} légitársaság!")
        print("1., Jegy foglalása")
        print("2., Foglalás lemondása")
        print("3., Foglalások listázása")
        print("4., Kilépés")

        dontes = int(input("Válasszon a fenti menüpontok közül: "))
        print("")

        if dontes == 1:
            szemelyi_szam_input = int(input("Kérem adja meg a személyi számát: "))
            nev_input = input("Kérem adja meg a nevét: ")
            print(
                f"\nHova szeretne utazni?\n1: {belfoldiJarat1.jaratszam}, célállomás: {belfoldiJarat1.celallomas}, indulás: {belfoldiJarat1.indulasi_idopont}\n2: {belfoldiJarat2.jaratszam}, célállomás: {belfoldiJarat2.celallomas}, indulás: {belfoldiJarat2.indulasi_idopont}\n3: {nemzetkoziJarat1.jaratszam}, célállomás: {nemzetkoziJarat1.celallomas}, indulás: {nemzetkoziJarat1.indulasi_idopont}"
            )
            dontes_celallomas = int(input("Válasszon a fenti menüpontok közül: "))
            if dontes_celallomas == 1:
                print(
                    foglalas.foglalasHozzaadasa(
                        szemelyi_szam_input, nev_input, belfoldiJarat1
                    )
                )
            elif dontes_celallomas == 2:
                print(
                    foglalas.foglalasHozzaadasa(
                        szemelyi_szam_input, nev_input, belfoldiJarat2
                    )
                )
            elif dontes_celallomas == 3:
                print(
                    foglalas.foglalasHozzaadasa(
                        szemelyi_szam_input, nev_input, nemzetkoziJarat1
                    )
                )
        elif dontes == 2:
            torlendo_foglalas_szemelyi_szam = input(
                "Kérem adja meg a törölni kívánt foglaláshoz tartozó személyi számot: "
            )
            print(foglalas.foglalasTorlese(torlendo_foglalas_szemelyi_szam))
        elif dontes == 3:
            foglalas.foglalasokListazasa
            print("")
        elif dontes == 4:
            break
        else:
            print("Nem megfelelő választás. Próbálja újra!\n")


felhasznaloi_interfesz()
