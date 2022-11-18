import pygame
import game_module as gm


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.center = [x, y]
        self.speed = 4
        self.mask = pygame.mask.from_surface(self.image)  # tworzymy maske pocisku

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, speed):
        self.rect.x += speed

    def off_screen(self):
        return not (0 <= self.rect.x <= gm.WIDTH)
