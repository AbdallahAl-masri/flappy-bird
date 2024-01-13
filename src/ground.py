import pygame
from settings import *
from pygame.sprite import Sprite

class Ground(Sprite):
    def __init__(self, x, y):
        super(Ground, self).__init__()
        self.image = ground_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Move Ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -win_width:
            self.kill()
