liste = ["elma", "armut", "elma", "kiraz",
         "çilek", "kiraz", "elma", "kebap"]

for i in set(liste):
    print("{} listede {} kez geçiyor!".format(i, liste.count(i)))
