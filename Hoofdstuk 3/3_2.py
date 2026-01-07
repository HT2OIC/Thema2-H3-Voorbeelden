# De superklasse Dier aanmaken.
class Dier:
    # Constructor
    def __init__(self, naam):
        self.naam = naam
    # Methode eten.
    def eten(self):
        print("Ik kan eten.")

# De subklasse Hond aanmaken.
class Hond(Dier):
    # Stringmethode
    def __str__(self):
        return "Mijn naam is "+ self.naam
    
    # De methode eten() overschrijven.
    def eten(self):
        print("Ik kan eten.")
        print("Ik eet vlees")

# Een object van de subklasse Hond aanmaken.
labrador = Hond("Woef")
labrador.eten()
print(labrador)

# Een object van de superklasse Dier aanmaken.
poedel = Dier("FiFi")
poedel.eten()