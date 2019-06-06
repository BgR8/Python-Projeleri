# import sys ile modülünü dahil ediyoruz
# sys.path ile sys modülünün niteliğini çağırıyoruz.
# sys.path.append(r'DizinAdı') ile niteliğine dizini yani ögeyi ekliyoruz
# böylece modülümüzü istediğimiz yerden çağırabiliriz.
# 'from distutils import sysconfig' ve
# 'sysconfig.get_python_lib()' ile dizinin yerini tespit ediyoruz.
# 'sys.path.insert(0, r'dizin/adı') ile öncelik vermek istediğimiz dizini
# listenin başına ekliyoruz.
# import(modül) ile modülü dahil ediyoruz
# modüle yeni bir fonksiyon vs. eklendiğinde değişikliğin
# dir(modüladı) ile tekrar gözükmesi için
# import importlib kütüphanesini dahil edip
# importlib.reload(modüladı) ile modülün tekrar yüklenmesini sağlanır.

# tekrar yeni bir modül eklendiğinde importlib.reload(modüladı) ile tekrar
# yüklenmesi sağlanmalı.

# modüle eklenen bir fonksiyonu silmek için del modüladı.fonksiyon ile sil.

#def personel_sayısını_görüntüle():
 #   print(len(Çalışan.personel))
    
class Çalışan():
    personel = []

    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetler = []
        self.personele_ekle()

    def personel_sayısını_görüntüle(self):
        print(len(self.personel))

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi.'.format(self.isim))

    def personeli_görüntüle(self):
        print('Personel Listesi: ')
        for kişi in self.personel:
            print(kişi)

    def kabiliyet_ekle(self, kabiliyet):
        self.kabiliyetler.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print('{} adlı kişinin kabiliyetleri: '.format(self.isim))
        for kabiliyet in self.kabiliyetler:
            print(kabiliyet)
