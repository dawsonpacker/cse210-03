'''
Authors:
Logan Crossley
John Pischke
Seth Whetten
Dawson Packer 

Description:
This is our puzzle class. The puzzle choses a word from wordlist and returns it size. The puzzle also can return the word chosen.
The puzzles main job is to check if the guess was correct or not and returns the index of where it was correct or if there are none correct.
'''
from game.word_list import word_list
import random
class Puzzle:
    
    def __init__(self):
        self._word = "word"

    # creates random word and returns length of word
    def create_word(self):
        self._word = random.choice(word_list)
        return len(self._word)

    # returns the word    
    def get_word(self):
        return self._word

    # checks the guess and returns where it is correct 
    def check_guess(self, guess):
        word = self._word

        times_letter_is_in_word = 0
        return_value = []
        for i in range(len(word)):
            letter = word[i]
            letter_index = i
            if guess == letter: 
                return_value.append(letter_index)
                times_letter_is_in_word += 1

        if times_letter_is_in_word == 0:
            return_value.append(-1)
        return(return_value)
