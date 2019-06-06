class Çalışan():
    __personel = []

    def __init__(self, isim):
        self.__isim = isim
        self.personele_ekle()

    def personele_ekle(self):
        self.__personel.append(self.__isim)
        print('{] adlı kişi personele eklendi'.format(self.__isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel Listesi: ')
        for kişi in cls.__personel:
            print(kişi)

    def isim_değiştir(self, yeni_isim):
        kişi = self.__personel.index(self.__isim)
        self.__personel[kişi] = yeni_isim
        print('yeni isim: ', yeni_isim)
