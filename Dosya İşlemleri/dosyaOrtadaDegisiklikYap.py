with open("fihrist.txt", "r+") as f:
    veri = f.readlines() # verileri liste olarak aldık
    veri.insert(2, "Buğra ARGON\t: 0541 290 2089\n")
    f.seek(0) #Dosyayı başa sar
    f.writelines(veri) # dosyaya liste tipinde veri yazdırır. Listeler değiştirilebilir

    # for öğe in veri:
    #   f.write(öğe)
    # Eğer writelines() kullanmazsak
