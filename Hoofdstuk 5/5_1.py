# Klasse cirkel met een constructor en de methode pastIn.
class Cirkel:
    def __init__(self, straal):
        self.straal = straal

# Eén van de argumenten van past_in is een object van een andere klasse.
    def past_in(self, rechthoek):
        """
            Kijkt na of een rechthoek in een cirkel past.
            argumenten: rechthoek (object)
            returns: boolean (past/past niet)
        """
        return ((2*self.straal >= rechthoek.hoogte) and (2*self.straal >= rechthoek.breedte))

# De klasse rechthoek met een constructor.
class Rechthoek:
   def __init__(self, breedte, hoogte):
       self.breedte = breedte
       self.hoogte = hoogte

# Objecten aanmaken en de methode oproepen.
c = Cirkel(5)
rh = Rechthoek(4,15)
print(c.past_in(rh))