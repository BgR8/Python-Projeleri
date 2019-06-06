class Sorgu():
    def __init__(self):
        self.liste = [('9789753424080', 'Grenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

    def bul(self, değer, sıra):
        return [li for li in self.liste if değer == li[sıra]]

    def sorgula(self, ölçüt=None, değer=None):
        d = {'isbn'     : self.bul(değer, 0),
             'yazar'    : self.bul(değer, 1),
             'eser'     : self.bul(değer, 2),
             'yayınevi' : self.bul(değer, 3)}

        for öğe in d.get(ölçüt, self.liste):
            print(*öğe, sep = ', ')
