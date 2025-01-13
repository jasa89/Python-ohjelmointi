class Kilpailija:
    """Luokka määrittelee kilpailijan pisteet ja värin"""
  
    pisteet=0
    vari=""

def lisaa_pisteet(self, lisays=1):
    self.pisteet =+ lisays


def lisaa_vari(self,valinta):
    self.vari=valinta


def tilanne(self):
    print(f"Olen {self.vari} ja minulla on {self.pisteet}")

def maali(self):
    self.pisteet = + 1

def main():
    eka = kilpailija()
    eka.lisaa_vari("sininen")
    eka.maali()
    eka.tilanne()
if __name__ == "__main__":
      main()
