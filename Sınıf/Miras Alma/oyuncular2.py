#Alt sınıf
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
    memleket = 'Arpaçbahşiş'

    def hareket_et(self):
        print('yeni hareket_et() metodu')

    def örnekmetetot(self):
        pass

    @classmethod
    def sınıfmetot(cls):
        pass

    @staticmethod
    def statikmetot():
        pass

class İşçi(Oyuncu):
    pass

class Yönetici(Oyuncu):
    pass
