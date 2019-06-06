class HarfSayacı:
    def __init__(self):
        self.sesli_harf = 'aeıioöuü'
        self.sesiz_harf = 'bcçdfgğhjklmnprsştvyz'
        self.sayaç_sesli = 0
        self.sayaç_sessiz = 0

    def kelime_sor(self):
        return input('Bir kelime girin : ')

    def seslidir(self, harf):
        return harf in self.sesli_harf

    def sessizdir(self, harf):
        return harf in self.sessiz.harf

    def artır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayaç_sesli += 1
            if self.sessizdir(harf):
                self.sayaç_sessiz += 1
        return (self.sayaç_sesli, self.sayaç_sessiz)

    def ekrana_bas(self):
        sesli, sessiz = self.artır()
        mesaj = "{} kelimesinde {} sesli {} sessiz harf var."
        print(mesaj.format(self.kelime, sesli, sessiz))

    def çalıştır(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
        sayaç = HarfSayacı()
        sayaç.çalıştır()
