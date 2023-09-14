import random


def main():
    amount = get_amount()
    length = get_length()

    print("\nPasswords:")

    for i in range(amount):
        print(generate(amount, length))


def get_amount():
    while True:
        number = input("How many passwords you want to generate? ")
        try:
            if int(number) > 0:
                return int(number)
        except ValueError:
            pass


def get_length():
    while True:
        try:
            length = input("Length: ")
            if int(length) < 8:
                raise ValueError
            return int(length)
        except ValueError:
            print("A password should be at least 8 characters long")
            pass


def get_chars():
    characters = list(map(chr, range(33, 126)))
    return characters


def generate(n, l):
    for i in range(n):
        passwords = ''
        for c in range(l):
            passwords += random.choice(get_chars())
    return passwords



if __name__ == "__main__":
    main()