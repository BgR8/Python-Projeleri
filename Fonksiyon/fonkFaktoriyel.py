def faktor(sayi):
    print(sayi, ' ')
    if sayi == 1:
        print("= ")
        return 1
    print('* ')
    return faktor(sayi - 1) * sayi

print(faktor(5))
