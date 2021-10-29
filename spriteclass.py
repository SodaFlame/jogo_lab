import pygame

class spritesheet():
    def __init__(self, img):
        self.sheet = img
        
    def get_sprite(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), ((frame*width), 0, width, height))   #pega a foto e bota na tela, os segundos argumentos falarm aonde comecar e aonde terminar a foto
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        
        return image
       

    