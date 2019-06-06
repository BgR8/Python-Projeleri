ilksayı = input("ilk sayı: ")
ikincisayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilksayı)
    sayı2 = int(ikincisayı)
    print(sayı1, "/", sayı2, "=", sayı1/sayı2)
except ValueError:
    print("Lütfen sayı giriniz")

