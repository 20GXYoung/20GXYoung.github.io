import os
import random

with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    word_list = [line.strip() for line in f]


def interface():
    pass
    
def get_random_word():
    word = random.choice(word_list)
    print(word)
    # e_word = list(enumerate(word))
    


def hangman():
    get_random_word()
    

def run():
    hangman()


if __name__ == "__main__":
    run()