import pygame
import os

SIZESCREEN = WIDTH, HEIGHT = 960, 740

PLAYER_SPACE_SHIP = pygame.image.load(os.path.join("images/PNG", "playerShip3_blue.png"))
PLAYER_FIRE = pygame.image.load(os.path.join("images/PNG/Effects", "fire03.bmp"))
OPPONENT_FIRE = pygame.image.load(os.path.join("images/PNG/Effects", "fire04.bmp"))
OPPONENT_BLACK_SPACE_SHIP = pygame.image.load(os.path.join("images/PNG/Enemies", "enemyBlack4.png"))
OPPONENT_BLUE_SPACE_SHIP = pygame.image.load(os.path.join("images/PNG/Enemies", "enemyBlue4.png"))
OPPONENT_GREEN_SPACE_SHIP = pygame.image.load(os.path.join("images/PNG/Enemies", "enemyGreen4.png"))
OPPONENT_RED_SPACE_SHIP = pygame.image.load(os.path.join("images/PNG/Enemies", "enemyRed4.png"))
OPPONENT_BOSS = pygame.image.load(os.path.join("images/PNG/Enemies", "boss.bmp"))
BACKGROUND_1 = pygame.image.load('images/Backgrounds/back1.png')
BACKGROUND_2 = pygame.image.load('images/Backgrounds/back2.png')
ICON = pygame.image.load(os.path.join("images/PNG", "playerShip1_red.png"))
HEART = pygame.image.load(os.path.join("images/PNG", "heart.png"))
