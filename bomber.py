import pygame
import random

BLACK = (0, 0, 0)
# Clase Bomberman
class Bomberman:
    def __init__(self, name, x, y):
        self.name = name
        self.updown = random.uniform(-1, 1)
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, 24)
        pygameSurface = pygame.image.load('bombi.png').convert_alpha()
        self.image = pygameSurface

        # Dibuja el texto en la burbuja
        self.text = self.font.render(self.name, True, BLACK)
    
    def draw(self, screen):
        # Dibujar bomberman
        screen.blit(self.image, (self.x, self.y))
        padding = 10

        screen.blit(self.text, (self.x - 10, self.y - 15))

    def falling(self):
        self.y += (0.005*self.updown) 

    def is_clicked(self, pos):
        rect = pygame.Rect(self.x, self.y, 50, 50)
        return rect.collidepoint(pos)
    
    def move_to_right(self):
        self.x += 0.03
        
    def set_image(self, img):
        pygameSurface = pygame.image.load(img).convert_alpha()
        self.image = pygameSurface