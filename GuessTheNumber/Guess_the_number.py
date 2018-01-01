try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

secret_number = 0
no_of_guesses = 0
range_max = 100


# helper function to start and restart the game
def new_game():
    global no_of_guesses, secret_number
    print ""
    print "***************************"
    print "New Game. The range is 0 to "+str(range_max-1)
    no_of_guesses = int(math.ceil(math.log(range_max,2)))
    secret_number = random.randrange(0,range_max)
    #print "*** Secret number is "+str(secret_number)+" ***"
    print "number of guesses left: "+str(no_of_guesses)


# event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_max
    range_max = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_max
    range_max = 1000
    new_game()
   
   
    
def input_guess(guess):
    global no_of_guesses, secret_number
    print ""
    print "The guess is " + guess
    no_of_guesses -= 1
    if no_of_guesses == 0 and int(guess) != secret_number:
        print "Game over. You lose!"  
        new_game()
    elif int(guess) < secret_number:
        print "Higher!"
        print "number of guesses left: "+str(no_of_guesses)
    elif int(guess) > secret_number:
        print "Lower!"
        print "number of guesses left: "+str(no_of_guesses)
    else:
        print "Correct!"  
        new_game()
        
    
frame = simplegui.create_frame("GTN",200,200)
# register event handlers for control elements and start frame
frame.add_button("0 to 100",range100,100)
frame.add_button("0 to 1000]",range1000,100)
frame.add_input("Enter your guess",input_guess,100)
frame.start()

new_game()

