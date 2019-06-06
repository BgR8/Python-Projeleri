for i in range(128):
    if i % 4 == 0:
        print("\n")

    print("{:<3}{:>8}\t".format(i, repr(chr(i))), sep="", end="")
