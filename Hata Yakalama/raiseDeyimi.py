trKar = "şçüöıİ"

sifre = input("Şifre: ")

for i in sifre:
    if i in trKar:
        raise TypeError("Şifrede Tr kullanma")
    else:
        pass

print("Şifre kabul")
