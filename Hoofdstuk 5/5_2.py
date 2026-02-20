# Klasse cirkel met een constructor en de methode maakIngesloten.
class Cirkel:
    def __init__(self, straal):
        self.straal = straal
    def maak_ingesloten(self):
        """
            Maakt een rechthoek die in een cirkel past.
            Returns: rechthoek (object)
         """
        breedte = 2*self.straal       
        hoogte = 2*self.straal
# De methode geeft een object als resultaat terug.                   
        return Rechthoek(breedte, hoogte)

# De klasse rechthoek met een constructor.
class Rechthoek:
   def __init__(self, breedte, hoogte):
       self.breedte = breedte
       self.hoogte = hoogte

# Objecten aanmaken en de methode oproepen.
c = Cirkel(5)
rh = c.maak_ingesloten()
print(rh.breedte, rh.hoogte)
print(type(rh))