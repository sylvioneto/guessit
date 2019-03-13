print("*****************************")
print("Welcome to the guessing game!")
print("*****************************")

secret_number = 35

user_input = int(input("Type a number: ", ))
print("You typed ", user_input)

if(user_input == secret_number):
    print("You won! :)")
else:
    print("You lost! :(")