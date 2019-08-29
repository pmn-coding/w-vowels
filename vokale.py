v = input("Word:")

vokale = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for i in vokale:
    v = v.replace(i, "")

print(v)