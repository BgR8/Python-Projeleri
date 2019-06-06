def tersçevir(s):
    if len(s) < 1:
        return s
    else:
        return tersçevir(s[1:]) + s[0]

kelime = input("Kelime girin: ")
print('Girdiğiniz kelimenin tersi: {}'.format(tersçevir(kelime)))
