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
imagem_chapeu= pygame.image.load("imagens_jogo/chapeu_chaves.png")
pygame.display.set_icon(imagem_chapeu)


def placar(quant_vida, passagens, imagem_sanduiches_vida, imagem_passagens):
    fonte = pygame.font.SysFont("arial", 40, True, True)
    
    imagem_sanduiches_vida = pygame.transform.scale(imagem_sanduiches_vida, (30, 30))
    imagem_passagens = pygame.transform.scale(imagem_passagens, (30, 30))

    passagens_escrito = f":{passagens}/7"
    vida = f':{quant_vida}'

    texto_vida = fonte.render(vida, True, (255, 255, 255))
    texto_passagens = fonte.render(passagens_escrito, True, (255, 255, 255))

    tela.blit(imagem_sanduiches_vida, (20, 70))
    tela.blit(imagem_passagens, (20, 10))
    
    tela.blit(texto_vida, (50, 70))
    tela.blit(texto_passagens, (50, 10))


class Collectible:

    def __init__(self, x_pos, y_pos, imagem, largura, altura, nome):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.largura = largura
        self.altura = altura
        self.nome = nome 
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
            x_pos = comprimento_tela,
            y_pos = y,
            imagem = obst_info['imagem'],
            largura = obst_info['largura'],
            altura = obst_info['altura'],
            nome = obst_info['nome']
        )
        itens_ativos.append(novo_obst),
        posicoes_disponiveis.remove(y)

    # --- 2) Coletáveis opcionais ---
    for y in posicoes_disponiveis:
        if random.random() < 0.2:  # 60% de chance de aparecer algo
            colet_info = random.choices([item for item in list_all_collects if item['nome'] != 'bola'], weights=[0.6, 0.2, 0.2])[0] # escolhe aleatoriamente entre os outros tipos de coletáveis
            novo_colet = Collectible(
                x_pos = comprimento_tela,
                y_pos = y,
                imagem = colet_info['imagem'],
                largura = colet_info['largura'],
                altura = colet_info['altura'],
                nome = colet_info['nome']
            )
            itens_ativos.append(novo_colet)

# creating a list in order to store the particular attributes of the different types of objects used during the game

list_all_collects = [{'nome': 'sanduiche', 'points': 1, 'imagem': "imagens_jogo/sanduiche.png", 'lista completa': [], 'lista pos y' :[], 'largura': 55, 'altura': 40}, 
                     {'nome': 'passagem', 'points': 1, 'imagem': "imagens_jogo/passagem.png", 'lista completa': [], 'lista pos y' :[], 'largura': 45, 'altura': 28}, 
                     {'nome': 'tamarindo', 'points': 0, 'imagem': "imagens_jogo/tamarindo.png", 'lista completa': [], 'lista pos y' :[], 'largura': 40, 'altura': 55}, 
                     {'nome': 'bola', 'points': -1, 'imagem': "imagens_jogo/bola.png", 'lista completa': [], 'lista pos y' :[], 'largura': 75, 'altura': 75}]

# carregando as imagens necessárias
for i in range(4):
    list_all_collects[i]['imagem'] = pygame.image.load(list_all_collects[i]['imagem']).convert_alpha()

# formatando as imagens do contador (3, 2, 1, GO!)
img_1 = pygame.image.load('imagens_jogo/img_1.png').convert_alpha()
img_1 = pygame.transform.scale(img_1, (200, 200))
img_2 = pygame.image.load('imagens_jogo/img_2.png').convert_alpha()
img_2 = pygame.transform.scale(img_2, (200, 200))
img_3 = pygame.image.load('imagens_jogo/img_3.png').convert_alpha()
img_3 = pygame.transform.scale(img_3, (200, 200))
img_go = pygame.image.load('imagens_jogo/img_go.png').convert_alpha()
img_go = pygame.transform.scale(img_go, (384, 256))
imagem_sanduiches_vida = pygame.image.load("imagens_jogo/sanduiche_vida.png")
imagem_passagens = pygame.image.load("imagens_jogo/passagem.png")

chaves_img_normal = pygame.image.load("imagens_jogo/Chaves.png").convert_alpha()
chaves_img_dano = pygame.image.load("imagens_jogo/Chaves_vermelho.png").convert_alpha()

# Ajuste para o tamanho do personagem
chaves_img_normal = pygame.transform.scale(chaves_img_normal, (100, 100))
chaves_img_dano = pygame.transform.scale(chaves_img_dano, (100, 100))

#define tempo do jogo
clock = pygame.time.Clock()
FPS = 60 

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
chaves.imagem = chaves_img_normal

obstaculos = [
    pygame.Rect(0 , 300, 860, 10),
    pygame.Rect(860 , 0, 1, 640),
    pygame.Rect(0 , 640, 860, 1)
]

velocidade = 3
#velocidade do cenario
chaves.get_velocidade_correnteza(velocidade)

#tempo_inicial = pygame.time.get_ticks()

#loop do jogo
run = True
morte = False

tempo_tamarindo = - 4000

tempo_dano = 0

while run:
        
        tela.fill((0,0,0))
        # rodando o menu
        menu_do_jogo.rodar_menu()

        # verificando se eu quero fechar a tela do jogo durante o menu
        if menu_do_jogo.sair_do_jogo == False: # se eu não quero fechar, vou entrar em alguma das 2 telas do jogo: o jogo em si e os créditos

            # verificando se o jogador apertou o botão START
            if menu_do_jogo.selected_index == 0:
                
                chaves.rect = pygame.Rect(400, 400, 100, 100)

                morte = False
                velocidade = 3
                scroll = 0
                vida = 3
                passagens = 0
                
                tempo_inicial = pygame.time.get_ticks()
                tempo_ultima_onda = pygame.time.get_ticks() + 3000
                
                # carregando o placar
                placar(vida, passagens, imagem_sanduiches_vida, imagem_passagens)
                
                itens_ativos = []

                while (not morte) and run:

                    clock.tick(FPS)
                    chaves.get_velocidade_correnteza(velocidade)

                    tempo = pygame.time.get_ticks()
                    #cenario infinito
                    for i in range (0, partes):
                        tela.blit(imagem_cenario, (i * imagem_comprimento + scroll, 0))
                    placar(vida, passagens, imagem_sanduiches_vida, imagem_passagens)

                    scroll -= velocidade
                    
                    if pygame.time.get_ticks() - tempo_inicial <= 1000:
                        rect3 = tela.blit(img_3, (355, 100))
                        pygame.display.update(rect3)

                    elif  pygame.time.get_ticks() - tempo_inicial <= 2000:
                        rect2 = tela.blit(img_2, (355, 100))
                        pygame.display.update(rect2)

                    elif pygame.time.get_ticks() - tempo_inicial <= 3000:
                        rect1 = tela.blit(img_1, (355, 100))
                        pygame.display.update(rect1)

                    elif pygame.time.get_ticks() - tempo_inicial <= 4000:
                        rect_go = tela.blit(img_go, (238, 100))
                        pygame.display.update(rect_go)
                    
                    teclas = pygame.key.get_pressed()
                    chaves.mover(teclas, obstaculos)

                    if pygame.time.get_ticks() - tempo >= 5000:
                        tempo = pygame.time.get_ticks()

                    tempo_atual = pygame.time.get_ticks()
                    if tempo_atual - tempo_ultima_onda >= intervalo_ondas:
                        criar_onda(list_all_collects)
                        tempo_ultima_onda = tempo_atual
                    
                    vida_antes = vida 

                    for item in itens_ativos[:]:

                        if chaves.rect.colliderect(item.rect):
                            
                            item.collided = True

                            if item.nome == 'tamarindo':
                                tempo_tamarindo = pygame.time.get_ticks() # "reseta" o tempo, contando a partir do momento atual. Isso por se só já verifica se há tamarindos disponíveis ou nãoo
                                itens_ativos.remove(item) 
                            elif item.nome == 'bola':
                                itens_ativos.remove(item) 
                                
                                if pygame.time.get_ticks() - tempo_tamarindo > 4000: # fazendo a animação de dano, caso Chaves não possua tamarindos para protegê-lo
                                    
                                    vida -= 1 
                                    chaves.imagem = chaves_img_dano
                                    tempo_dano = pygame.time.get_ticks()

                                    if vida == 0:
                                        morte = True
                                        menu_do_jogo.running = True

                            elif item.nome == 'sanduiche' and vida < 3:
                                itens_ativos.remove(item) 
                                vida += 1

                            elif item.nome == 'passagem':
                                itens_ativos.remove(item) 
                                passagens += 1
                                    
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

                    if velocidade >= 10:
                        velocidade = 10
                    else: 
                        velocidade += 0.003

                    chaves.get_velocidade_correnteza(velocidade)

                    if chaves.get_colisao_barreira_morte(): #condicao de morte do chaves obs: tem que resetar o coletaveis se derrota por isso
                        morte = True
                        menu_do_jogo.running = True

                    # fiz esse ELSE para não ocorrer o seguinte bug: o jogador morre ao chegar no limite esquerdo e o Chaves era desenhado mais uma vez na tela
                    else:

                        if tempo_dano != 0 and pygame.time.get_ticks() - tempo_dano > 200:
                            chaves.imagem = chaves_img_normal
                            tempo_dano = 0

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