nimi=input("Anna tiedoston nimi:") #pyydetään tiedoston nimi käyttäjältä 
try:

    tiedosto = open(nimi,"r")
    sisalto = tiedosto.read()
    sisalto = int(sisalto) +313
    tiedosto.close()
except IOError:
          print("Virheellinen tiedostonnimi")

except ValueError:
          print("Tiedoston sisältö virheellinen!")
    
else:
      
      print(f"Saatiin tulos {sisalto}")