class Sınıf():
    sınıf_nitelik = 0

    def __init__(self, veri):
        self.veri = veri

    def örnekmetod(self):
        return self.veri

    @classmethod
    def sınıfmetod(cls):
        return cls.sınıf_nitelik

    @staticmethod
    def statikmetot():
        print('merhaba statik metot')
