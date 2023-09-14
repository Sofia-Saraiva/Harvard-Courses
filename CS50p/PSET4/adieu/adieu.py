import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
        mylist = p.join((names))
    except EOFError:
        break

print(f"Adieu, adieu, to {mylist}")
