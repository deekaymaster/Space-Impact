import pygame
from SpaceShip import SpaceShip
import game_module as gm
from pygame import mixer


class PlayerSpaceShip(SpaceShip):
    def __init__(self, x, y, image, speed, bullet_speed, lives, screen):
        super().__init__(x, y, image, speed, bullet_speed, lives)

        self.level = None
        self.points = 0
        self.lose = False
        self.screen = screen

    def move_bullets(self, vel, opponent_spaceships):
        self.countdown()  # odliczamy pomiedzy seriami strzalu
        for bullet in self.bullets:
            bullet.move(vel)
            if bullet.off_screen():
                print("poza")
                self.bullets.remove(bullet)
            else:
                for o in opponent_spaceships:
                    if pygame.sprite.collide_mask(bullet, o):  # kolizja oparta na masce obiektów
                        print("trafiony")
                        o.lives -= 1  # zmniejszamy zycia przeciwnika
                        if o.lives == 0:  # jesli przeciwnik nie ma juz zyc to usuwamy go
                            mixer.Sound('audio/explosion.wav').play()  # dzwiek przy wybuchu
                            opponent_spaceships.remove(o)
                        #pygame.time.delay(20)
                        self.bullets.remove(bullet)
                        self.points += 1

    def collision(self, opponent_spaceships):  # wykrywanie kolizji statku gracza z przeciwnikiem
        for o in opponent_spaceships:
            if pygame.sprite.collide_mask(self, o):  # kolizja oparta na masce obiektów
                self.lives -= 1
                opponent_spaceships.remove(o)
                mixer.Sound('audio/sfx_lose.ogg').play()
                mixer.Sound('audio/explosion.wav').play()  # dzwiek wybuchu

    def go_up(self):
        self.rect.y -= self.speed

    def go_down(self):
        self.rect.y += self.speed

    def get_event(self):
        # ruch w pionie
        keys = pygame.key.get_pressed()  # zwraca nam tablice wszystkich przycisków
        if keys[pygame.K_UP] and self.rect.y - self.speed > 35:  # na osi y większe od 35, bo nie gramy gdzie napisy
            self.go_up()  # ruch do góry
        if keys[pygame.K_DOWN] and self.rect.y + self.speed + self.rect.height < gm.HEIGHT:
            self.go_down()  # ruch w dół
        if keys[pygame.K_LCTRL]:
            self.shoot()

    # zapisujemy do pliku wynik gracza
    def save_result(self, file):
        # dodani wyniku gracza do półki
        file["results"].append(self.points)
        # zapisanie/aktualizacja stanu półki
        file.sync()
