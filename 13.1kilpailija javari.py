class Kilpailija:
      """Luokka määrittelee kilpailijoiden pisteet ja värin"""
    
__vari = ""
__pisteet = 0

def lisaa_pisteet(self, lisays = 1):
    self.__pisteet = + lisays
   
def lisaa_vari(self, valinta):
    self.__vari = valinta

def tulostaja(self):
    print(f"Kilpailijalla on {self.__vari} on {self.__pisteet} pistettä!")
       
def main():
      eka = Kilpailija()
      eka.__pisteet(10)
      eka.__vari("Sininen")
      
      eka.tulostaja()
        
if __name__ == "__main__":
      main()




      # -*- coding: latin-1 -*-

#class Henkilo:
 #   nimi = "arto";
  #  ika = 5;

   # def __init__(self, nimi):
    #    self.nimi = nimi;
     #   self.ika = 0;

    #def kerro(self):
     #   return "Hei! Olen " + self.nimi + " ja ikäni on " + str(self.ika);

#arto = Henkilo("Arto")
#print "Mitä kertoo?: " + arto.kerro();