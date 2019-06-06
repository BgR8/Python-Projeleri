sesliharf = "aeıioöuü"
sessizharf= "bcçdfgğhjklmnprsştvyz"

sesliler = ""
sessizler = ""

kelime = "istanbul"

for i in kelime:
    if i in sesliharf:
        sesliler += i
    else:
        sessizler += i

print(sesliharf)
print(sessizharf,"\n")
print("-"*len(sessizharf),"\n")

print("sesli harf: ", sesliler)
print("sessiz harf:", sessizler)
