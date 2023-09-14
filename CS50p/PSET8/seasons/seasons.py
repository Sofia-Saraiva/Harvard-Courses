from datetime import date, time
import sys
import inflect
p = inflect.engine()

def main():
    print(convert(input("Date of Birth: ")))


def convert(s):
    if "-" in s:
        age = date.today() - date.fromisoformat(s)
        minutes = int(age.days) * 1440
        words = p.number_to_words(minutes, andword="")
        return f"{words.capitalize()} minutes"

    else:
        sys.exit("Invalid")


if __name__ == "__main__":
    main()