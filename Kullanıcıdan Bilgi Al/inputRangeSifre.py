while True:
    sifre = input("Şifre belirle: ")

    if not sifre:
        print("Şifre giriniz")

    elif len(sifre) in range(3, 8):
        # şifre uzunluğu 3, 8 karakter aralığında
        print("Şifreniz", sifre)
        break

    else:
        print("Şifreniz 3 ve 8 karakter arasından olmalı")
    
