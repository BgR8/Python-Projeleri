import sqlite3
#veritabanına bağlan, vt yoksa oluştur
vt = sqlite3.connect('C:/Users/Buğra/Desktop/Python/SQLite/test.sqlite')
# geçici vt oluştur
#vt = sqlite3.connect(':memory:')
#vt üzerinde işlem yap
im = vt.cursor()
#tablo oluştur. IF NOT EXIST ile tekrar vt oluşturma hatası ortadan kalkacak
im.execute("CREATE TABLE IF NOT EXIST personel (isim, soyisim, memleket)")
#veya sql = "CREATE TABLE adresdefter (isim, soyisim)"
# im.execute(sql)

degergir = """INSERT INTO personel VALUES ('BUĞRA', 'ARGON', 'AKSARAY')"""
im.execute(degergir)

# verileri vtye işle
vt.commit()
vt.close()
