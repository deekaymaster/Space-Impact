import pygame
import random
from SpaceShip import SpaceShip
from Bullet import Bullet
import game_module as gm
from pygame import mixer


class OpponentSpaceShip(SpaceShip):

    def __init__(self, x, y, image, speed, bullet_speed, lives, player):
        super().__init__(x, y, image, speed, bullet_speed, lives)
        self.player = player
        self.slide_up = False  # flaga pomocnicza dla ruchu gora/dol bossa

    def move(self):
        self.rect.x -= self.speed

    def boss_move(self):
        min = 35  # górna granica na osi y
        max = gm.HEIGHT-gm.OPPONENT_BOSS.get_height()  # dolna granica na osi y
        # jeśli boss dotknie pkt krancowych to zmiana flagi
        if self.rect.y == min:
            self.slide_up = False
        elif self.rect.y == max:
            self.slide_up = True
        # przesuwanie bossa w zaleznosci od flagi
        if self.slide_up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        self.draw(self.player.screen)
        self.move_bullets(self.bullet_speed, self.player)
        if random.randrange(0, 2 * 70) == 1:  # losowana liczba od 1 do 2 * liczba FPS
            self.shoot()

    def move_bullets(self, vel, player_spaceship):
        self.countdown()  # odliczamy pomiedzy seriami strzalu
        for bullet in self.bullets:
            bullet.move(-vel)  # -vel bo przeciwnik strzela w przeciwna strone niz gracz
            if bullet.off_screen():
                self.bullets.remove(bullet)
            else:
                if pygame.sprite.collide_mask(bullet, player_spaceship):
                    print("raniony!")
                    player_spaceship.lives -= 1
                    mixer.Sound('audio/sfx_lose.ogg').play()  # dzwiek przy trafieniu gracza
                    self.bullets.remove(bullet)

    def shoot(self):
        if self.counter == 0:  # mozna oddac strzal gdy licznik wyzerowany
            bullet = Bullet(self.rect.centerx, self.rect.centery, gm.OPPONENT_FIRE)
            self.bullets.append(bullet)
            self.counter = 1
