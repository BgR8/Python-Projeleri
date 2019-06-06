kaynak = "şçöğüıŞÇÖĞÜİ"
hedef = "scoguiSCOGUI"

çeviritablo = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."

print(metin.translate(çeviritablo))
