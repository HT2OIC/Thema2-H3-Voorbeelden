# Klasse Dier aanmaken. Dit is een superklasse van vogel en zoogdier.
class Dier:
    # Constructor
    def __init__(self, naam):
        self.naam = naam
    
    # Methode eten
    def eten(self):
        print("Ik kan eten.")

# Klasse Zoogdier aanmaken. Dit is een subklasse van Dier. Het is een superklasse van Hond en Kat.
class Zoogdier(Dier):
    def wandelen(self):
        print("Ik kan wandelen.")

# Klasse Vogel aanmaken. Dit is een subklasse van Dier.
class Vogel(Dier):
    def vliegen(self):
        print("Ik kan vliegen.")

# Klasse Hond aanmaken. Dit is een subklasse van Zoogdier.
class Hond(Zoogdier):
    def communiceren(self):
        print("Waf!")

# Klasse Kat aanmaken. Dit is een subklasse van Zoogdier.
class Kat(Zoogdier):
    def communiceren(self):
        print("Miauw!")