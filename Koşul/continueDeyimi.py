while True:
    s = input("Sayı gir: ")

    if s == "i":
        break

    if len(s) <= 3:
        continue

    print("en fazla 3 haneli sayı gir")
