kullanıcı_adı = input("Kullanıcı adınız: ")
parola = input("Parolanız: ")

if kullanıcı_adı == "aliveli":
    if parola == "12345678":
        print("Programa hoşgeldiniz")
    else:
        print("Yanlış kullanıcı adı veya parola!")
else:
    print("Yanlış kullanıcı adı veya parola!")
