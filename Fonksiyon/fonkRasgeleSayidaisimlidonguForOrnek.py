def yenikayit(**bilgiler):
    print("-"*30)

    for anahtar, değer in bilgiler.items():
        print("{:<10}: {}".format(anahtar, değer))

    print("-"*30)

yenikayit(ad="BgR", soyad="Soyad", şehir="Aksaray", tel="123456789")
