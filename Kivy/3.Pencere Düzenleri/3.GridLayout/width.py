from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Ornek(App):
    def build(self):

        govde = GridLayout(cols = 2)
        # Azami 2 sütundan oluşmasını istedik
        # 2 sütundan sonra alta kayacak.

        # Birden fazla buton ekleyip nasıl görünecek
        # for döngüsü ile ekleyelim

        for i in range(10):
            if (i%2 == 0):
                # Aynı sütuna denk gelenler için
                govde.add_widget(Button(text = "{}".format(i+1),
                                        size_hint_x = None,
                                        width = 200))
# Eğer none verilmezse size_hint_x için width ile boyut belirlemeye izin verilmeyecek
            else:
                govde.add_widget(Button(text = "{}".format(i+1)))

        return govde

Ornek().run()

