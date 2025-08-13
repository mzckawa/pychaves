import pygame
import math
from personagem import Jogador
from creditos import classe_creditos
from random import randint
import random

# importando o menu
from menu import classe_menu

# # importando os coletáveis e a função de criação
# from classes_e_funcoes_coletaveis import *

pygame.init()

class Collectible:

    def __init__(self, x_pos, y_pos, imagem, largura, altura):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.largura = largura
        self.altura = altura
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.largura, self.altura)
        self.imagem = pygame.transform.scale(imagem, (self.largura, self.altura))
        self.collided = False
        self.out_of_screen = False

    def draw_collec(self):
        tela.blit(self.imagem, (self.x_pos, self.y_pos))

    def movement(self):

        self.x_pos -= 10

        if self.x_pos < -2 * self.largura: # in order to make the collectible disappear from the screen, but stop being drawn
            self.out_of_screen = True

        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50) 









def creating_collectibles(lista_pos):
    
    lista_aux = []
    lista_aux_colec = []
    
    n_obstaculos = random.choices([1, 2], weights = [0.7, 0.3])
    
    # FOR para gerar as posições dos obstáculos
    for i in range(n_obstaculos):
        
        y = random.choice(lista_pos)
        
        lista_aux.append(y)
        
        #README cuidado para não alterar a lista de fora
        lista_pos.remove(y)
    
    status_colec = random.choices([True, False], weights = [0.3, 0.7]) 
    
    if status_colec:
        y = random.choice(lista_pos)

        tipo = random.choices(["saduiche","suco","passagem"], weights = [0.4, 0.3, 0.2])

        lista_aux_colec.append(y)

        lista_pos.remove(y)

        resultado = f'obstáculos: {lista_aux}\n coletável: tipo {tipo} e posição {lista_aux_colec} \n restante {lista_pos}'
    
    else:
        
        resultado = f'obstáculos: {lista_aux}\n não tem coletável \n restante {lista_pos}'
    
    return resultado




















#define tempo do jogo
clock = pygame.time.Clock()
FPS = 60 # mudar depois

#dimencionamento da tela
comprimento_tela = 860
largura_tela = 640

#criando a tela
tela = pygame.display.set_mode((comprimento_tela, largura_tela))
pygame.display.set_caption("pychaves")

#receber a imagem dos arquivos
imagem_cenario = pygame.image.load("imagens_jogo/cenario_jogo.jpg").convert()
#convercao da imagem
imagem_cenario = pygame.transform.scale(imagem_cenario, (2*comprimento_tela/3, largura_tela))
imagem_comprimento = imagem_cenario.get_width()

# criando o menu do jogo
menu_do_jogo = classe_menu(tela)

# criando os créditos do jogo
creditos_do_jogo = classe_creditos(tela)

#variaveis do jogo
scroll = 0
partes = math.ceil(comprimento_tela/imagem_comprimento) + 2
print(partes)

chaves = Jogador(400, 400, 100, 100)
obstaculos = [
    pygame.Rect(0 , 300, 860, 10),
    pygame.Rect(860 , 0, 1, 640),
    pygame.Rect(0 , 640, 860, 1)
]

velocidade = 3
#velocidade do cenario
chaves.get_velocidade_correnteza(velocidade)









for i in range(4):

    list_all_collects[i]['imagem'] = pygame.image.load(list_all_collects[i]['imagem']).convert_alpha()

    if i == 3: # adicionando os objetos bola à lista de obstáculos

        for bola in list_all_collects[i]['lista completa']:
            obstaculos.append(bola.rect)







# APAGAR

#loop do jogo
run = True
morte = False
while run:
        
        tela.fill((0,0,0))
        # rodando o menu
        menu_do_jogo.rodar_menu()

        # verificando se eu quero fechar a tela do jogo durante o menu
        if menu_do_jogo.sair_do_jogo == False: # se eu não quero fechar, vou entrar em alguma das 2 telas do jogo: o jogo em si e os créditos

            # verificando se o jogador apertou o botão START
            if menu_do_jogo.selected_index == 0:

                morte = False
                velocidade = 3
                scroll = 0
                while (not morte) and run:

                    clock.tick(FPS)
                    chaves.get_velocidade_correnteza(velocidade)
                    #cenario infinito
                    for i in range (0, partes):
                        tela.blit(imagem_cenario, (i * imagem_comprimento + scroll, 0))
                    scroll -= velocidade

                    teclas = pygame.key.get_pressed()
                    chaves.mover(teclas, obstaculos)

                    PreenchSeguintes()# APAGAR
                    

                    # resetando scroll 
                    if abs(scroll) > imagem_comprimento:
                        scroll = 0

                    #receber evento
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False

                    if velocidade >= 6:
                        velocidade = 6
                    else: 
                        velocidade += 0.001

                    chaves.get_velocidade_correnteza(velocidade)

                    if chaves.get_colisao_barreira_morte(): #codicao de morte do chaves obs: tem que resetar o coletaveis se derrota por isso
                        morte = True
                        menu_do_jogo.running = True

                    # fiz esse ELSE para não ocorrer o seguinte bug: o jogador morre ao chegar no limite esquerdo e o Chaves era desenhado mais uma vez na tela
                    else:
                        chaves.desenhar(tela)

                    pygame.display.update()

            # verificando se o jogador apertou o botão credits
            elif menu_do_jogo.selected_index == 1:

                clock.tick(FPS)

                creditos_do_jogo.rodar_tela_creditos()
                
                if creditos_do_jogo.fechar_tela == True:
                    
                    run = False

                elif creditos_do_jogo.fechar_tela == False:

                    menu_do_jogo.running = True
                    creditos_do_jogo.running = True

        # verificando se eu quero fechar a tela do jogo durante o menu
        else:
            
            # mudando o valor da variável que controla o loop
            run = False

pygame.quit()