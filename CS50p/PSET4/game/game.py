import random


while True:
    level = input("Level: ")
    game = random.randint(1, 100)
    try:
        if int(level) >= 1:
            guess = input("Guess: ")
        if int(guess) >= 1:
            if int(guess) < game:
                print("Too small!")
            elif int(guess) > game:
                print("Too large!")
            else:
                print("Just right!")
                break
    except (ValueError, NameError):
        pass
