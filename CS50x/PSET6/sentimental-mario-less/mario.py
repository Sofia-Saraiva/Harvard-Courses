# // Building a right-aligned pyramid

from cs50 import get_int

# Get user input of the height
while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

# Rows of the pyramid
for i in range(n):
    # Columns of the pyramid
    for j in range(n):
        # Print blankspaces and hashes
        if i + j < n - 1:
            print(" ", end="")
        else:
            print("#", end="")
    print()
    