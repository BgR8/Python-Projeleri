ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

#ilk_metin değişkende olup ikinci_metin değişkende olanı arama
for s in ilk_metin:
    if not s in ikinci_metin:
        print(s)
        
print("-"*3)
#ikinci_metin değişkende olup ilk_metin değişkende olanı arama
for s in ikinci_metin:
    if not s in ilk_metin:
        print(s)

print("-"*3)

#farklı olan harften yalnızca 1 tanesini göster

fark = ""

for s in ikinci_metin:

    # if not s in ilk_metin and not s in fark:
    #if deyimini tek satırda kullanma
    
    if not s in ilk_metin:
        if not s in fark:
            fark +=s
        print(fark)


