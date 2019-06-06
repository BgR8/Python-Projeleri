simge = input("Simgeniz: ")
sifre = input("Şifreniz: ")

tuzunluk = len(simge) + len(sifre)
mesaj = "Simgeniz ve şifreniz toplam {} karakterden oluşmaktadır."

print(mesaj.format(tuzunluk))

if tuzunluk > 40:
    print("Simgeniz ve parolanızın",
          "toplam uzunluğu 40 karakteri geçmemeli.")

else:
    print("Hoşgeldiniz")
