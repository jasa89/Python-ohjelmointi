
class Kilpailija:
    def __init__(self, vari, pisteet=0):
        self.vari = vari
        self.pisteet = pisteet
    
    def tilanne(self):
        print(f"Olen {self.vari} ja minulla on {self.pisteet} pistettä!")
    
    def maali(self):
        self.pisteet += 1

# Luodaan olio nimeltä "eka" ja annetaan sille väriksi "sininen"
eka = Kilpailija("sininen")
            
# Kutsutaan jäsenfunktiota maali
eka.maali()

# Kutsutaan jäsenfunktiota
eka.tilanne()