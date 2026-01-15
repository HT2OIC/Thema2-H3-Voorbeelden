# Klasse MyGrid aanmaken. Dit is een subklasse van GridLayout.
class MyGrid(GridLayout):
    # Constructor met variabele aantal attributen (kwargs).
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        # Hoofdraster met 1 kolom.
        self.cols = 1

        # Raster in hoofdraster met 2 kolommen.
        # Dit raster geven we de naam inside.
        self.inside = GridLayout()
        self.inside.cols = 2

        # Inside Rij 1: 
        # Kolom 1: label.
        self.inside.add_widget(Label(text="Naam: "))
        # Kolom 2: Textinput.
        self.naam = TextInput(multiline = False)
        self.inside.add_widget(self.naam)

        # Hoofdraster:
        # Rij 1: inside als eerste rij in het hoofdraster invoegen.
        self.add_widget(self.inside)
        # Rij2: knop.
        self.submit = Button(text="Indienen", font_size=40)
        self.add_widget(self.submit)
        