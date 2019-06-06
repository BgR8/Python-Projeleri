while True:
    ilksayı = input("ilk sayı: ")
    ikincisayı = input("ikinci sayı: ")

    #hata yakalama sayı 0'a bölünemez

    try:
        sayı1 = int(ilksayı)
        sayı2 = int(ikincisayı)
        print(sayı1, "/", sayı2, "=", sayı1/sayı2)
    except ZeroDivisionError as sıfırhata:
        print("Bir sayıyı sıfıra bölemezsiniz")
        print(sıfırhata)
    except ValueError as hata:
        print("Sadece sayı giriniz")
        print(hata)

    #hatagrupla
        #except(ValueError, ZeroDivisionError)
        #print("Hata")

    #hatagrupla: hata adları
        #except(ValueError, ZeroDivisionError) as hata
        #print("Hata")
