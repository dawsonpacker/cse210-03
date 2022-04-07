'''
Authors:
Logan Crossley
John Pischke
Seth Whetten
Dawson Packer 

Description:
This is our director class. The director in in charge of running the game. The director starts the game, gets inputs, updates, and does the outputs.
'''
from game.jumper import Jumper;
from game.puzzle import Puzzle;
from game.terminal import Terminal;
import re;

class Director:
    
    def __init__(self):
        self._is_playing = False
        self._word_list = []
        self._puzzle = Puzzle()
        self._terminal = Terminal()
        self._jumper = Jumper()
        self._max_miss_count = 8
        
    # starts game
    def start_game(self):
        self._is_playing = True
        word_len = self._puzzle.create_word()
        self._word_list = ['-']*word_len

        self._print_board()
        self._jumper.send_graphic(self._terminal)

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    # receives valid input
    def _get_inputs(self):
        self._guess = input('Guess a letter [a-z]: ').lower()
        while not re.search("[a-z]", self._guess) or len(self._guess) != 1:
            print('Invalid input: Please enter a letter')
            self._guess = input('Guess a letter [a-z]: ').lower()    

    # updates the miss_count and word_list
    def _do_updates(self):
        index_list = self._puzzle.check_guess(self._guess)
        if index_list[0] == -1:
            self._jumper.adjust_miss_count()
        else:
            for item in index_list:
                self._word_list[item] = self._guess

    # prints the board and updates is_playing
    def _do_outputs(self):
        self._print_board()
        self._jumper.send_graphic(self._terminal)

        if ''.join(self._word_list) == self._puzzle.get_word():
            self._is_playing = False

        if self._jumper.get_miss_count() >= self._max_miss_count:
            self._is_playing = False

    # prints the current board
    def _print_board(self):
        board_string = '\n'
        for item in self._word_list:
            board_string += item + ' '
        self._terminal.print_to_terminal(board_string)
        
