ilksayı = input("ilk sayı: ")
ikincisayı = input("ikinci sayı: ")

#hata yakalama sayı 0'a bölünemez

try:
    sayı1 = int(ilksayı)
    sayı2 = int(ikincisayı)
    print(sayı1, "/", sayı2, "=", sayı1/sayı2)
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz")
