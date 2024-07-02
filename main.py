import random

# top_of_range = int(input("Type a number: "))
#
#
# random_number = random.randint(-5, 11)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print('Please type a number next time.')
    quit()


random_number = random.randint(0,top_of_range)

guesses = 0

while True:
    guesses +=1
    user_guess = input("Make Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number: ")
        continue

    if user_guess == random_number:
        print("Yay! You got it right!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You below the number!")

print("you got it in", guesses, "guesses")