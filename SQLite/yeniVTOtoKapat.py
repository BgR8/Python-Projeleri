import sqlite3

# vt bağlantısı açtığımızda, bütün iş bittikten sonra kendiliğinden sonlandır
with sqlite3.connect('test.sqlite') as vt:
    im = vt.cursor()

    im.execute("""CREATE TABLE IF NOT EXIST personel
        (isim,soyisim, memleket)""")
    im.execute("""INSERT INTO personel VALUES
        ('Buğra', 'ARGON', 'Aksaray')""")

    vt.commit()
