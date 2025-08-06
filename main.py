import pygame
import math
from personagem import Jogador

pygame.init()

#define tempo do jogo
clock = pygame.time.Clock()
FPS = 60

#dimencionamento da tela
comprimeto_tela = 860
largura_tela = 640

#criando a tela
tela = pygame.display.set_mode((comprimeto_tela, largura_tela))
pygame.display.set_caption("pychaves")

#receber a imagem dos arquivos
imagem_cenario = pygame.image.load("cenario_jogo.jpg").convert()
#convercao da imagem
imagem_cenario = pygame.transform.scale(imagem_cenario, (2*comprimeto_tela/3, largura_tela))
imagem_comprimento = imagem_cenario.get_width()


#variaveis do jogo
scroll = 0
partes = math.ceil(comprimeto_tela/imagem_comprimento) + 2
print(partes)
#loop do jogo

chaves = Jogador(400, 400, 100, 100)
obstaculos = [
    pygame.Rect(0 , 300, 860, 10),
    pygame.Rect(-100 , 0, 1, 640),
    pygame.Rect(860 , 0, 1, 640),
    pygame.Rect(0 , 640, 860, 1)
]

velocidade = 3
chaves.get_velocidade_correnteza(3)
run = True
while run:

    clock.tick(FPS)

    #cenario infinito
    for i in range (0, partes):
        tela.blit(imagem_cenario, (i * imagem_comprimento + scroll, 0))
    scroll -= velocidade

    teclas = pygame.key.get_pressed()
    chaves.mover(teclas, obstaculos)

    # resetando scroll 
    if abs(scroll) > imagem_comprimento:
        scroll = 0

    #receber evento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if velocidade >= 8:
        velocidade  = 8
    else: 
        #velocidade += 0.0005
        velocidade += 8

    chaves.get_velocidade_correnteza(0)

    chaves.desenhar(tela)

    pygame.display.update()

pygame.quit()