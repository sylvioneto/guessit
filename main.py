import gallow
import guessit

print("***************************")
print("Choose a game")
print("***************************")

print("1 - Guess it")
print("2 - Gallows")

game = input("What game? ")

if game == "1":
    print("Guess it selected")
    gallow.play()
elif game == "2" :
    print("Gallows selected")
    guessit.play()