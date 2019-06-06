sayılar = 0
notlar = []

for i in range(10):
    veri = int(input("{}. not: ".format(i+1)))
    sayılar += veri
    notlar += [veri]

print("Girilen Notlar: ", *notlar)
print("Not Ortalama: ", sayılar/10)
