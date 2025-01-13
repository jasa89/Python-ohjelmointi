import math

def pyydä_lukua():
    while True:
        luku = input("Anna luku: ")
        try:
            return int(luku)
        except ValueError:
            print("Virheellinen syöte!")

def main():
    luku1 = pyydä_lukua()
    luku2 = pyydä_lukua()

    while True:
        print("(1) +")
        print("(2) -")
        print("(3) *")
        print("(4) /")
        print("(5) sin(luku1/luku2)")
        print("(6) cos(luku1/luku2)")
        print("(7) Vaihda luvut")
        print("(8) Lopeta")
        print(f"Valitut luvut: {luku1} {luku2}")

        valinta = input("Tee valinta (1-8): ")
        
        if valinta == "1":
            tulos = luku1 + luku2
            print(f"Tulos on: {tulos}")
        elif valinta == "2":
            tulos = luku1 - luku2
            print(f"Tulos on: {tulos}")
        elif valinta == "3":
            tulos = luku1 * luku2
            print(f"Tulos on: {tulos}")
        elif valinta == "4":
            if luku2 != 0:
                tulos = luku1 / luku2
                print(f"Tulos on: {tulos}")
            else:
                print("Nollalla ei voi jakaa!")
        elif valinta == "5":
            if luku2 != 0:
                tulos = math.sin(luku1 / luku2)
                print(f"Tulos on: {tulos}")
            else:
                print("Nollalla ei voi jakaa!")
        elif valinta == "6":
            if luku2 != 0:
                tulos = math.cos(luku1 / luku2)
                print(f"Tulos on: {tulos}")
            else:
                print("Nollalla ei voi jakaa!")
        elif valinta == "7":
            luku1 = pyydä_lukua()
            luku2 = pyydä_lukua()
        elif valinta == "8":
            print("Lopetetaan.")
            break
        else:
            print("Virheellinen valinta!")

if __name__ == "__main__":
    main()