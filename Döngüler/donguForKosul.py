trharf = "şçöğüİı"

sifre = input("Şifre: ")

for karakter in sifre:
    if karakter in trharf:
        print("Türkçe karakter kullanılamaz")
