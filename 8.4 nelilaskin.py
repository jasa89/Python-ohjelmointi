
import math

luku_1=int(input("Anna ensimmäinen luku:"))
luku_2=int(input("Anna toinen luku:"))
while True:
    print(" (1) +\n (2) -\n (3) *\n (4) / \n(5)sin(luku1/luku2) \n(6)cos(luku1/luku2) \n(7)Vaihda luvut \n(8)Lopeta")
    print("Valitut luvut:",luku_1,luku_2)

    valinta=int(input("Tee valinta (1-8):")) 
   
    if valinta == 1:
        print("Tulos on:", luku_1+luku_2)
    if valinta == 2:
        print("Tulos on:", luku_1-luku_2)
    if  valinta == 3:
        print("Tulos on:", luku_1*luku_2)
    if  valinta == 4:
        print("Tulos on:", luku_1/luku_2) 
    if  valinta == 5: # lisätään ohjelmaan sin(luku1/luku2) vaihtoehto
        print("Tulos on:", math.sin(luku_1/luku_2))
    if  valinta == 6: # lisätään ohjelmaan cos(luku1/luku2) vaihtoehto
        print("Tulos on:", math.cos(luku_1/luku_2))
   
    if  valinta == 7:
        luku_1=int(input("Anna uusi ensimmäinen luku:"))
        luku_2=int(input("Anna uusi toinen luku:"))
        
    
    if  valinta == 8:
        break
    elif valinta > 8:
        print("Valintaa ei tunnistettu.")