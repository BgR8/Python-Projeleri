while True:
    sifre = input("Şifre belirle: ")

    if not sifre:
        print("Şifre boş bırakılamaz")

    elif len(sifre) > 8 or len(sifre) < 3:
        print("şifre 8 karakterden uzun 3 karakterden az olamaz.")
        print("Şifreniz : ",len(sifre), "karakter")

    else:
        print("Yeni şifreniz", sifre)
        break
