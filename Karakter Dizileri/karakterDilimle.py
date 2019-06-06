#site = "www.milevni.com"
#print(site[4:11])

site1 = "www.milevni.com"
site2 = "www.atolyemde.com"
site3 = "www.google.com"
site4 = "www.gnu.org"

for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])

print("-"*len(site2))


#atasözlerindeki ünlem işareti kaldır ve nokta ekle

ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2 = "Ağa güçlü olunca kul suçlu olur!"
ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"

for ata in ata1, ata2, ata3, ata4, ata5:
    print(ata[0:-1] + ".")
