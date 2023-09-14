# Gives minimal number of coins needed
from cs50 import get_float

# Ask how many cents the customer is owed
while True:
    cents = get_float("Change owed: ")
    if cents > 0:
        break

cents = round(cents * 100)

# Keep track of how many coins needed
count = 0

# Quarters
while cents >= 25:
    cents = cents - 25
    count += 1

# Dimes
while cents >= 10:
    cents = cents - 10
    count += 1

# Nickels
while cents >= 5:
    cents = cents - 5
    count += 1

# Pennies
while cents >= 1:
    cents = cents - 1
    count += 1

# Print total number of coins to give the customer
print(f"{count}")
