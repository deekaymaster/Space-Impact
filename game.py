import pygame
import os
import shelve
import game_module as gm
from Button import Button
from Level_1 import Level_1
from PlayerSpaceShip import PlayerSpaceShip
from pygame import mixer


os.environ["SDL_VIDEO_CENTERED"] = '1'  # wysrodkowanie okna na ekranie komputera

# otwieramy pulke na wyniki
shelf = shelve.open("results/results.dat", writeback=True)
print('wyniki =', shelf["results"])

pygame.init()  # inicjalizujemy wszystkie zaimportowane moduły pygame
pygame.font.init()  # inicjujemy czcionki
# definowanie okna gry
screen = pygame.display.set_mode(gm.SIZESCREEN)

# CZCIONKA
score_font = pygame.font.SysFont("Verdana", 20)
win_font = pygame.font.SysFont("Verdana", 45)
message_font = pygame.font.SysFont("Verdana", 40)

# Tytuł okna, gry i ikona gry
pygame.display.set_caption("Space Impact")
icon = gm.ICON
pygame.display.set_icon(icon)

# MUZYKA W TLE
mixer.music.load("audio/background.wav")
mixer.music.play(-1)  # -1, żeby zapetlalo

clock = pygame.time.Clock()  # tworzymy obiekt do śledzenia czasu
FPS = 70

# METODY STATYCZNE


def get_top_score(file):  # zwraca najlepszy(najwiekszy) wynik z pliku
    return max(file["results"])


# konkretyzacja obiektow
bullet_speed = 3
player_speed = 4
player_lives = 3
opponents_amount = 15
# GRACZ
player = PlayerSpaceShip(50, 321, gm.PLAYER_SPACE_SHIP, player_speed, bullet_speed, player_lives, screen)
# LEVELS
current_level = Level_1(player, opponents_amount, gm.BACKGROUND_1)
player.level = current_level

# MENU STARTOWE

startButton = Button("START GAME", 400, 150, (255, 255, 255), (0, 0, 0),
                     gm.WIDTH // 2, gm.HEIGHT // 2, size=35, font_type='Verdana')

window_open = True
active_game = False
pause_game = False


# pętla główna gry
while window_open:
    # tło obrazkowe
    current_level.draw_background(screen)
    # obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_level.player.save_result(shelf)
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                active_game = False
                pause_game = True
                pygame.mouse.set_visible(True)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mixer.Sound('audio/click.mp3').play()  # dzwiek klikniecia
            if startButton.rect.collidepoint(pygame.mouse.get_pos()):
                active_game = True
                pause_game = False
                pygame.mouse.set_visible(False)
                pygame.time.delay(500)
                startButton.set_text("RETURN GAME")
                startButton.image = startButton.font.render(startButton.text, 1, startButton.text_colour,
                                                            startButton.background_colour)
    if current_level.player.lose:
        mixer.music.stop()
        mixer.Sound('audio/gameover.mp3').play()  # dzwiek game over
        message_label = message_font.render("GAME OVER", 1, (255, 255, 255))
        # blit() rysuje jeden obrazek na drugim, parametry: źródło, cel.
        screen.blit(message_label, (gm.WIDTH / 2 - message_label.get_width() / 2, 350))
        pygame.display.flip()  # pokaż to co wcześniej narysowaliśmy

    elif active_game and not pause_game and not current_level.victory_level:

        # KONIEC ŻYĆ GRACZA
        if current_level.player.lives <= 0:
            current_level.player.lose = True
            continue

        current_level.player.move_bullets(bullet_speed, current_level.opponents_spaceships)  # ruch pociskow gracza
        current_level.player.collision(current_level.opponents_spaceships)  # wykrywanie kolizji gracza z przeciwnikiem
        current_level.player.get_event()  # zczytywanie eventow z klawiatury

        # rysowanie i aktualizacja obiektów

        current_level.update()
        current_level.draw(screen)
        current_level.player.draw(screen)

    elif current_level.victory_level:  # jeżeli wygrana
        # wypisanie na ekranie wyników
        mixer.music.stop()
        mixer.Sound('audio/victory.mp3').play()  # dzwiek fanfar
        win_label = win_font.render(f"YOU WIN!!!", 1, (255, 255, 255))
        your_score_label = score_font.render(f"Your score: {current_level.player.points}", 1, (255, 255, 255))
        top_score_label = score_font.render(f"TOP score: {get_top_score(shelf)}", 1, (255, 255, 255))
        screen.blit(your_score_label, (gm.WIDTH - your_score_label.get_width() - 10, 10))
        screen.blit(top_score_label, (10, 10))
        screen.blit(win_label, (gm.WIDTH / 2 - win_label.get_width() / 2, 350))
    else:  # wyswietlanie menu
        startButton.draw(screen)
        # wypisanie na ekranie wyników
        your_score_label = score_font.render(f"Your score: {current_level.player.points}", 1, (255, 255, 255))
        top_score_label = score_font.render(f"TOP score: {get_top_score(shelf)}", 1, (255, 255, 255))
        screen.blit(your_score_label, (gm.WIDTH - your_score_label.get_width() - 10, 10))
        screen.blit(top_score_label, (10, 10))

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(FPS)  # kontroluje ile milisekund upłynęło od poprzedniego wywołania

# zamknięcie półki
shelf.close()
pygame.quit()
