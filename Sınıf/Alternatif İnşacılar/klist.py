liste = [('9789753424080', 'Grenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
         ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
         ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def sorgula(ölçüt=None, değer=None):
    for li in liste:
        if not ölçüt and not değer:
            print(*li, sep=', ')

        elif ölçüt == 'isbn':
            if değer == li[0]:
                print(*li, sep=', ')

        elif ölçüt == 'yazar':
            if değer == li[1]:
                print(*li, sep=', ')

        elif ölçüt == 'eser':
            if değer == li[2]:
                prnt(*li, sep=', ')

        elif ölçüt == 'yayınevi':
            if değer == li[3]:
                print(*li, sep=', ')
