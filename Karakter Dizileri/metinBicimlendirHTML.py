sayfa = """
<html>
<head>
<title> %(dil)s </title>
</head>
<body>
<h1> %(dil)s </h1>
<p>Web sitemize hoşgeldiniz! Konumuz: %(dil)s</p>
</body>
</html>
"""

print(sayfa % {"dil": "Python Programlama Dili"})
