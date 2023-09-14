due = 50
while due > 0:
    print(f"Amount due: {due}")
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
else:
    change = str(due).strip("-")
    print(f"Change owed: {change}")

