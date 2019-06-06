sifre = input("Şifreniz: ")

kontrol = True

for i in sifre:
    if sifre.count(i) > 1:
        kontrol = False

if kontrol:
    print("Şifre onaylandı!")
else:
    print("Aynı harf bir kez kullanılır")
