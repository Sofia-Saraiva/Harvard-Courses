def main():
    text = input()
    print(emoji(text))

def emoji(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

main()
