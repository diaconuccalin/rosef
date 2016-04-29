#servo

import time
import curses
import atexit

import pigpio

SERVO = 18

MIN_PW = 1000
MID_PW = 1500
MAX_PW = 2000

def cleanup():
   curses.nocbreak()
   curses.echo()
   curses.endwin()
   pi.stop()

pi = pigpio.pi()

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

atexit.register(cleanup) # Ensure original screen state is restored.

in_escape = False
in_cursor = False

pulsewidth = MID_PW

pi.set_servo_pulsewidth(SERVO, pulsewidth)



#joystick
import pygame
pygame.init()
done = False

pygame.joystick.init()


#main loop

while done==False:

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    axis = joystick.get_axis( 2 )
    
    if axis > 1:
        pw = MAX_PW
    else:
        pw = MIN_PW
        
    if pw != pulsewidth:
       pulsewidth = pw
       pi.set_servo_pulsewidth(SERVO, pulsewidth)

pygame.quit ()
