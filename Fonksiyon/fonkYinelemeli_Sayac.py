def sayaç(sayı, sınır):
    print(sayı)
    if sayı == sınır:
        return 'bitti!'
    else:
        # sayı+1, yukarıya doğru sayar, 0,1,2,3.....
        return sayaç(sayı-1, sınır)

print(sayaç(20, 0))
# sayı+1 olduğu zaman
# print(sayaç(0,20))
