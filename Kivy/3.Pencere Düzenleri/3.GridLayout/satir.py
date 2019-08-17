from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Satir(App):
    def build(self):

        govde = GridLayout(rows = 2)
        # Max 2 sütundan oluşmasını istedik
        # 2 sütundan sonra alta kayacaktır

        # Birden fazla buton ekleyerek nasıl göründüğüne bakalım
        # for döngüsü ile ekleyelim
        for i in range(10):
            govde.add_widget(Button(text = "{}".format(i+1)))

        return govde

Satir().run()