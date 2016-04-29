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
    
    for event in pygame.event.get():
        
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            done = True
            
    joystick_count = pygame.joystick.get_count()

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        name = joystick.get_name()
        
        axes = joystick.get_numaxes()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            if i == 2:
                if axis < 0:
                    pw = MIN_PW
                else:
                    pw = MAX_PW
                    print("test")
            
        buttons = joystick.get_numbuttons()
        
        for i in range( buttons ):
            button = joystick.get_button( i )
            
        hats = joystick.get_numhats()
        
        for i in range( hats ):
            hat = joystick.get_hat( i )
    
pygame.quit ()
