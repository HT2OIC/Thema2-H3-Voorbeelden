# De klasse MyApp aanmaken. Dit is een subklasse van App.
class MyApp(App):
    # We roepen ons raster op om te tonen in onze app.
    def build(self):
        return MyGrid()