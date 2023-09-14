def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Check for invalid characters and length of plate
    if s.isalnum() == False or len(s) < 2 or len(s) > 6:
        return False

    # Check if it starts with 2 letters
    if s[0].isalpha() == False and s[1].isalpha() == False:
        return False

    # Check if number is 0
    temp = ""
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            temp += s[i]
            if temp[0] == "0":
                return False

    # Check if there is number in the middle
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False

    return True


main()
