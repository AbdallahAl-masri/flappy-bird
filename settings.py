import pygame
from pygame import mixer
pygame.init()

win_height = 720
win_width = 800

# Images
bird_images = [pygame.image.load("images/bird_down.png"),
                       pygame.image.load("images/bird_mid.png"),
                       pygame.image.load("images/bird_up.png")]

skyline_image = pygame.image.load("images/background.png")
skyline_image = pygame.transform.scale(skyline_image, (win_width, win_height))

ground_image = pygame.image.load("images/ground.png")
ground_image = pygame.transform.scale(ground_image, (win_width, win_height))

top_pipe_image = pygame.image.load("images/pipe_top.png")

bottom_pipe_image = pygame.image.load("images/pipe_bottom.png")

game_over_image = pygame.image.load("images/game_over.png")

# Game
scroll_speed = 2
bird_start_position = (100, 250)
font = pygame.font.SysFont('Segoe', 26)
game_stopped = True

# Sounds
sound_jump = mixer.Sound('sounds/flappy_whoosh.mp3')
