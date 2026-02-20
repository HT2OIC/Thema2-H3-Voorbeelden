# Klasse Rechthoek
class Rechthoek:
    def __init__(self, breedte, hoogte):
        self.breedte = breedte
        self.hoogte = hoogte
    
    def oppervlakte(self):
        """
            Oppervlakte rechthoek berekenen.
            Returns: oppervlakte (float)
        """
        return self.breedte * self.hoogte

# Klasse Canvas: kan een vorm bevatten (associatie)
class Canvas:
    def __init__(self, vorm):
        self.vorm = vorm  # associatie: Canvas heeft een vorm

# Objecten aanmaken
r = Rechthoek(4, 10)
canvas2 = Canvas(r)

# Toegang tot attributen en methoden via de associatie
print(canvas2.vorm.breedte)          # 4
print(canvas2.vorm.oppervlakte())    # 40