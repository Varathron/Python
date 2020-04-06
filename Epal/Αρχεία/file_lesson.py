
fin = open("words.txt", "r")

print fin.read(3)

print fin.tell()

fin.seek(6)

print fin.read(3)
print fin.tell()
