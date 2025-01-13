


def tulostaja(merkkijono="Oletustulostus"):
    print(merkkijono)             
       
      
def main():
        while True:
            syote=input("Anna syöte (Lopeta lopettaa):")    
            if syote=="Lopeta":
                break
            elif len(syote)>=5:  
                tulostaja(syote)
            else:
                tulostaja()
 
        


if __name__ == "__main__":
        main()