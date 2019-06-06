class Asker():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 100

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')

class İşçi():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 70

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')

class Yönetici():
    def __init__(self, isim, rütbe):
        self.isim = isim
        self.rütbe = rütbe
        self.güç = 20

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')
