def düzlisteyap(liste):
    if not isinstance(liste, list):
        return [liste]
    elif not liste:
        return []
    else:
        return düzlisteyap(liste[0]) + düzlisteyap(liste[1:])

l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]

print(düzlisteyap(l))
