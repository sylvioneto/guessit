# author: sylvio.pedroza@gmail.com
import random

print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = random.randrange(1, 101);
no_tentatives = 3

for rodada in range(1, no_tentatives+1):
    print("Tentatives {} of {} ".format(rodada, no_tentatives))

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
        print("You won! :)")
        break #step out the loop
    else:
        if(higher):
            print("You guess was higher")
        elif(lesser):
            print("You guess was lesser")

print("The secret number was {}".format(secret_number))

print("End of game")