#swapcase ile büyük harfi küçüğe, küçüğü büyüğe değiştir.

kardiz = "python"
print(kardiz.swapcase())

print("-"*len(kardiz))

print("Swapcase", "\n----")

kardiz = "istanbul"

for i in kardiz:
    if i == "İ":
        kardiz = kardiz.replace('İ', 'i')
    elif i == 'i':
        kardiz = kardiz.replace('i', 'İ')
    else:
        kardiz = kardiz.replace(i, i.swapcase())

print(kardiz)
