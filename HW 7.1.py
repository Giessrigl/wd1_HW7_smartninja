

for x in range(5):
    mood = input("what's your mood: ")

    if mood == "happy":
        print("It is great to see you happy!")

    elif mood == "nervous":
        print("Take a deep breath 3 times.")

    elif mood == "sad":
        print("Cheer up, mate!")

    elif mood == "excited":
        print("Keep calm and write python code!")

    elif mood == "relaxed":
        print("I don´t know what to say^^")

    else:
        print("I don´t recognize this mood")

    question = input("Has your mood changed? (y/n)  ")

    if question == "n":
        break