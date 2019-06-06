#Her bir ayın kaç gün çektiğini tanımlıyoruz
ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
nisan = haziran = eylül = kasım = 30
şubat = 28
#Doğalgazın vergiler dahil metreküp fiyatı
birimFiyat = 0.79
#Kullanıcı ayda ne kadar doğalgaz tüketmiş?
aylıkSarfiyat = input("Aylık doğalgaz sarfiyatınızı metreküp olarak giriniz: ")
#Kullanıcı hangi aya ait faturasını öğrenmek istiyor?
dönem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
(Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")
#Yukarıdaki input() fonksiyonundan gelen veriyi
#Python'ın anlayabileceği bir biçime dönüştürüyoruz
ay = eval(dönem)
#Kullanıcının günlük doğalgaz sarfiyatı
günlükSarfiyat = int(aylıkSarfiyat) / ay
#Fatura tutarı
fatura = birimFiyat * günlükSarfiyat * ay
print("günlük sarfiyatınız: \t", günlükSarfiyat, " metreküp\n",
"tahmini fatura tutarı: \t", fatura, " TL", sep="")
