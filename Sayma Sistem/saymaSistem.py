sayısistem = ["onlu", "sekizli", "on altılı", "ikili"]

print(("{: ^9} " *len(sayısistem)).format(*sayısistem))

#{^5} karakter ortala
#{>5} karakter sağa yasla
#{<5} karakter sola yasla

for i in range(17):    
    print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
