# {isim} ile format işlevi kullanımı
sayfa = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>{konu}</title>
</head>
<body>
<h1>istihza.com web sitesine hoş geldiniz!</h1>
<p><b>{konu}</b> için bir Türkçe belgelendirme projesi...</p>
</body>
</html>
"""
print(sayfa.format(konu="Python Programlama Dili"))
