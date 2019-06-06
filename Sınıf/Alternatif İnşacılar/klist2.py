liste = [('9789753424080', 'Grenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
         ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
         ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def sorgula(ölçüt=None, değer=None):
    d = {'isbn'     : [li for li in liste if değer == li[0]],
         'yazar'    : [li for li in liste if değer == li[1]],
         'eser'     : [li for li in liste if değer == li[2]],
         'yayınevi' : [li for li in liste if değer == li[3]]}

    for öğe in d.get(ölçüt, liste):
        print(*öğe, sep = ', ')
