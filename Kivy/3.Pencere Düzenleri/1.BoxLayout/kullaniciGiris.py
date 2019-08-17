from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Program(App):
    def build(self):
        self.anaDuzen = BoxLayout(orientation = "vertical") # Elemanların hepsini tutan ana pencere düzenimiz

        self.ilkSatir = BoxLayout()
        self.ikinciSatir = BoxLayout()

        self.nick = Label(text="Nick")
        self.nickKutu = TextInput()

        self.sifre = Label(text = "Şifre")
        self.sifreKutu = TextInput()


        self.buton = Button(text = "Giriş Yap")

        self.ilkSatir.add_widget(self.nick)
        self.ilkSatir.add_widget(self.nickKutu)

        self.ikinciSatir.add_widget(self.sifre)
        self.ikinciSatir.add_widget(self.sifreKutu)

        # Şimdi hepsini ana düzene yerleştir

        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)
        self.anaDuzen.add_widget(self.buton)

        return self.anaDuzen

Program().run()
