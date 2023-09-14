def main():
    text = input("Input: ")
    print(value(text))

def value(greeting):
    greeting = greeting.lower()
    greeting = greeting.replace(" ", "")
    if "hello" in greeting:
        return "$0"
    elif greeting.find("h") == 0:
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()