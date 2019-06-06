#Dizideki her kelimenin ilk harfini büyüt

kardiz = "istanbul büyükşehir belediyesi"

if kardiz.startswith("i"):
    kardiz = "İ" + kardiz[1:]
    kardiz = kardiz.title()

print(kardiz)

print("-"*len(kardiz))

kardiz = "on iki ada"

for kelime in kardiz.split():
    if kelime.startswith("i"):
        kelime = "İ" + kelime[1:]

    kelime = kelime.title()

    print(kelime, end=" ")
