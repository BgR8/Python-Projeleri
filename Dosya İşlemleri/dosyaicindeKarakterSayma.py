hakkinda = open("hakkinda.txt")

harf = input("Sorgulamak istenen harf: ")
    
sayı = 0

for karakterdizi in hakkinda:
    for karakter in karakterdizi:
        if harf == karakter:
            sayı += 1

    print(sayı)
    
    hakkinda.close()
