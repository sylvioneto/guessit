# author: sylvio.pedroza@gmail.com
import random

import file_handler

def play():
    print("***************************")
    print("Welcome to the hanging game")
    print("***************************")

    # local variables
    is_hanged = False
    is_won =  False
    max_tentatives = 10
    errors = 0;

    file = file_handler.get_file("words.txt")
    secret_word = file.readlines()[random.randrange(0, 5)].strip().upper()
    file.close()

    # masked word
    masked_word = ["_" for l in secret_word]

    # loop while user does not win the game
    while(not is_hanged and not is_won):
        print(masked_word)
        guessing = input("Letter : ").strip().upper()

        index_list = get_positions(secret_word, guessing)
        for position in index_list:
            masked_word[position] = guessing
            print("Letter found in {}".format(position))

        if masked_word.count("_") == 0:
            is_won = True

        max_tentatives=max_tentatives-1
        if max_tentatives == 0:
            is_hanged = True

    if is_hanged:
        print("You lost")

    if is_won:
        print("You win")
        print(masked_word)

    print("*******End of Game*********")


# method to search a letter in a string
def get_positions(word, letter):
    index_list = []
    index = 0
    for l in word:
        if(l == letter):
            index_list.append(index)
        index = index + 1
    return index_list;


# in case of this class execution directly
if __name__ == "__main__":
    play()