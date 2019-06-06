modüller = ['os', 'sys', 'random', 'subprocess']

def kesişimbul(modüller):
    kümeler = [set(dir(__import__(modül))) for modül in modüller]
    return set.intersection(*kümeler)

print(kesişimbul(modüller))
