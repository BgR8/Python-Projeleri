for i in range(3):
    sifre = input("şifre belirle: ")
    if i == 2:
        print("şifre 3 kez yanlış girildi",
              "Lütfen 30dk sonra deneyin")

    elif not sifre:
        print("Şifre boş bırakma")

    elif len(sifre) in range(3, 8):
        print("Yeni şifre", sifre)
        break

    else:
        print("şifre 3 ila 8 karakter arasında olmalı")
