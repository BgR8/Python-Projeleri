# data kelimesi yerine veri kelimesi daha uygun olduğu düşünüldüğünde
# @property bezeyicisini kullanarak data() metodunu niteliğe dönüştürdük
# böylece
# p = Program()
# p.data ve
# p.veri
# self.veri üzerindeki değişiklik self.data niteliğine de yansıyacak
class Program():
    def __init__(self):
        self.veri = 0

    @property
    def data(self):
        return self.veri
