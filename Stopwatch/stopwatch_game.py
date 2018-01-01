# "Stopwatch: The Game"
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define global variables
counter_time = 0
attempts = 0
successes = 0
seconds_decimal = 0
is_timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global seconds_decimal
    time = t*0.1
    minutes = int(time//60)
    seconds = int(time-minutes*60)
    seconds_decimal = int(10*((time-minutes*60) - seconds))
    
#    print "t: "+str(t)
#    print "time: "+str(time)
#    print "minutes: "+ str(minutes)
#    print "seconds: "+ str(seconds)
#    print "seconds_decimal: "+str(seconds_decimal)
    
    if seconds <10:
        return str(minutes)+":0"+str(seconds)+"."+str(seconds_decimal)
    else:
        return str(minutes)+":"+str(seconds)+"."+str(seconds_decimal)
    
       
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def btn_start():
    global is_timer_running
    timer.start()
    is_timer_running = True
    
def btn_stop():
    global attempts, successes, is_timer_running
    timer.stop()
    
    if is_timer_running:
        attempts +=1
        if not seconds_decimal:
            successes +=1
    is_timer_running = False
    
    
def btn_reset():
    global counter_time, seconds_decimal, successes, attempts
    timer.stop()
    is_timer_running = False
    counter_time = 0
    attempts =0
    successes = 0
    

# define event handler for timer with 0.1 sec interval
def tick():
    global counter_time
    counter_time+=1
    

# define draw handler
def draw(canvas):
    #text = str(counter_time/10.0)
    text_time = format(counter_time)
    canvas.draw_text(text_time, [150,150],30,"Red")
    text_attempts = str(successes)+ "/"+ str(attempts)
    canvas.draw_text(text_attempts,[250,40],30,"Red")

    
# create frame
frame = simplegui.create_frame("SW",300,300)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start",btn_start,150)
frame.add_button("Stop",btn_stop,150)
frame.add_button("Reset",btn_reset,150)
timer = simplegui.create_timer(100,tick)

# start frame
frame.start()
