import random


print("welcome to the number guessing game!\n you have 5 attempts guess the   number between 50 to 100" )

number_to_guess = random.randrange(50, 100)

chances = 5
 
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("enter your guess:"))
    
    if my_guess == number_to_guess:
        print(f"you guessed the numnber is{number_to_guess} and you found it in {guess_counter} attempts")
        break
    elif guess_counter >= chances:
        print(f"sorry you have used all your chances")
        break
    elif my_guess< number_to_guess:
        print("you guessed a lower number")
    elif my_guess> number_to_guess:
        print("you guseeed a higher number")
    else:
        print("invalid input")
        