class Sorgu():
    def __init__(self, değer=None, sıra=None):
        self.liste = [('9789753424080', 'Grenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

        if not değer and not sıra:
            l = self.liste
        else:
            l = [li for li in self.liste if değer == li[sıra]]

        for i in l:
            print(*i, sep=', ')

    @classmethod
    def isbnden(cls, isbn):
        cls(isbn, 0)

    @classmethod
    def yazardan(cls, yazar):
        cls(yazar, 1)

    @classmethod
    def eserden(cls, eser):
        cls(eser, 2)

    @classmethod
    def yayınevinden(cls, yayınevi):
        cls(yayınevi, 3)
