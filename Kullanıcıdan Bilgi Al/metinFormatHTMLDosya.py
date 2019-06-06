kodlama = "utf-8"
site_adı = "Python Programlama Dili"
ders = "Python"
dosya = open("deneme.html", "w", encoding=kodlama)
içerik = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset={}" />
<title>{}</title>
</head>
<body>
<h1>istihza.com web sitesine hoş geldiniz!</h1>
<p><b>{}</b> için bir Türkçe belgelendirme projesi...</p>
</body>
</html>
"""
# {sayı} yaparak değişken tekrarından kurtulunur
# Örnek: {1} ders

print(içerik.format(kodlama, site_adı, site_adı), file=dosya)
dosya.close()
