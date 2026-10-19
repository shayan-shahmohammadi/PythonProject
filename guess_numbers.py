import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess_number = input("Guess the number: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)

        if guess_number <= 100:
            attempts += 1

            if guess_number > secret_number:
                print("Higher number!")

            elif guess_number < secret_number:
                print("Lower number!")

            else:
                secret_number = guess_number
                print("You guessed the number!")
                print(f"You guessed the number in {attempts} attempts")
                break

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")