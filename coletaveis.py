import pygame
from pygame.locals import *
from personagem import Jogador
from random import randint

pygame.init()

#define tempo do jogo
clock = pygame.time.Clock()
FPS = 500

#dimencionamento da tela
comprimeto_tela = 860
largura_tela = 640

#posiçoes blocos
x = 860
y = 0
x_azul = randint(30, 700)
y_azul = randint (30, 500)

tela = pygame.display.set_mode((comprimeto_tela, largura_tela))
pygame.display.set_caption("pychaves")

run = True
while run:
    tela.fill((0,0,0))
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    quad_verm = pygame.draw.rect(tela, (255,0,0), (x,y,90,90))
    quad_azul = pygame.draw.rect(tela, (0,0,255), (x_azul, y_azul,40,40))

    if x <= 0:
        x = 860
        y = randint(30, 640)

    if y >= 640:
        y=0
    x = x - 1

    if quad_verm.colliderect(quad_azul):
        print("azul perdeu!")
        x_azul = randint(30, 700)
        y_azul = randint (30, 500)


    pygame.display.update()

pygame.quit()