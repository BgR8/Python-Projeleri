def karşılıkbul(*args, **kwargs):
    for sözcük in args:
        if sözcük in kwargs:
            print("{} = {}".format(sözcük, kwargs[sözcük]))
        else:
            print("{} kelimesi sözlükte yok!".format(sözcük))

sözlük = {"kitap"       : "book",
          "bilgisayar"  : "computer",
          "programlama" : "programming"}

karşılıkbul("kitap", "bilgisayar", "programlama", "fonksiyon", **sözlük)
