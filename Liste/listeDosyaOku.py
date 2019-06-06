f = open("listedeneme.txt", "r")

içerik = f.readlines()

#dosyaya istenen konuma öğe ekle
#içerik.insert(konum, metin)

içerik.insert(1, "Ferhat Yaz\n")

g = open("listedeneme.txt", "w")
g.writelines(içerik)



f.close()
g.close()
