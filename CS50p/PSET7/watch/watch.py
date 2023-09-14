import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    raw = re.search(r"src=.+\/embed/(.+)\"", s)
    if raw:
        link = raw.group(1)
        return (f"https://youtu.be/{link}")

if __name__ == "__main__":
    main()