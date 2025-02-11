import pygame
from datetime import datetime
from pygame.locals import *
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 700
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moon Threads")

font = pygame.font.SysFont("Castellar", 70)
font_score = pygame.font.SysFont("Castellar", 30)

tile_size = 35
game_over = 0
main_menu = True
level = 0
max_level = 6
score = 0

black = (0, 0, 0)
yellow = (255, 225, 0)
red = (255, 0, 0)

# load images
start_im = pygame.image.load("start_btn.png")
start_im = pygame.transform.scale(start_im, (300, 140))
exit_im = pygame.image.load("exit_btn.png")
exit_im = pygame.transform.scale(exit_im, (300, 140))
retry_im = pygame.image.load("retry_btn.png")
retry_im = pygame.transform.scale(retry_im, (200, 98))
no_retry_im = pygame.image.load("end_btn.png")
no_retry_im = pygame.transform.scale(no_retry_im, (200, 98))
moon_im = pygame.image.load("moon.png")
sky_im = pygame.image.load("sky.png")
bad_end_im = pygame.image.load("bad_end.png")
good_end_im = pygame.image.load("good_end.png")
good_exit_im = pygame.image.load("good_exit_btn.png")
good_exit_im = pygame.transform.scale(good_exit_im, (200, 98))
good_tryagain_im = pygame.image.load("good_tryagain_btn.png")
good_tryagain_im = pygame.transform.scale(good_tryagain_im, (200, 98))

# loud sounds
pygame.mixer.music.load("moon_theme.mp3")
pygame.mixer.music.play(-1, 0.0, 5000)
pygame.mixer.music.set_volume(0.1)
firefly_fx = pygame.mixer.Sound("sound-firefly.wav")
firefly_fx.set_volume(0.55)
jump_fx = pygame.mixer.Sound("sound-jump.wav")
jump_fx.set_volume(1)
gameover_fx = pygame.mixer.Sound("sound-gameover.mp3")
gameover_fx.set_volume(0.175)

# levels
world_level0 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 2, 2, 0, 7, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 8, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_level1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 6, 6, 6, 1],
    [1, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 6, 6, 6, 6, 6, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 0, 0, 0, 0, 0, 7, 0, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 0, 0, 0, 2, 2, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 6, 2, 2, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_level2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 7, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
]

world_level3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1],
    [1, 0, 0, 0, 7, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 6, 1, 1, 1, 0, 0, 0, 7, 0, 0, 0, 0, 7, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 2, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 1, 1, 1, 1],
    [1, 0, 2, 0, 2, 2, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
    [1, 6, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 2, 0, 0, 0, 0, 7, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 6, 6, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
    [1, 6, 2, 2, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_level4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 6, 6, 6, 6, 6, 6, 6, 6, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1],
    [1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 0, 0, 7, 1, 7, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 6, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 1, 6, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 7, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 6, 6, 1, 2, 0, 0, 1],
    [1, 0, 0, 2, 0, 8, 0, 0, 0, 3, 0, 0, 1, 1, 1, 1, 1, 6, 6, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_level5 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 6, 6, 6, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 1],
    [1, 6, 6, 6, 1, 0, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 7, 0, 0, 1],
    [1, 0, 4, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 0, 3, 0, 2, 0, 0, 1],
    [1, 6, 6, 6, 1, 1, 0, 7, 0, 1, 1, 1, 1, 2, 2, 2, 1, 5, 0, 1],
    [1, 6, 6, 6, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 6, 0, 0, 1],
    [1, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 0, 7, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 0, 7, 0, 0, 0, 0, 1],
    [1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 2, 0, 4, 0, 0, 1],
    [1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 7, 1],
    [1, 6, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 7, 5, 6, 1, 1, 1, 2, 1],
    [1, 6, 0, 0, 6, 4, 0, 2, 2, 0, 4, 0, 2, 0, 6, 1, 1, 1, 1, 1],
    [1, 6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 6, 1, 1, 1, 1, 1],
    [1, 6, 0, 5, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 1, 1, 1, 1, 1],
    [1, 6, 0, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 6, 0, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 6, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

world_level6 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 3, 0, 0, 3, 0, 7, 3, 0, 0, 3, 0, 0, 3, 0, 8, 1],
    [1, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]

list_world = [
    world_level0,
    world_level1,
    world_level2,
    world_level3,
    world_level4,
    world_level5,
    world_level6,
]


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_level(level):
    hero.reset(70, screen_height - 91)
    all_spiders.empty()
    all_goos.empty()
    all_bats.empty()
    all_webs.empty()
    all_spikes.empty()
    exit_group.empty()
    platform_group.empty()
    firefly_group.empty()
    firefly_group.add(score_firefly)
    # load in level data and create world
    world_data = list_world[level]
    night = NightWorld(world_data)

    return night


class Hero:
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        col_thresh = 15
        dx = 0
        dy = 0
        walk_cd = 5
        if game_over == 0:
            # get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and not self.jump:
                jump_fx.play()
                self.v_y = -10
                self.jump = True
            if not key[pygame.K_SPACE]:
                self.jump = False
            if key[pygame.K_LEFT]:
                dx -= 3
                self.cntr += 1
                self.drctn = -1
            if key[pygame.K_RIGHT]:
                dx += 3
                self.cntr += 1
                self.drctn = 1
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                self.cntr = 0
                self.indx = 0
                if self.drctn == 1:
                    self.im = self.ims_right[self.indx]
                if self.drctn == -1:
                    self.im = self.ims_left[self.indx]

            if self.cntr > walk_cd:
                self.cntr = 0
                self.indx += 1
                if self.indx >= len(self.ims_right):
                    self.indx = 0
                if self.drctn == 1:
                    self.im = self.ims_right[self.indx]
                if self.drctn == -1:
                    self.im = self.ims_left[self.indx]

            # add gravity
            self.v_y += 1
            if self.v_y > 10:
                self.v_y = 10
            dy += self.v_y

            # check for collision
            self.in_air = True
            for tile in night.tile_list:
                if tile[1].colliderect(
                    self.rect.x + dx, self.rect.y, self.wdth, self.hght
                ):
                    dx = 0
                if tile[1].colliderect(
                    self.rect.x, self.rect.y + dy, self.wdth, self.hght
                ):
                    if self.v_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.v_y = 0
                    elif self.v_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.v_y = 0
                        self.in_air = False

            for platform in platform_group:
                # collision in the x direction
                if platform.rect.colliderect(
                    self.rect.x + dx, self.rect.y, self.wdth, self.hght
                ):
                    dx = 0
                if platform.rect.colliderect(
                    self.rect.x, self.rect.y + dy, self.wdth, self.hght
                ):
                    # check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.v_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    # check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    # move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

            if pygame.sprite.spritecollide(self, all_spiders, False):
                game_over = -1
                gameover_fx.play()

            if pygame.sprite.spritecollide(self, all_bats, False):
                game_over = -1
                gameover_fx.play()

            if pygame.sprite.spritecollide(self, all_webs, False):
                game_over = -1
                gameover_fx.play()

            if pygame.sprite.spritecollide(self, all_spikes, False):
                game_over = -1
                gameover_fx.play()

            if pygame.sprite.spritecollide(self, all_goos, False):
                game_over = -1
                gameover_fx.play()

            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            # update player coords
            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:
            self.im = self.dead_im
            if self.rect.y > 140:
                self.rect.y -= 3
            screen.blit(bad_end_im, (0, 0))
            draw_text(
                "THE END?",
                font,
                red,
                (screen_width // 2) - 180,
                screen_height // 2 - 90,
            )

        # draw hero onto screen
        screen.blit(self.im, self.rect)
        return game_over

    def reset(self, x, y):
        self.ims_right = []
        self.ims_left = []
        self.indx = 0
        self.cntr = 0
        for n in range(1, 9):
            im_right = pygame.image.load(f"hero{n}.png")
            im_right = pygame.transform.scale(im_right, (28, 56))
            im_left = pygame.transform.flip(im_right, True, False)
            self.ims_right.append(im_right)
            self.ims_left.append(im_left)
        self.dead_im = pygame.image.load("ghost.png")
        self.dead_im = pygame.transform.scale(self.dead_im, (28, 56))
        self.im = self.ims_right[self.indx]
        self.rect = self.im.get_rect()
        self.drctn = 0
        self.wdth = self.im.get_width()
        self.hght = self.im.get_height()
        self.rect.x = x
        self.rect.y = y
        self.v_y = 0
        self.jump = False
        self.in_air = True


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # draw button
        screen.blit(self.image, self.rect)
        return action


class NightWorld:
    def __init__(self, data):
        self.tile_list = []

        # load images
        dirt_im = pygame.image.load("dirt.png")
        grass_im = pygame.image.load("grass.png")
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    im = pygame.transform.scale(dirt_im, (tile_size, tile_size))
                    im_rect = im.get_rect()
                    im_rect.x = col_count * tile_size
                    im_rect.y = row_count * tile_size
                    tile = (im, im_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    im = pygame.transform.scale(grass_im, (tile_size, tile_size))
                    im_rect = im.get_rect()
                    im_rect.x = col_count * tile_size
                    im_rect.y = row_count * tile_size
                    tile = (im, im_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    spider = Enemy1(col_count * tile_size, row_count * tile_size + 15)
                    all_spiders.add(spider)
                if tile == 4:
                    platform = Platform(
                        col_count * tile_size, row_count * tile_size, 1, 0
                    )
                    platform_group.add(platform)
                if tile == 5:
                    platform = Platform(
                        col_count * tile_size, row_count * tile_size, 0, 1
                    )
                    platform_group.add(platform)
                if tile == 6:
                    web = Web(
                        col_count * tile_size, row_count * tile_size + (tile_size // 2)
                    )
                    all_webs.add(web)
                if tile == 7:
                    firefly = FireFly(
                        col_count * tile_size + (tile_size // 2),
                        row_count * tile_size + (tile_size // 2),
                    )
                    firefly_group.add(firefly)
                if tile == 8:
                    exit = Exit(
                        col_count * tile_size, row_count * tile_size - (tile_size // 2)
                    )
                    exit_group.add(exit)
                if tile == 9:
                    bat = Enemy2(col_count * tile_size, row_count * tile_size + 15)
                    all_bats.add(bat)
                if tile == 10:
                    spike = Spike(
                        col_count * tile_size, row_count * tile_size + (tile_size // 2)
                    )
                    all_spikes.add(spike)
                if tile == 11:
                    goo = Enemy3(col_count * tile_size, row_count * tile_size + 15)
                    all_goos.add(goo)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_drctn = 1
        self.move_cntr = 0

    def update(self):
        self.rect.x += self.move_drctn
        self.move_cntr += 1
        if abs(self.move_cntr) > 35:
            self.move_drctn *= -1
            self.move_cntr *= -1


class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bat.png")
        self.image = pygame.transform.scale(self.image, (33, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_drctn = 1
        self.move_cntr = 0

    def update(self):
        self.rect.y += self.move_drctn
        self.move_cntr += 1
        if abs(self.move_cntr) > 35:
            self.move_drctn *= -1
            self.move_cntr *= -1


class Enemy3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("goo.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_drctn = 1
        self.move_cntr = 0

    def update(self):
        self.rect.x += self.move_drctn
        self.move_cntr += 3
        if abs(self.move_cntr) > 50:
            self.move_drctn *= -1
            self.move_cntr *= -1


class Web(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("web.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("spikes.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class FireFly(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("firefly.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("exit.png")
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("m_platf.png")
        self.image = pygame.transform.scale(image, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 35:
            self.move_direction *= -1
            self.move_counter *= -1


hero = Hero(70, screen_height - 91)

all_bats = pygame.sprite.Group()
all_goos = pygame.sprite.Group()
all_spiders = pygame.sprite.Group()
all_webs = pygame.sprite.Group()
all_spikes = pygame.sprite.Group()
firefly_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()

score_firefly = FireFly(tile_size // 2, tile_size // 2)
firefly_group.add(score_firefly)

world_data = list_world[level]
night = NightWorld(world_data)

# create buttons
start_button = Button(screen_width // 2 - 165, screen_height // 2 + 35, start_im)
exit_button = Button(screen_width // 2 - 165, screen_height // 2 + 190, exit_im)

run = True
while run:
    file = open("GameLaunches.txt", "w")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"Last Launch: {current_time}\n")
    clock.tick(fps)
    screen.blit(sky_im, (0, 0))
    screen.blit(moon_im, (75, 55))
    if main_menu == True:
        draw_text(
            "Moon Threads",
            font,
            yellow,
            (screen_width // 2) - 320,
            screen_height // 2 - 100,
        )
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False
    else:
        night.draw()

        if game_over == 0:
            all_spiders.update()
            all_bats.update()
            all_goos.update()
            platform_group.update()
            # update score
            # check if a firefly has been collected
            if pygame.sprite.spritecollide(hero, firefly_group, True):
                score += 1
                firefly_fx.play()
            draw_text(str(score), font_score, black, tile_size - 6, -2)

        all_goos.draw(screen)
        all_spiders.draw(screen)
        all_spikes.draw(screen)
        all_bats.draw(screen)
        all_webs.draw(screen)
        firefly_group.draw(screen)
        exit_group.draw(screen)
        platform_group.draw(screen)
        game_over = hero.update(game_over)

        # if player has died
        if game_over == -1:
            no_button = Button(
                screen_width // 2 - 105, screen_height // 2 + 35, retry_im
            )
            yes_button = Button(
                screen_width // 2 - 105, screen_height // 2 + 190, no_retry_im
            )
            if no_button.draw():
                score = 0
                world_data = []
                night = reset_level(level)
                game_over = 0
            if yes_button.draw():
                run = False

        # if player has completed the level
        if game_over == 1:
            # reset game and go to next level
            level += 1
            if level <= max_level:
                # reset level
                world_data = []
                night = reset_level(level)
                game_over = 0
            else:
                screen.blit(good_end_im, (0, 0))
                good_exit_button = Button(
                    screen_width // 2 - 105, screen_height // 2 + 191, good_exit_im
                )
                good_tryagain_button = Button(
                    screen_width // 2 - 105, screen_height // 2 + 36, good_tryagain_im
                )
                if good_tryagain_button.draw():
                    score = 0
                    level = 0
                    # reset level
                    world_data = []
                    night = reset_level(level)
                    game_over = 0
                if good_exit_button.draw():
                    run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()