class Program():
    def __init__(self):
        self._sayı = 0

    @property
    def sayı(self):
        return self._sayı

    @sayı.setter
    def sayı(self, yeni_değer):
        if yeni_değer % 2 == 0:
            self._sayı = yeni_değer
        else:
            print('çift değil!')
            
        return self._sayı

    @sayı.deleter
    def sayı(self):
        del self._sayı
