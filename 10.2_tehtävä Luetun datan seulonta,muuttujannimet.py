with open("merkkijonoja.txt", "r") as tiedosto:
    while True:
        rivi = tiedosto.readline().strip()
        if rivi == "":
            break

        ehto = rivi.isalnum()
        
        if ehto:
            print("Kelpaa salasanaksi:", rivi)
        else:
            print("Sisältää virheellisiä merkkejä:", rivi)



