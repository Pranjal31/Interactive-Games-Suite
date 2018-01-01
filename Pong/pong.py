# Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# Global variables
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0,0]
ball_vel = [0,0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
        

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == "left":
        ball_vel = [-random.randrange(2,4),-random.randrange(1,3)]
        
    else:
        ball_vel = [random.randrange(2,4),-random.randrange(1,3)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    num = random.randrange(0,2)
    if num == 0:
        spawn_ball('left')
    elif num == 1:
        spawn_ball('right')

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
      
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    #gutter ball collision conditions    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and not((ball_pos[1] -BALL_RADIUS >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] - BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT) or (ball_pos[1] + BALL_RADIUS >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] + BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT) ):
        spawn_ball('right')
        score2 +=1
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and not((ball_pos[1] - BALL_RADIUS >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] - BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT) or (ball_pos[1] + BALL_RADIUS >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] + BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT) ):
        spawn_ball('left')
        score1 += 1
        
    #pad ball collision conditions
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS and ((ball_pos[1] -BALL_RADIUS >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] - BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT) or (ball_pos[1] + BALL_RADIUS >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] + BALL_RADIUS <= paddle1_pos + HALF_PAD_HEIGHT)):
        ball_vel[0] = -1.3 * ball_vel[0] 
    elif ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS and ((ball_pos[1] - BALL_RADIUS >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] - BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT) or (ball_pos[1] + BALL_RADIUS >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] + BALL_RADIUS <= paddle2_pos + HALF_PAD_HEIGHT)):
        ball_vel[0] = -1.3 * ball_vel[0] 

   
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,5,"White","White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos = paddle1_pos + paddle1_vel
    if paddle1_pos <= HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
        
    paddle2_pos = paddle2_pos + paddle2_vel
    if paddle2_pos <= HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT

    # draw paddles
    canvas.draw_line([0,paddle1_pos],[PAD_WIDTH,paddle1_pos], PAD_HEIGHT, 'White')
    canvas.draw_line([WIDTH-PAD_WIDTH,paddle2_pos],[WIDTH,paddle2_pos], PAD_HEIGHT, 'White')
    
    # draw scores
    canvas.draw_text(str(score1),[WIDTH/2-WIDTH/8,HEIGHT/4],40,"White")
    canvas.draw_text(str(score2),[WIDTH/2+WIDTH/8,HEIGHT/4],40,"White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 2
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 2
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 2
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 2
        
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += 2
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel -= 2
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel += 2
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel -= 2
        
def button_click():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",button_click,150)
new_game()
frame.start()
