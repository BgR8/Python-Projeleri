kontrol = []
sonuç = 1

while True:
    sayı = input("sayı (hesaplamak için q)): ")
    if sayı == "q":
        break
    kontrol.append(sayı)
    sonuç *= int(sayı)

if len(kontrol) < 2:
    print("Yeterli sayı girilmedi!")
else:
    print(sonuç)
