class Punt:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

p = Punt(3.5, 5.0)
q = Punt()

print("p: ({}, {})".format(p.x, p.y))
print("q: ({}, {})".format(q.x, q.y))