import pygame
import math
from personagem import Jogador

# importando o menu
from menu import classe_menu

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

# criando o menu do jogo
menu_do_jogo = classe_menu(tela)

#variaveis do jogo
scroll = 0
partes = math.ceil(comprimeto_tela/imagem_comprimento) + 2
print(partes)

chaves = Jogador(400, 400, 100, 100)
obstaculos = [
    pygame.Rect(0 , 300, 860, 10),
    pygame.Rect(-100 , 0, 1, 640),
    pygame.Rect(860 , 0, 1, 640),
    pygame.Rect(0 , 640, 860, 1)
]

velocidade = 3
#velocidade do cenario
chaves.get_velocidade_correnteza(velocidade)

#loop do jogo
run = True
while run:

    # rodando o menu
    menu_do_jogo.rodar_menu()

    # verificando se eu quero fechar a tela do jogo durante o menu
    if menu_do_jogo.sair_do_jogo == False: # se eu não quero fechar, vou entrar em alguma das 2 telas do jogo: o jogo em si e os créditos

        # verificando se o jogador apertou o botão START
        if menu_do_jogo.selected_index == 0:

            clock.tick(FPS)
            chaves.get_velocidade_correnteza(velocidade)
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

            if velocidade >= 6:
                velocidade  = 6
            else: 
                velocidade += 0.001

            chaves.get_velocidade_correnteza(velocidade)

            chaves.desenhar(tela)

            pygame.display.update()

        # verificando se o jogador apertou o botão credits
        elif menu_do_jogo.selected_index == 1:

            rodando_creditos = True

            while rodando_creditos:

                clock.tick(FPS)
                
                # verificando os eventos que o jogador vai mandar para mim
                for event in pygame.event.get():
                    
                    # verificando se o jogador fechou a tela do jogo
                    if event.type == pygame.QUIT:
                        
                        # mudando o valor da variável para terminar o loop do jogo
                        rodando_creditos = False
                        run = False

                    # verificando se o jogador apertou alguma tecla do teclado
                    elif event.type == pygame.KEYDOWN:
                        
                        # verificando se o jogador clicou na tecla "ENTER"
                        if event.key == pygame.K_RETURN:
                                                
                            rodando_creditos = False
                            menu_do_jogo.running = True
                
                # pintando a tela de preto
                tela.fill((0, 0, 0))

                # carregando a imagem dos creditos
                tela_de_creditos = pygame.image.load("imagem_creditos.png")

                # redimensionando a tela de créditos
                tela_de_creditos = pygame.transform.scale(tela_de_creditos, (largura_tela, largura_tela))

                # desenhando a imagem na tela do pygame
                tela.blit(tela_de_creditos, (110, 0))

                # definindo as coordenadas do retangulo seletor
                x_ret_cred, y_ret_cred = 130, 540

                # definindo o tamanho do retangulo seletor
                largura_ret_cred, altura_ret_cred = 150, 65

                # definindo a largura do contorno do retangulo
                largura_contorno_ret_cred = 7
                
                # criando o retangulo seletor
                retangulo_seletor_creditos = pygame.Rect(x_ret_cred, y_ret_cred, largura_ret_cred, altura_ret_cred)

                # desenha retangulo seletor na tela
                pygame.draw.rect(tela, (255, 0, 0), retangulo_seletor_creditos, largura_contorno_ret_cred)

                # atualizando a tela com tudo que eu desenhei
                pygame.display.flip()

    # verificando se eu quero fechar a tela do jogo durante o menu
    else:
        
        # mudando o valor da variável que controla o loop
        run = False

pygame.quit()