d1 = open("isim1.txt", encoding="utf-8") # dosya aç, karakter dili
d1_satir = d1.readlines() # satırları oku

d2 = open("isim2.txt", encoding="utf-8")
d2_satir = d2.readlines()

for i in d2_satir:
    if not i in d1_satir:
        print(i)


print("-"*3)

# benzer ögeleri ayıkla
for i in d2_satir:
    if i in d1_satir:
        print(i)

d1.close()
d2.close()
