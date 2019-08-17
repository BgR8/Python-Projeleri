from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class AnchorOrnek(App):
    def build(self):
        self.govde = FloatLayout()

        anchor = AnchorLayout(anchor_x = "left",anchor_y = "center")
        buton = Button(text = "Sol Orta",size_hint = (.2,.2))
        anchor.add_widget(buton)

        self.govde.add_widget(anchor)

        return self.govde

AnchorOrnek().run()