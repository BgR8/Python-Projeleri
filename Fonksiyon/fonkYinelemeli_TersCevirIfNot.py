def tersçevir(s):
    if not s:
        return s
    else:
        return s[-1] + tersçevir(s[:-1])

print(tersçevir('atölyemde'))
