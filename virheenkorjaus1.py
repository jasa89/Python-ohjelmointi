def luvunpyytaja(): 
   
          
        luku = input("Anna luku: ")

        try:
          luku = int(luku)
        except Exception:
          print("Virheellinen syöte!")
          #Jos virhettä ei löydy, ajetaan else
        else:
              print("Syöte oli kelvollinen.")
                   
        
def main():
    
    luvunpyytaja()



if __name__ == "__main__":
      main()