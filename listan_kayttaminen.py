lista=[]


while True:
   
    valinta=int(input(" Haluatko\n (1) Lisätä listaan\n (2) Poistaa listalta vai\n (3)Lopettaa?: "))
    
  
    if valinta == 1: # Lisätään uusi alkio listaan
        lisaa= input("Mitä lisätään?: ")
        lista.append(lisaa)
    
    elif valinta == 2: #Poistetaan alkio listalta
        try:  
            pituus= len(lista)
            print(f"Listalla on {pituus} alkiota.")
            poista=int(input("Monesko niistä poistetaan?: " ))
            lista.pop(poista)
        except IndexError:
            print("Virheellinen valinta.")
    
    elif  valinta == 3: # Ohjelman lopetus valinta
        print("Listalla oli tuotteet:")
        for i in lista:
            print(i)
        break
    else:     
        print("Virheellinen valinta.")
  