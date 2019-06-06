class Çalışan():
    _personel = []

    def __init__(self, isim):
        self._isim = isim
        self.personele_ekle()

    def personele_ekle(self):
        self._personel.append(self._isim)
        print('{} adlı kişi personele eklendi'.format(self._isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kişi in cls._personel:
            print(kişi)

    @property
    def isim(self):
        return self._isim

    @isim.setter
    def isim(self, yeni_isim):
        kişi = self._personel.index(self.isim)
        self._personel[kişi] = yeni_isim
        print('yeni isim: ', yeni_isim)
