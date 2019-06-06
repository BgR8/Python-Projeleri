kelime = input("Herhangi bir kelime: ")

sayaç = ""

for harf in kelime:
    if harf not in sayaç:
        sayaç += harf

for harf in sayaç:
    print("{} harfi {} kelimesinde {} kez geçiyor". format(harf,
                                                           kelime,
                                                           kelime.count(harf)))
