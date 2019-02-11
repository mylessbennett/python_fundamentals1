secret_number = 42
user_number = int(input("Guess the secret number: "))

if user_number == secret_number:
    print("You win!")
elif user_number == secret_number - 1 or user_number == secret_number + 1:
    print("So close!")
else:
    print("Try again.")
