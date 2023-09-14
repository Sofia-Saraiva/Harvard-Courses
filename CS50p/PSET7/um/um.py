import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"\b(um)\b", s.lower())
    return len(um), um


if __name__ == "__main__":
    main()