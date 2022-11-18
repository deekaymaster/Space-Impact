import pygame
from Bullet import Bullet
from pygame import mixer
import game_module as gm


class SpaceShip(pygame.sprite.Sprite):
    BREAK = 20  # min. czas w ms pomiędzy wystrzałem pocisku

    def __init__(self, x, y, image, speed, bullet_speed, lives):
        super().__init__()
        self.image = image  # obrazek statku
        self.rect = self.image.get_rect()  # zwraca prostokąt zawierający obrazek, czyli obiekt Rect
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)  # tworzymy maske statku
        self.speed = speed  # "szybkość" statku, tzn. o ile px statek sie przesunie
        self.lives = lives  # ilość żyć statku
        self.bullet_speed = bullet_speed
        self.bullets = []  # lista wystrzelonych pociskow
        self.counter = 0  # pomocnicza do odmierzania czasu

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        for bullet in self.bullets:
            bullet.draw(surface)

    def countdown(self):
        if self.counter >= self.BREAK:  # jesli minelo 20 ms
            self.counter = 0  # zerujemy licznik
        elif self.counter > 0:  # jesli odliczamy pomiedzy strzalami
            self.counter += 1  # zwiekszamy licznik

    def shoot(self):
        if self.counter == 0:  # mozna oddac strzal gdy licznik wyzerowany
            bullet = Bullet(self.rect.centerx, self.rect.centery, gm.PLAYER_FIRE)
            self.bullets.append(bullet)
            self.counter = 1
            mixer.Sound('audio/laser.wav').play()  # dzwiek przy strzale gracza
