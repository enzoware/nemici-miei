import pygame
import assets
from settings import GRANDEZZA_TILES

class Npc:
    def __init__(self, tile_x, tile_y, mondo, finestra, image):
        self.mondo = mondo
        self.finestra = finestra
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.parlando = False
        img = image
        sx, sy = self.mondo.tile_to_screen(tile_x, tile_y)
        bottom_center = (sx + GRANDEZZA_TILES // 2, sy + GRANDEZZA_TILES)  
        self.scale_factor = 1
        new_size = (int(GRANDEZZA_TILES/2), int(GRANDEZZA_TILES * self.scale_factor))
        self.image = pygame.transform.scale(img, new_size)
        self.rect = self.image.get_rect(midbottom=bottom_center)
    
    def update(self):
        self.finestra.blit(self.image, self.rect)
