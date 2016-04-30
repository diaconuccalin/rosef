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

SERVO = 18
aux=0

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

pulsewidth = MID_PW

pi.set_servo_pulsewidth(SERVO, pulsewidth)

while done==False:
    pw = pulsewidth

    pygame.event.get()
            
    joystick_count = pygame.joystick.get_count()

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
           
    axis = joystick.get_axis( 0 )
    
    pw = pw + axis * 0.2

    if pw > MAX_PW:
        pw = MAX_PW
    elif pw < MIN_PW:
        pw = MIN_PW

    if joystick.get_button(9) == 1:
        done = True
        
    #hats = joystick.get_numhats()
        
    #for i in range( hats ):
    #    hat = joystick.get_hat( i )

    if pw != pulsewidth:
        pulsewidth = pw
        pi.set_servo_pulsewidth(SERVO, pulsewidth)
    
pygame.quit ()
