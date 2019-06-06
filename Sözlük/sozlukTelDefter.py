tDefter = {"ahmet öz"   : "0532 532 32 32",
           "mehmet su"  : "0543 543 42 42",
           "seda naz"   : "0533 533 33 33",
           "eda ala"    : "0212 212 12 12"}

kişi = input("TelNo öğrenmek için kişi adı girin: ")

if kişi in tDefter:
    cevap = "{} adlı kişinin telefon numarası: {}"
    print(cevap.format(kişi, tDefter[kişi]))
else:
    print("Aranılan kişi yok")
