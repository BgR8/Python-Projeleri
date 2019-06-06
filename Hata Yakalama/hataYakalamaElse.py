try:
    bölünen = int(input("bölünecek sayı: "))
    bölen = int(input("bölen sayı: "))

except ValueError :
    print("Sadece sayı")
else:
    try:
        print("bölünen/bölen")
    except ZeroDivisionError :
        print("Sayı 0'a bölünemez")
