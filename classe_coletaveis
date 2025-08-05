import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

tela = pygame.display.set_mode((860, 640))

x = 0
y = 0

pygame.display.set_caption('Pychaves')
running = True

while running:

    pygame.display.update()
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    x += 0.5
    y += 0.5

    if x >= 860:
        x = 0

    if y >= 640:
        y = 0

    pygame.draw.rect(tela, (255, 255, 255), (x, y, 100, 100))
    pygame.draw.circle(tela, (255, 90, 70), (0, 320), 100)
    pygame.draw.line(tela, (50, 50, 50), (0, 0), (860, 640), 10)

pygame.quit()         
exit()
# definindo as características dos coletáveis 

# tamanho, velocidade
# como criar o sistema de contabilização dos coletáveis?

# print('Hello')
