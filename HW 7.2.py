secret = 52
guess = int(input("guess the secret number: "))

if guess == secret:
    print("Congratulation! You win!")

elif guess < secret:
    print("Wrong number! You need to go up!")

else:
    print("Wrong number! You need to go down!")