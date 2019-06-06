def azalt(s):
    if len(s) < 1:
        return s
    else:
        print(list(s))
        return azalt(s[:-1])

print(azalt('AtölyemDe'))
