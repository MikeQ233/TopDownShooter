import pygame
from typing import List
import random


class Grid(pygame.sprite.Sprite):
    def __init__(self, position, image, size=(36, 36), is_safe_grid=False):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface(size)
        # self.image.fill(color)
        self.image = image
        self.image = pygame.transform.scale(self.image, (36, 36))
        self.rect = self.image.get_rect()
        self.rect.center = position


    def set_type(self):
        pass

    def get_center(self):
        return self.rect.center


class Boundary(pygame.sprite.Sprite):
    def __init__(self, position, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = position


class Obstacle(Grid):

    def __init__(self, position, image):
        Grid.__init__(self, position, image)
        self.image = pygame.transform.scale(self.image, (36, 36))


class Wall:

    width: int
    height: int
    sprites: List[Obstacle]

    def __init__(self, shape):
        self.obstacles = shape
        self.width = 0
        self.height = 0
        for item in shape:
            self.width = max(self.width, item[0])
            self.height = max(self.height, item[1])

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_obstacle(self, init_position, size: int, image):
        sprite = []
        x = init_position[0]
        y = init_position[1]

        for item in self.obstacles:
            v_x, v_y = item[0], item[1]
            sprite.append(Obstacle((x + v_x * size, y + v_y * size), image))

        return sprite


