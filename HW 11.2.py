import random
import json
import datetime

name = str(input("What's your name?"))

current_time = datetime.datetime.now()

print(current_time)

secret = random.randint(1, 1000)

attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:
    print("Top scores: " + (str(score_dict.get("attempts")) + " attempts, date: " + str(score_dict.get("date"))
          + ", name: " + str(score_dict.get("name")) + ", number was: " + str(score_dict.get("secret"))))

while True:
    guess = int(input("guess the secret number (1-1000): "))

    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "name": str(name), "secret": str(secret)})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Congratulation! You win!")
        print("Attempts needed: " + str(attempts))
        break

    elif guess < secret:
        score_list.append({"wrong_guesses": [guess]})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Wrong number! You need to go up!")
    else:
        score_list.append({"wrong_guesses": [guess]})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Wrong number! You need to go down!")