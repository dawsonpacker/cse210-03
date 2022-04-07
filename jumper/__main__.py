'''
Authors:
Logan Crossley
John Pischke
Seth Whetten
Dawson Packer 

Description:
This is our main function. Our main function should create a director
object. Main should then call the functions of the director object to
run the game. 
'''
from game.director import Director;

def main ():
    director = Director()
    director.start_game()

main()