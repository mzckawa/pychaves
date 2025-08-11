import pygame

class classe_creditos:

    # definindo as características da minha classe
    def __init__(self, tela_do_jogo):
        
        # guardando a tela do jogo como uma característica da minha classe
        self.screen = tela_do_jogo

        # criando uma variável bool para controlar o menu
        self.running = True

        # criando uma variável para mostrar pro meu programa de que quero fechar a tela do jogo
        # durante os créditos
        self.fechar_tela = False

        # salvando a cor VERMELHO para pintar o retângulo seletor da opção "EXIT"
        self.color_selected = (255, 0, 0)

    def desenhar_tela_creditos(self):

        # pintando a tela de preto - tô tentando "limpar a tela"
        self.screen.fill((0, 0, 0))

        # carregando a imagem dos creditos
        tela_de_creditos = pygame.image.load("imagens_jogo\imagem_creditos.png")

        # redimensionando a tela de créditos
        tela_de_creditos = pygame.transform.scale(tela_de_creditos, (640, 640))

        # desenhando a imagem na tela do pygame
        self.screen.blit(tela_de_creditos, (110, 0))

        # definindo as coordenadas do retangulo seletor
        x_ret_cred, y_ret_cred = 130, 540

        # definindo o tamanho do retangulo seletor
        largura_ret_cred, altura_ret_cred = 150, 65

        # definindo a grossura do contorno do retangulo
        largura_contorno_ret_cred = 7
        
        # criando o retangulo seletor
        retangulo_seletor_creditos = pygame.Rect(x_ret_cred, y_ret_cred, largura_ret_cred, altura_ret_cred)

        # desenha retangulo seletor na tela
        pygame.draw.rect(self.screen, (255, 0, 0), retangulo_seletor_creditos, largura_contorno_ret_cred)

    def pegar_eventos_teclado_creditos(self):

        # verificando os eventos que o jogador vai mandar para mim
        for event in pygame.event.get():
            
            # verificando se o jogador fechou a tela do jogo
            if event.type == pygame.QUIT:
                
                # mudando o valor da variável para terminar o loop do jogo
                self.running = False
                self.fechar_tela = True

            # verificando se o jogador apertou alguma tecla do teclado
            elif event.type == pygame.KEYDOWN:
                
                # verificando se o jogador clicou na tecla "ENTER"
                if event.key == pygame.K_RETURN:
                                        
                    self.running = False

    def rodar_tela_creditos(self):

        while self.running:

            self.pegar_eventos_teclado_creditos()

            self.desenhar_tela_creditos()

            # comando que atualiza a tela com tudo o que foi desenhado
            pygame.display.flip()