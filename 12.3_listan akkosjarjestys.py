tiedosto = open("sanoja.txt","r") #avataan tiedosto
sisalto = tiedosto.readlines()
sisalto = [sana.strip() for sana in sisalto] #poistetaan ylimääräiset rivinvaihdot
sisalto.sort() # laitetaan sanat aakkossjärjestykseen

print("Sanat laitettuna aakkosjärjestykseen:")

for i in sisalto: # tulostetaan sanat
    print(i)