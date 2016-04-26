#inits

#servo
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

#joystick
import pygame
pygame.init()
done = False

pygame.joystick.init()


#main loop

while done==False: #marcator final loop
    
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONUP:
            done=True

    joystick_count = pygame.joystick.get_count()

    for i in range (joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        axes = joystick.get_numaxes()

        for i in range ( axes ):
            axis = joystick.get_axis( i )
            if i == 2:
                duty = ((float(axis)+1)/2)*17.5+3
                pwm.ChangeDutyCycle(duty)
                print(duty)

pygame.quit ()
