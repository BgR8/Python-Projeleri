def tersçevir(s):
    if len(s) < 1:
        return s
    else:
        tersçevir(s[1:])
        print(s[0])

tersçevir('atölyemde')
