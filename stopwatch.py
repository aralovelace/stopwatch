# template for "Stopwatch: The Game"

# define global variables
import simplegui

# define helper function format that converts time

timer = ""
width = 500
height = 500
interval= 100

position = [50, 70]
position_attempts = [150, 30]
minutes = 0
seconds = 0

timer=None
time=0
display="0:00.0"
trials=0
success=0
started=False





# in tenths of seconds into formatted string A:BC.D
def format(t):
    global display
    tenthseconds=t%10
    sec=t/10
    minutes=int(sec/60)
    seconds=int(sec%60)    
    display =str(minutes)+":"+('%02d' % seconds)+"."+str(tenthseconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def stop_button():
    timer.stop()
    global trials
    global success
    global label
    global started
    if started:
        if time%10==0:
            success=success+1
        started=False
        trials=trials+1
    
def start_button():
    timer.start()
    global started
    started=True
    
def reset_button():
    global time
    global started
    global trials
    global success
    started=0
    trials=0
    success=0
    timer.stop()
    time=0
    format(time)

# define event handler for timer with 0.1 sec interval
def increment_time():
    global time
    time=time+1
    format(time)
    
   
              
# define draw handler
def draw(canvas):
    
    canvas.draw_text(display, position, 40, "white")
    canvas.draw_text(str(success)+"/"+str(trials), position_attempts, 20, "Red")
    
    
# create frame
frame = simplegui.create_frame("Home", width, height)



# register event handlers

frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, increment_time)
start = frame.add_button('Start', start_button,100)
stop = frame.add_button('Stop', stop_button,100)
reset = frame.add_button('Reset', reset_button,100)
# start frame
frame.start()

# Please remember to review the grading rubric
