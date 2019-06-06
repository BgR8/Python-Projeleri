for i in range(3):
    print(i)
    parola = input("parola belirle: ")
    if i == 2:
        print("parolayı 3 kez yanlış girdiniz.",
              "Lütfen 30 dakika sonra tekrar deneyin!")

    elif not parola:
        print("parola bölümü boş geçilemez!")

    elif len(parola) in range(3, 8):
        print("Yeni parolanız", parola)
        break

    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı.")
