
from gpiozero import LightSensor, PWMLED
from gpiozero import Buzzer
buzz = Buzzer (22)
#import pygame

ldr=LightSensor(4)
#print(ldr.value)


while True:
    ldr.wait_for_light()
    
    print("It's light :)")
    ldr.wait_for_dark()
    buzz.beep(0.2,0.2,5
              )
    print("It's dark :(")
   
#ldr.when_dark = lambda: buzz.beep(0.2, 0.2, )
#ldr.when_light = buzz.off()







buzz.off()


#import pygame
#pygame.init()

#my_sound = pygame.mixer.Sound('path/to/my/soundfile.wav')

#my_sound.play()



