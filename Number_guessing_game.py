import random

x = random.randint(1, 100)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

tries = []

while True:
    guess = int(input("Take a guess: "))

    tries.append(guess)
    if guess in tries[:-1]:
        print("You already guessed that number. Try again.")
        continue
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if guess - x < -10:
        print("Your guess is too low.")
    elif guess - x > 10:
        print("Your guess is too high.")
    elif 0 > guess - x > -10:
        print("Close! But still too low.")
    elif 0 < guess - x < 10:
        print("Close! But still too high.")
    elif 0 > guess - x > -5:
        print("Almost got it! Just a little too low.")
    elif 0 < guess - x < 5:
        print("Almost got it! Just a little too high.")
    else:
        print("Congratulations! You've guessed the number.")
        print(f"The number was {x}.")
        print(f"It took you {len(tries)} tries.")
        tries.clear()

        cont = input('''Do you want to continue? 
(Press enter to continue or type 'N' to stop): ''')
        if cont.lower() in ["n", "no", "stop"]:
            print("Thanks for playing!")
            break
