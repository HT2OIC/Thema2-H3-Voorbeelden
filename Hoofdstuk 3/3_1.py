# Klasse Dier aanmaken. Dit is de superklasse.
class Dier:
    # Constructor
    def __init__(self, naam):
        self.naam = naam
    
    # Methode eten
    def eten(self):
        print("Ik kan eten.")

# Klasse Hond aanmaken. Dit is een subklasse.
class Hond(Dier):
    # Stringmethode
    def __str__(self):
        return "Mijn naam is {}".format(self.naam)

# Object labrador aanmaken met behulp van de subklasse Hond.
# De superklasse heeft het attribuut naam dat we moeten instellen.
labrador = Hond("Woef")

# We kunnen de methode eten() van de superklasse gebruiken.
labrador.eten()

# We kunnen de stringmethode van de subklasse gebruiken.
print(labrador)