import pygame
import random
import game_module as gm


class Level:
    def __init__(self, player, image):
        self.player = player
        self.opponents_spaceships = []
        self.background_image = image.convert()
        self.victory_level = False

    def draw_background(self, screen):
        # tło obrazkowe
        screen.blit(self.background_image, [0, 0])

    def update(self):
        if len(self.opponents_spaceships) == 0:
            self.victory_level = True
            print("wygrałeś")

    def draw(self, screen):
        # przeciwnicy
        for opponent in self.opponents_spaceships:
            if len(self.opponents_spaceships) == 1 and opponent.rect.x <= (gm.WIDTH - gm.OPPONENT_BOSS.get_width() - 50):  # jesli został tylko BOSS i "dojedzie" do prawej krawędzi
                print(opponent.rect.y)
                self.opponents_spaceships[0].boss_move()
            else:
                opponent.draw(screen)
                opponent.move()
                opponent.move_bullets(opponent.bullet_speed, self.player)
                # prawdopodobieństwo oddania strzału przez przeciwnika
                if random.randrange(0, 2 * 70) == 1:  # losowana liczba od 1 do 2 * liczba FPS
                    opponent.shoot()

                if opponent.rect.x <= 0:
                    self.player.lives -= 1
                    self.opponents_spaceships.remove(opponent)

        # CZCIONKA
        score_font = pygame.font.SysFont("Verdana", 20)
        # wypisanie na ekranie gry ilości żyć, poziomu i punktów
        points_label = score_font.render(f"Points: {self.player.points}", 1, (255, 255, 255))
        screen.blit(points_label, (gm.WIDTH - points_label.get_width() - 10, 10))
        # rysowanie żyć(serduszek)
        for i in range(self.player.lives):
            screen.blit(gm.HEART, [10 + 40 * i, 10])
