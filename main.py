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

#dimensionamento da tela
comprimento_tela = 860
largura_tela = 640

#criando a tela
tela = pygame.display.set_mode((comprimento_tela, largura_tela))
pygame.display.set_caption("pychaves")

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

    def draw_collec(self, tela):
        tela.blit(self.imagem, (self.x_pos, self.y_pos))

    def movement(self):

        self.x_pos -= 10

        if self.x_pos < -2 * self.largura: # in order to make the collectible disappear from the screen, but stop being drawn
            self.out_of_screen = True

        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50) 

def creating_collectibles(list_all_collects, i, comprimento_tela):

    list_all = list_all_collects[i]['lista completa']
    list_y = [358, 470, 582]
    available_y = list_y[::]
    img = list_all_collects[i]['imagem']
    larg = list_all_collects[i]['altura']
    alt = list_all_collects[i]['altura']
    
    # defining a random number of appearances for the collectibles
    amount_collect = randint(1, 2)

    while len(list_all) < amount_collect:

        x_collect = comprimento_tela # we want the collectibles to always go from the right side to the left side
        y_collect = random.choice(available_y) # generating a random y-axis position for the collectible

        # adding the random-yet-adequate y-axis position to the list of positions
        available_y.remove(y_collect)

        # creating the objects of the class Collectible with the generated random positions
        collectible = Collectible(x_collect, y_collect, img, larg, alt)

        # adding the newly-created collectible to the list with the other collectibles of the same kind
        list_all.append(collectible)

    return list_all, list_y

# creating a list in order to store the particular attributes of the different types of objects used during the game

list_all_collects = [{'nome': 'sanduiche', 'points': 1, 'imagem': "imagens_jogo/sanduiche.png", 'lista completa': [], 'lista pos y' :[], 'largura': 55, 'altura': 40}, 
                     {'nome': 'passagem', 'points': 1, 'imagem': "imagens_jogo/passagem.png", 'lista completa': [], 'lista pos y' :[], 'largura': 45, 'altura': 28}, 
                     {'nome': 'tamarindo', 'points': 0, 'imagem': "imagens_jogo/tamarindo.png", 'lista completa': [], 'lista pos y' :[], 'largura': 40, 'altura': 55}, 
                     {'nome': 'bola', 'points': -1, 'imagem': "imagens_jogo/bola.png", 'lista completa': [], 'lista pos y' :[], 'largura': 75, 'altura': 75}]
list_probabilities = [0, 0, 0, 0, 1, 2, 3]
# filling the lists created inside the dictionaries 

def PrimeiroPreenchimento():

    for i in range(4):

        list_all_collects[i]['imagem'] = pygame.image.load(list_all_collects[i]['imagem']).convert_alpha()
        list_all_collects[i]['lista completa'], list_all_collects[i]['lista pos y'] = creating_collectibles(list_all_collects, i, comprimento_tela)
    
def PreenchSeguintes():

    for i in range(4):

        if not list_all_collects[i]['lista completa']: # if there aren't any objects of this type available, let's go through their creation process again!

            list_all_collects[i]['lista completa'], list_all_collects[i]['lista pos y'] = creating_collectibles(list_all_collects, i, comprimento_tela)

        remaining_all = []
        remaining_y_pos = []

        for collectible in list_all_collects[i]['lista completa']:

            # creating the collision conditional
            if chaves.rect.colliderect(collectible.rect):

                collectible.collided = True
                
            # keeping on drawing the collectible, if it was not caught by the player or if it's an obstacle
            if not collectible.collided and not collectible.out_of_screen:
                
                collectible.draw_collec(tela)
                collectible.movement()
                remaining_all.append(collectible)
                remaining_y_pos.append(collectible.y_pos)

        # recreating the list of all collectibles only with the ones actually available
        
        list_all_collects[i]['lista completa'] = remaining_all
        list_all_collects[i]['lista pos y'] = remaining_y_pos
        # recreating the list of all collectibles only with the ones actually available
        
        list_all_collects[i]['lista completa'] = remaining_all
        list_all_collects[i]['lista pos y'] = remaining_y_pos

#define tempo do jogo
clock = pygame.time.Clock()
FPS = 60 # mudar depois

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
        list_all_collects[i]['lista completa'], list_all_collects[i]['lista pos y'] = creating_collectibles(list_all_collects, i, comprimento_tela)

tempo = pygame.time.get_ticks()

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

                if pygame.get_ticks() - tempo >= 5000:
                    tempo = pygame.time.get_ticks()
                    PreenchSeguintes()

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