# De superklasse Dier aanmaken.
class Dier:
    def __init__(self, naam):
        self.naam = naam
    
    def eten(self):
        print("Ik kan eten.")

# De subklasse Hond aanmaken.
class Hond(Dier):
    def __str__(self):
        return "Mijn naam is "+ self.naam
    # De methode eten() uit Dier oproepen en een extra printopdracht aan toevoegen.

    def eten(self):
        super().eten()
        print("Ik eet vlees")

# Het object labrador aanmaken via de klasse Hond.
labrador = Hond("Woef")
labrador.eten()
print(labrador)

# Het object parkiet aanmaken via de klasse Dier.
parkiet = Dier("Coco")
parkiet.eten()