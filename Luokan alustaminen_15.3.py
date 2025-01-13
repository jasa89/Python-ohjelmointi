class Kilpailija:
    """Kilpailija luokka joka määrittelee pisteet ja värin"""

    def __init__(self):
        self.pisteet = 0
        self.vari = input("Anna minulle väri:")

    def tilanne(self):
        print(f"Olen {self.vari} ja minulla on {self.pisteet} pistettä!")

def main():
    eka = Kilpailija()
    toka = Kilpailija()
    eka.tilanne()
    toka.tilanne()
    print(eka.__doc__)

if __name__ == "__main__":
    main()
