# self.kabiliyet sınıf niteliği değil, örnek niteliğidir.
# örnek niteliğe erişebilmek için de ilgili sınıfı mutlaka örneklemek gerekir
# Ayrıca sınıf niteliklerinin aksine,
# örnek niteliğine sınıf adı üzerinden erişemeyiz
class Çalışan():
    def __init__(self):
        self.kabiliyet = []
        print(self.kabiliyet)

Çalışan()
