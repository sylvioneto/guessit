# author: sylvio.pedroza@gmail.com
import random

print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = random.randrange(1, 101);
no_tentatives = 0

print("What difficult level you want to play?")
print("(1) Easy, (2) Medium, (3) Hard")
game_level = input("Level: ")

if game_level == "1":
    no_tentatives = 10
elif game_level == "2":
    no_tentatives = 6
elif game_level == "3":
    no_tentatives = 3

for round in range(1, no_tentatives + 1):
    print("Tentatives {} of {} ".format(round, no_tentatives))

    user_input = input("Type a number between 1 and 100: ")
    if len(user_input) == 0:
        continue

    user_input = int(user_input)
    print("You typed ", user_input)

    if user_input < 1 or user_input > 100:
        print("Number out of the range ", user_input)
        continue # go to next iteration

    user_won = user_input == secret_number
    higher = user_input > secret_number
    lesser = user_input < secret_number

    if(user_won):
        total_points = (no_tentatives - round) * 10
        print("You won! :) Total points: ", total_points)
        break #step out the loop
    else:
        if(higher):
            print("You guess was higher")
        elif(lesser):
            print("You guess was lesser")

print("The secret number was {}".format(secret_number))

print("End of game")