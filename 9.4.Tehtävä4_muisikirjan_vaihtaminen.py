import os
from datetime import datetime

def tarkista_ja_luo_tiedosto(tiedostonimi):
    if not os.path.exists(tiedostonimi):
        print(f"Oletusmuistioa ei löydy, luodaan tiedosto.")
        with open(tiedostonimi, 'w') as file:
            pass

def lue_muistikirjaa(tiedostonimi):
    with open(tiedostonimi, 'r') as file:
        content = file.read()
        if content:
            print(content)
        else:
            print("Muistio on tyhjä.")

def lisää_merkintä(tiedostonimi):
    merkintä = input("Kirjoita uusi merkintä: ")
    aikaleima = datetime.now().strftime(":::%H:%M:%S %d/%m/%y")
    with open(tiedostonimi, 'a') as file:
        file.write(f"{merkintä}{aikaleima}\n")

def tyhjennä_muistikirja(tiedostonimi):
    with open(tiedostonimi, 'w') as file:
        pass
    print("Muistio tyhjennetty.")

def vaihda_muistiota():
    uusi_tiedostonimi = input("Anna tiedoston nimi: ")
    tarkista_ja_luo_tiedosto(uusi_tiedostonimi)
    return uusi_tiedostonimi

def main():
    tiedostonimi = "muistio.txt"
    tarkista_ja_luo_tiedosto(tiedostonimi)

    while True:
        print(f"Käytetään muistiota: {tiedostonimi}")
        print("(1) Lue muistikirjaa")
        print("(2) Lisää merkintä")
        print("(3) Tyhjennä muistikirja")
        print("(4) Vaihda muistiota")
        print("(5) Lopeta")
        
        valinta = input("Mitä haluat tehdä?: ")

        if valinta == "1":
            lue_muistikirjaa(tiedostonimi)
        elif valinta == "2":
            lisää_merkintä(tiedostonimi)
        elif valinta == "3":
            tyhjennä_muistikirja(tiedostonimi)
        elif valinta == "4":
            tiedostonimi = vaihda_muistiota()
        elif valinta == "5":
            print("Lopetetaan.")
            break
        else:
            print("Virheellinen valinta!")

if __name__ == "__main__":
    main()
