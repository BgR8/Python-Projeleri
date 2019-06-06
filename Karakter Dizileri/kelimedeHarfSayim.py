kelime = input("Herhang bir kelime: ")

for harf in kelime:
    print("{} harfi {} kelimesinde {} kez geçiyor!".format(harf,
                                                           kelime,
                                                           kelime.count(harf)))
