#örnek niteliği sadece fonksiyon içinde tanımlanır
class Çalışan():
    kabiliyet = ['sınıf niteliği']

    def __init__(self):
        self.kabiliyet = ['örnek niteliği']

#sınıf niteliğine erişmek için
#sınıf adını kullanıyoruz
print(Çalışan.kabiliyet)

#örnek niteliğine erişmek için
#örnek adını kullanıyoruz
ahmet = Çalışan()
print(ahmet.kabiliyet)
