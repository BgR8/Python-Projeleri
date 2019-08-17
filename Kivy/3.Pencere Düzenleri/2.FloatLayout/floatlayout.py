from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class Program(App):
    def build(self):

        duzen = FloatLayout() # pencere düzenimizi tanımladık

        buton = Button(text = "Merhaba",
                                size_hint = (.1,.1),
                                pos = (10,10))
# size_hint, butonun ekrana orantılı şekilde boyutlandırılması için;
# Yani .1 yazıldığında pencere boyutunun 10'da 1'i kadar genişlik ve yükseklikte boyutlandır.
# .5 yazılsaydı ekranın boyutunun yarısı kadar olacaktı.
# pos, pencere düzeninde yerini belirlendi. (0,0) noktası sol alt köşedir

# Yani (10, 10) ile 10px soldan 10px aşağıdan uzaklık şeklinde
        duzen.add_widget(buton) # butonu yerleştiriyoruz
        
        return duzen

Program().run()