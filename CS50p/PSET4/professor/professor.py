import random
import sys

random.seed(0)

def main():
    level = get_level()

    score = 0
    error = 1

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y
        equation = input(f"{x} + {y} = ")


        if int(equation) == answer:
            score += 1

        while int(equation) != answer:
            error += 1
            print("EEE")
            equation = input(f"{x} + {y} = ")
            if error >= 3:
                print(f"{x} + {y} = {answer}")
                break

    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        try:
            if 1 <= int(level) <= 3:
                return int(level)
        except ValueError:
            pass

def generate_integer(level):
    try:
        if level == 1:
            x = random.randint(0, 9)
            return x
        elif level == 2:
            x = random.randint(10, 99)
            return x
        elif level == 3:
            x = random.randint(100, 999)
            return x
    except:
        raise ValueError

if __name__ == "__main__":
    main()