import pygame
from pygame import mixer
from pygame.locals import *
import random

pygame.init()
pygame.mixer.init()

mixer.music.load('Clown.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basket Ball Game")

icon = pygame.image.load("ball.png")
pygame.display.set_icon(icon)
background = pygame.image.load("court.jpg")
background = pygame.transform.scale(background, (800, 600))
ring_img = pygame.image.load("basketball_ring.png")
ring_img = pygame.transform.scale(ring_img, (300, 300))
ball_img = pygame.image.load("ball.png")
ball_img = pygame.transform.scale(ball_img, (100, 100))

ring_x = 300
ring_y = 350
ball_x = random.randint(50, 700)
ball_y = 50
ball_speed = 1

font = pygame.font.Font(None, 36)
score = 0
scored = False

def ring_pic():
    screen.blit(ring_img, (ring_x, ring_y))

def ball_pic():
    screen.blit(ball_img, (ball_x, ball_y))

def shoot():
    global scored
    if ball_y >= ring_y + 150 and ball_x -40>= ring_x and ball_x <= ring_x + 120:
        if not scored:
            scored = True
            return True
    else:
        scored = False
    return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ring_x > -100:
        ring_x -= 5
    if keys[pygame.K_RIGHT] and ring_x < 600:
        ring_x += 5

    ball_y += ball_speed
    if ball_y > 500:    
        ball_y = 50
        ball_x = random.randint(50, 750)

    ring_pic()
    ball_pic()

    if shoot():
        score += 1

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    
pygame.quit()
