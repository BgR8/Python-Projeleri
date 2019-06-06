import random

def sayıuret(başlangıç=0, bitiş=500, adet=6):
    sayılar=set()

    while len(sayılar) < adet:
        sayılar.add(random.randrange(başlangıç, bitiş))

    return sayılar

# Rastgele 6 öğeli 100 sayı göster
for i in range(100):
    print(sayıuret())

#farklı parametreyle 0-100 arası
# print(sayıuret(0, 100, 10))

#küme parantezi olmadan
# 100-1500 arası 20 adet
# print(*sayıuret(100, 1500, 20), sep="-")
