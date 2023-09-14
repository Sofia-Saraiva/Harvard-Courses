text = input("Input: ")

for c in text:
    if not c.lower() in ["a", "e", "i", "o", "u"]:
        print(c, end="")

print()