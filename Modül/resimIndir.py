import urllib.request

url1 = "https://www.agac.gen.tr/images/agac-isismleri.jpg"
url2 = "https://wallpapershome.com/images/pages/pic_h/20329.jpg"
url3 = "https://wallpapershome.com/images/pages/pic_h/18275.jpg"

urllistesi = [url1, url2, url3]
say =1
for url in urllistesi:
    urllib.request.urlretrieve(url, "Resim" + str(say) + ".jpg")
    say +=1
