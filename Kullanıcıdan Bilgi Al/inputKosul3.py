yaş = int(input("Yaşınız: "))

if yaş == 18:
    print("18")

elif yaş < 0:
    print("Hadi ordan")

elif yaş < 18:
    print("Gençlik başımda duman")

elif yaş > 18:
    print("Büyümektesin")
