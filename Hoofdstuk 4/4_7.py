# Klasse MyGrid aanmaken. Dit is een subklasse van GridLayout.
class MyGrid(GridLayout):
    # Constructor met variabele aantal attributen (kwargs).
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        # 2 kolommen aanmaken in het raster.
        self.cols = 2

        # Rij 1
        # Kolom 1: label.
        self.add_widget(Label(text="Naam: "))
        # Kolom 2: Textinput.
        self.naam = TextInput(multiline = False)
        self.add_widget(self.naam)

        # Rij 2
        # Kolom 1: label.
        self.add_widget(Label(text="Achternaam"))
        # Kolom 2: Textinput.
        self.achternaam = TextInput(multiline = False)
        self.add_widget(self.achternaam)

        # Rij 3
        # Kolom 1: label.
        self.add_widget(Label(text="E-mail"))
        # Kolom 2: Textinput.
        self.mail = TextInput(multiline = False)
        self.add_widget(self.mail)