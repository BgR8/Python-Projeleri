f = open("python3.pdf", "rb")
okunan = f.read()

#/Producer = Belgeyi PDF'ye çeviren yazılım
producer_index = okunan.index(b"/Producer")

#Producer ifadesi ilk baytı
print(okunan[producer_index])

# sayının hangi karaktere karşılık geldiği
print(chr(okunan[producer_index]))

# PDF'yi üreten yazılım
print(okunan[producer_index:producer_index+70].split())
