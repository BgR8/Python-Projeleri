# @property Bezeyicisi
# eklenen ismi sonradan değiştirmek için (@property için değil)
# kişi = Çalışan.personel.index('Ahmet')
# Çalışan.personel[kişi] = 'Selim' // kullanışlı bir yöntem değildir.
class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.personele_ekle()

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi pesonele eklendi'.format(self.isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel Listesi: ')
        for kişi in cls.personel:
            print(kişi)

    def isim_değiştir(self, yeni_isim):
        kişi = self.personel.index(self.isim)
        self.personel[kişi] = yeni_isim
        print('yeni isim: ', yeni_isim)
