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
   print (axis)

   button = joystick.get_button(0)
   
   if button == 1:
      done == True

pygame.quit ()
