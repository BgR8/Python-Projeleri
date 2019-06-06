with open("fihrist.txt", "r+") as f:
    veri = f.read()
    f.seek(0) #Dosyayı başa sar
    f.write("Sedat Köz\t: 0322 234 45 45\n"+veri)
