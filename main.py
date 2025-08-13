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

        self.x_pos -= 7

        if self.x_pos < -2 * self.largura: # in order to make the collectible disappear from the screen, but stop being drawn
            self.out_of_screen = True

        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50) 

posicoes_y = [358, 470, 582]

intervalo_ondas = 750
itens_ativos = []

def criar_onda(list_all_collects):
    global itens_ativos

    posicoes_disponiveis = posicoes_y.copy()

    # --- 1) Obstáculos obrigatórios ---
    qtd_obstaculos = random.randint(1, 2)  # pode ter 1 ou 2
    pos_obstaculos = random.sample(posicoes_disponiveis, qtd_obstaculos)

    for y in pos_obstaculos:
        obst_info = next(item for item in list_all_collects if item['nome'] == 'bola')  
        novo_obst = Collectible(
            x_pos=comprimento_tela,
            y_pos=y,
            imagem=obst_info['imagem'],
            largura=obst_info['largura'],
            altura=obst_info['altura']
        )
        itens_ativos.append(novo_obst)
        posicoes_disponiveis.remove(y)

    # --- 2) Coletáveis opcionais ---
    for y in posicoes_disponiveis:
        if random.random() < 0.1:  # 60% de chance de aparecer algo
            colet_info = random.choices([item for item in list_all_collects if item['nome'] != 'bola'], weights=[0.6, 0.2, 0.2])[0] # escolhe aleatoriamente entre os outros tipos de coletáveis
            novo_colet = Collectible(
                x_pos=comprimento_tela,
                y_pos=y,
                imagem=colet_info['imagem'],
                largura=colet_info['largura'],
                altura=colet_info['altura']
            )
            itens_ativos.append(novo_colet)

# creating a list in order to store the particular attributes of the different types of objects used during the game

list_all_collects = [{'nome': 'sanduiche', 'points': 1, 'imagem': "imagens_jogo/sanduiche.png", 'lista completa': [], 'lista pos y' :[], 'largura': 55, 'altura': 40}, 
                     {'nome': 'passagem', 'points': 1, 'imagem': "imagens_jogo/passagem.png", 'lista completa': [], 'lista pos y' :[], 'largura': 45, 'altura': 28}, 
                     {'nome': 'tamarindo', 'points': 0, 'imagem': "imagens_jogo/tamarindo.png", 'lista completa': [], 'lista pos y' :[], 'largura': 40, 'altura': 55}, 
                     {'nome': 'bola', 'points': -1, 'imagem': "imagens_jogo/bola.png", 'lista completa': [], 'lista pos y' :[], 'largura': 75, 'altura': 75}]

for i in range(4):

    list_all_collects[i]['imagem'] = pygame.image.load(list_all_collects[i]['imagem']).convert_alpha()
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
                tempo_ultima_onda = pygame.time.get_ticks() + 1500
                while (not morte) and run:

                    clock.tick(FPS)
                    chaves.get_velocidade_correnteza(velocidade)
                    #cenario infinito
                    for i in range (0, partes):
                        tela.blit(imagem_cenario, (i * imagem_comprimento + scroll, 0))
                    scroll -= velocidade

                    teclas = pygame.key.get_pressed()
                    chaves.mover(teclas, obstaculos)

                    if pygame.time.get_ticks() - tempo >= 5000:
                        tempo = pygame.time.get_ticks()

                    tempo_atual = pygame.time.get_ticks()
                    if tempo_atual - tempo_ultima_onda >= intervalo_ondas:
                        criar_onda(list_all_collects)
                        tempo_ultima_onda = tempo_atual

                    for item in itens_ativos[:]:

                        if chaves.rect.colliderect(item.rect):

                            item.collided = True 

                        if not item.collided and not item.out_of_screen:
                            item.movement()
                            item.draw_collec(tela)
                    
                    # resetando scroll 
                    if abs(scroll) > imagem_comprimento:
                        scroll = 0

                    #receber evento
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False

                    if velocidade >= 8:
                        velocidade = 8
                    else: 
                        velocidade += 0.003

                    chaves.get_velocidade_correnteza(velocidade)

                    if chaves.get_colisao_barreira_morte(): #condicao de morte do chaves obs: tem que resetar o coletaveis se derrota por isso
                        morte = True
                        menu_do_jogo.running = True
                        itens_ativos = []

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