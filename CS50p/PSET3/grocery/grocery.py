grocery = {}

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    if item in grocery:
        grocery[item] += 1
    else:
        grocery[item] = 1

for item in sorted(grocery.keys()):
    print(grocery[item], item)

