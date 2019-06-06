tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

print("\n"*5)

for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)


kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

x_durumu = []
y_durumu = []


sıra = 1

while True:
    if sıra % 2 == 0:
        işaret = "X".center(3)
    else:
        işaret = "O".center(3)

    sıra += 1

    print()
    print("İŞARET: {}\n".format(işaret))

    x = input("yukardan aşağı [1, 2, 3]: ".ljust(30))
    if x == "q":
        break

    y = input("soldan sağa [1, 2, 3]: ".ljust(30))

    if y == "q":
        break

    x = int(x)-1
    y = int(y)-1

    print("\n"*15)

    if tahta[x][y] == "__":
        tahta[x][y] = işaret
        if işaret == "X".center(3):
            x_durumu += [[x, y]]
        elif işaret == "O".center(3):
            o_durumu += [[x, y]]
        sıra += 1
    else:
        print("\nORASI DOLU! TEKRAR DENEYİN!")

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)

    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        

        if len(0) == len(i):
            print("O KAZANDI!")
            quit()
        if len(x) == len(i):
            print("X KAZANDI!")
            quit()
