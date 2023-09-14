import sys
import validators

def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    validators.email('someone@example.com')
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()