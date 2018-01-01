# implementation of card game - Memory

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

list1 = []
list2 = []
exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
state = 0
is_same_click = False
card1_idx = 0
card2_idx = 0
turns = 0

# helper function to initialize globals
def new_game():
    global list1,list2,state,is_same_click,exposed,turns
    list1 = range(8)
      
    #print list1
    list2 = range(8)
        
    #print list2
    list1.extend(list2)
    random.shuffle(list1)
    #print list1
    state = 0
    is_same_click = False
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    turns = 0
    label.set_text("Turns = "+ str(turns))
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    card_idx = 0
    global state, is_same_click, card1_idx,card2_idx, turns
    
##    for i in range(len(list1)):
##        if pos[0] >= 50*i and pos[0] < 50+i*50:
    
    i = pos[0]/50
    
    if exposed[i] == False:
        exposed[i] = True
        card_idx = i
        is_same_click = False
    else:
        is_same_click = True
    
    if not is_same_click:
        if state == 0:
            state = 1
            card1_idx = card_idx
        elif state == 1:
            state = 2
            card2_idx = card_idx
            turns += 1
            label.set_text("Turns = "+ str(turns))
        else:
            
            if not (list1[card1_idx] == list1[card2_idx]):
                exposed[card1_idx] = False
                exposed[card2_idx] = False
##                for i in range(len(list1)):
##                    if (i == card1_idx) or (i == card2_idx):
##                        exposed[i] = False
            state = 1
            card1_idx = card_idx
                
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(len(list1)):
        if exposed[i]:
            canvas.draw_text(str(list1[i]),[25+50*i,50],20,"White")
        else:
            canvas.draw_line([25+ 50*i,0],[25 + 50*i,100],50,"Green")
        
        canvas.draw_line([50+ 50*i,0],[50 + 50*i,100],1,"White")
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
