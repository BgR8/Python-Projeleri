#super()
# miras alınan üst sınıftan nitelik ve metot üzerinde değişiklik yapıldığında
# mevcut özelliği de muhafaza et
class Oyuncu():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')
        
class Asker(Oyuncu): # (miras alınan sınıf)
    def __init__(self, *arglar):
        super().__init__(*arglar)
        self.güç = 100

class İşçi(Oyuncu):
    def __init__(self, *arglar):
        super().__init__(*arglar)
        self.güç = 70

    def hareket_et(self):
        super().hareket_et()
        print('hedefe ulaşıldı')

class Yönetici(Oyuncu):
    def __init__(self, *arglar):
        super().__init__(*arglar)
        self.güç = 50
