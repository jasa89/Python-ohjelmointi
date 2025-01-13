
#"""Tee yksinkertainen Supermarket-ohjelma,
#jossa kymmenen tuotteen hinnat ovat listassa seuraavasti: [10,14,22,33,44,13,22,55,66,77].
#joka kysyy (input) tuotteen numeroa väliltä 1 - 10 ja laskee listasta haettavan tuotteen hinnan mukaan ostosten kokonaissummaan, samalla tulostaen haetun tuotteen numeron ja hinnan.
#joka kysyy tuotteita kunnes käyttäjä antaa '0' lopettaakseen ohjelman (while-silmukka).
#joka lopuksi tulostaa 'Yhteensä:' ostosten kokonaissumma ja pyytää käyttäjältä summan 'Maksu:' ja tulostaa lopuksi palautettavat vaihtorahat 'Vaihto:' (maksu - summa) käyttäjälle.
#Ohjelmassa on käytettävä: while, input """



print("Supermarket\n===========")

# Tuotteiden hinnat listassa
hinnat = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]

# Alustetaan ostosten kokonaissumma
kokonaissumma = 0

while True:
    # Kysytään tuotteen numeroa käyttäjältä
    tuote_numero = input("Valitse tuote (1-10) 0 lopetus: ")
    
    # Muutetaan syöte kokonaisluvuksi
    try:
        tuote_numero = int(tuote_numero)
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")
        continue
    
    # Tarkistetaan, onko syöte 0 lopettamista varten
    if tuote_numero == 0:
        break
    
    # Tarkistetaan, että numero on välillä 1-10
    if 1 <= tuote_numero <= 10:
        # Haetaan tuotteen hinta
        hinta = hinnat[tuote_numero - 1]
        # Lisätään hinta kokonaissummaan
        kokonaissumma += hinta
        # Tulostetaan tuotteen numero ja hinta
        print(f"Tuote: {tuote_numero} Hinta: {hinta}")
    else:
        print("Virheellinen tuotenumero, yritä uudelleen.")
        
# Tulostetaan kokonaissumma
print(f"Yhteensä: {kokonaissumma}")

# Kysytään maksun määrää käyttäjältä
while True:
    try:
        maksu = int(input("Maksu: "))
        break
    except ValueError:
        print("Virheellinen syöte, yritä uudelleen.")

# Lasketaan vaihtorahat
vaihto = maksu - kokonaissumma

# Tulostetaan vaihtorahat
print(f"Vaihto: {vaihto}")





