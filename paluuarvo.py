def pituusmitta(pituus):
   pituus = len(pituus)
   return int(pituus) 
       
      
def main():
        while True:
            syote=input("Anna syöte (Lopeta lopettaa):")    
            syote_pituus=pituusmitta(syote)
            if syote=="Lopeta":
                break
            elif syote_pituus == 0:
                print("Et antanut syötettä")  
                
            else:
                print("Antamasi syöte oli", syote_pituus, "merkkiä pitkä.")
 

                        


if __name__ == "__main__":
        main()