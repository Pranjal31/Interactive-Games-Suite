# GUI-based version of RPSLS
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
import random

# Functions that compute RPSLS
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1    
    
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    else:
        return "scissors"
        
    
def rpsls(inp):
    print ""
    print "Player chooses "+inp
    pc = name_to_number(inp)
    if pc == -1:
        print "Error: Bad input " + inp + " to rpsls"
        return None
    cc = random.randrange(0,5)
    computer_choice = number_to_name(cc)
    print "Computer chooses "+computer_choice
    if ((pc - cc) %5 == 1) or ((pc - cc) %5 == 2):
        print "Player wins!"
    elif ((pc - cc) %5 == 3) or ((pc - cc) %5 == 4):
        print "Computer wins!"
    else:
        print "It's a draw!"
        
    
# Handler for input field
def get_guess(guess):
    rpsls(guess)
    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test - Uncomment the below to run the test

#get_guess("Spock")
#get_guess("dynamite")
#get_guess("paper")
#get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
