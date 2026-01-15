# Klasse MyGrid aanmaken. Dit is een subklasse van GridLayout.
class MyGrid(GridLayout):
    # Constructor met variabele aantal attributen (kwargs).
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        # 2 kolommen aanmaken in het raster.
        self.cols = 2