#joystick

import pygame

pygame.init()
 
done = False

pygame.joystick.init()


#servo

import time
import curses
import atexit
import pigpio

SERVO1 = 17
SERVO2 = 18

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

atexit.register(cleanup)

pulsewidth1 = MID_PW
pulsewidth2 = MID_PW

pi.set_servo_pulsewidth(SERVO1, pulsewidth1)
pi.set_servo_pulsewidth(SERVO2, pulsewidth2)

while done==False:
    pw1 = pulsewidth1
    pw2 = pulsewidth2

    pygame.event.get()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
           
    axis = joystick.get_axis( 1 )    
    pw1 = pw1 + axis * 0.2

    axis = joystick.get_axis( 3 )
    pw2 = pw2 + axis * 0.2

    if pw1 > MAX_PW:
        pw1 = MAX_PW
    elif pw1 < MIN_PW:
        pw1 = MIN_PW
        
    if pw2 > MAX_PW:
        pw2 = MAX_PW
    elif pw2 < MIN_PW:
        pw2 = MIN_PW

    if joystick.get_button(9) == 1:
        done = True
        
    #hats = joystick.get_numhats()
        
    #for i in range( hats ):
    #    hat = joystick.get_hat( i )

    if pw1 != pulsewidth1:
        pulsewidth1 = pw1
        pi.set_servo_pulsewidth(SERVO1, pulsewidth1)
        
    if pw2 != pulsewidth2:
        pulsewidth2 = pw2
        pi.set_servo_pulsewidth(SERVO2, pulsewidth2)
    
pygame.quit ()
