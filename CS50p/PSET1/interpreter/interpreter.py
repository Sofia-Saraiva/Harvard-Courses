text = input("Equation: ")
x, y, z = text.split(" ")

if y == "+":
    t = int(x) + int(z)
    print(float(t))
elif y == "-":
    t = int(x) - int(z)
    print(float(t))
elif y == "*":
    t = int(x) * int(z)
    print(float(t))
elif y == "/":
    t = int(x) / int(z)
    print(float(t))