from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class Program(App):

        def build(self):
                govde = StackLayout(orientation = "lr-tb")

                for i in range(1,11):
                        govde.add_widget(Button(text = "{}".format(i),size_hint = (None,None),size = (100,50)))

                return govde


Program().run()