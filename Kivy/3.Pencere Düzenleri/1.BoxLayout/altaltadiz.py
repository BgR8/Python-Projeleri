from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Program(App):
    def build(self):
        duzen = BoxLayout(orientation = "vertical")

        yazi1 = Label(text = "Merhaba")

        yazi2 = Label(text = "Dünya")

        duzen.add_widget(yazi1)
        duzen.add_widget(yazi2)

        return duzen

Program().run()
