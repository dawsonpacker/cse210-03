'''
Authors:
Logan Crossley
John Pischke
Seth Whetten
Dawson Packer 

Description:
This is our jumper class. this class is meant to keep track of misses as well as send the correct graphic.
'''
from game.terminal import Terminal;

class Jumper:
    
    def __init__(self):
        self._graphic_parts = [
            '  ___\n /___\\\n \\   /\n  \\ /\n   0\n',
            '     \n /___\\\n \\   /\n  \\ /\n   0\n',
            '     \n  ___\\\n \\   /\n  \\ /\n   0\n',
            '     \n  ___  \n \\   /\n  \\ /\n   0\n',
            '     \n       \n \\   /\n  \\ /\n   0\n',
            '     \n       \n     /\n  \\ /\n   0\n',
            '     \n       \n      \n  \\ /\n   0\n',
            '     \n       \n      \n    /\n   0\n',
            '     \n       \n      \n     \n   x\n'
        ]
        self._end_graphic = '  /|\\\n  / \\\n\n^^^^^^^'
        self._miss_count = 0

    # adjusts the miss count
    def adjust_miss_count(self):
        self._miss_count += 1
        pass

    # sends the correct graphic
    def send_graphic(self, terminal):
        terminal.print_to_terminal(self._graphic_parts[self._miss_count] + self._end_graphic + '\n')
        
    # returns the miss count
    def get_miss_count(self):
        return self._miss_count
