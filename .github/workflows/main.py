import pygame
from time import sleep
print("Everyone is fucker untill the real fucker arrived!")
sleep(3)
pygame.init()
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('wakeuptoreality.mp3')
pygame.mixer.music.play()
sleep(34)
image = pygame.image.load('scr.jpeg')
window.blit(image, (0,0))
pygame.display.update()
sleep(3)
