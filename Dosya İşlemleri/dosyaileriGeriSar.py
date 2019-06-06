f = open("hakkinda.txt")
print(f.read())

f.seek(10)

#f.tell() ile dosyanın hangi bayt konumunda olduğunu söyler
print(f.tell())

print(f.read())
