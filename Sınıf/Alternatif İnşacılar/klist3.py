liste = [('9789753424080', 'Grenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
         ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
         ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def bul(değer, sıra):
    return [li for li in liste if değer == li[sıra]]

def sorgula(ölçüt=None, değer=None):
    d = {'isbn'     : bul(değer, 0),
         'yazar'    : bul(değer, 1),
         'eser'     : bul(değer, 2),
         'yayınevi' : bul(değer, 3)}

    for öğe in d.get(ölçüt, liste):
        print(*öğe, sep = ', ')
