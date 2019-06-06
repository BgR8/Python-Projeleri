# kullanıcıdan daire çapı iste
çap = input("Dairenin çapı: ")

# verilen çap bilgisine göre
# yarıçapı hesapla
yarıçap = int(çap) / 2

# pi sayısı
pi = 3.14159

# yukarıdaki bilgilere göre
# daire alanını hesapla
alan = pi * (yarıçap * yarıçap)

# hesaplanan alanı yazdır.
print("Çapı", çap, "cm olan dairenin alanı: ", alan, "cm2dir")
