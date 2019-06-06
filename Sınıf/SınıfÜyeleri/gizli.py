class Sınıf():
    # isim bulandırma ile erişmek için
    # s = gizli.Sınıf()
    # s._Sınıf__gizli
    __gizli = 'gizli'

    def örnekmetot(self):
        print(self.__gizli)
        print('örnek metot')

    @classmethod
    def sınıfmetot(cls):
        print('sınıf metot')

    @staticmethod
    def statikmetot():
        print('statik metot')
