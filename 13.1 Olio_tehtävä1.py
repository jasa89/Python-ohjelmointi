
class Kilpailija:
  def __init__(self, vari, pisteet):
    self.vari = vari
    self.pisteet = pisteet

  def __str__(self):
    return f"{self.vari} {self.pisteet}"    

eka = Kilpailija("Sininen", 10)

print(eka)
