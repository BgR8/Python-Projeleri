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

sözlük = {"kitap"       : "book",
          "bilgisayar"  : "computer",
          "programlama" : "programming"}

def ara(sözcük):
    hata = "{} kelimesi sözlükte yok!"
    return sözlük.get(sözcük, hata.format(sözcük))

def ekle(sözcük, anlam):
    mesaj = "{} kelimesi sözlüğe eklendi!"
    sözlük[sözcük] = anlam
    print(mesaj.format(sözcük))

def sil(sözcük):
    try:
        sözlük.pop(sözcük)
    except KeyError as err:
        print(err, "kelimesi bulunamadı!")
    else:
        print("{} kelimesi sözlükten silindi!".fortmat(sözcük))
