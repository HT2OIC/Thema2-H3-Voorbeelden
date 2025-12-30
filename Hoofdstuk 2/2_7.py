from math import sqrt

class Punt:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def afstand_tot_oorsprong(self):
        return sqrt(self.x**2 + self.y**2)

p = Punt(3.5, 5.0)
print(p.afstand_tot_oorsprong()) 