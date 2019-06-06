class Çalışan():
    _personel = []

    def __init__(self, isim):
        self._isim = isim
        self.personele_ekle()

    def personele_ekle(self):
        self._personel.append(self._isim)
        print('{] adlı kişi personele eklendi'.format(self._isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel Listesi: ')
        for kişi in cls._personel:
            print(kişi)

    def isim_değiştir(self, yeni_isim):
        kişi = self._personel.index(self._isim)
        self._personel[kişi] = yeni_isim
        print('yeni isim: ', yeni_isim)
