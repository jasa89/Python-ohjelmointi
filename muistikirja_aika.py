import time	


    
tiedosto = open("muistio.txt", "r")
tiedosto.close()
    
while True:
    
        print(" (1)Lue muistikirjaa \n (2)Lisää merkintä \n (3)Tyhjennä muistikirja \n (4) Lopeta")
        valinta=int(input("Mitä haluat tehdä?:"))
        if valinta == 1: # lue tiedoston sisältö
          tiedosto = open("muistio.txt","r")
          teksti = tiedosto.read()
          print(teksti)
          tiedosto.close()  
   
        if valinta == 2: # kirjoita uusi merkintä
            tiedosto = open("muistio.txt","a")
            lisays = input("Kirjoita uusi merkintä:")
            aika = time.strftime("%X %x")
            tiedosto.write(lisays+":::"+aika)
            tiedosto.close()
    
        if  valinta == 3: # tyhjennä tiedosto
            tiedosto = open("muistio.txt","w")
            tiedosto.close()
            print("Muistio tyhjennetty.")  
        elif  valinta == 4: # lopeta ohjelma
            print("Lopetetaan.")  
            break
        #else:  #virheellinen valinta
         #  print("Valintaa ei tunnistettu.")
            