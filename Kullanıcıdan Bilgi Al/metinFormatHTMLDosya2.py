kodlama = "utf-8"
site_adı = "Python Programlama Dili"
dosya = open("deneme.html", "w", encoding=kodlama)
içerik = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset={0}" />
<title>{1}</title>
</head>
<body>
<h1>istihza.com web sitesine hoş geldiniz!</h1>
<p><b>{1}</b> için bir Türkçe belgelendirme projesi...</p>
</body>
</html>
"""


print(içerik.format(kodlama, site_adı), file=dosya)
dosya.close()
