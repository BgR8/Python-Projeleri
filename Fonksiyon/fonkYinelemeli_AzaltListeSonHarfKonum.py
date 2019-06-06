n = 0

def azalt(s):
    global n
    mesaj = '{} harfinin {}. çalışmadaki konumu: [}'
    if len(s) < 1:
        return s
    else:
        n += 1
        print(mesaj.format('a', n, s.index('a')))
        return azalt(s[1:])

azalt('atölyemde')
