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
        tela_de_creditos = pygame.image.load("imagens_jogo/imagem_creditos.png")

        # desenhando a imagem na tela do pygame
        self.screen.blit(tela_de_creditos, (0, 0))

    def pegar_eventos_teclado_creditos(self, som_enter_exit):

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

                    som_enter_exit.play()

    def rodar_tela_creditos(self):

        # carregando o efeito sonoro
        som_enter = pygame.mixer.Sound("efeitos_sonoros/som_selecao_opcoes_menu_8bit.wav")

        som_enter.set_volume(.1)

        pygame.mixer.music.load("music/Elefante Branco 2.ogg")

        # tocando a música de fundo. O "-1" significa que, quando a música parar, ela deve tocar novamente se eu ainda estiver na tela dos créditos
        pygame.mixer.music.play(-1)

        while self.running:

            self.pegar_eventos_teclado_creditos(som_enter)

            self.desenhar_tela_creditos()

            # comando que atualiza a tela com tudo o que foi desenhado
            pygame.display.flip()

        pygame.mixer.music.stop()

        pygame.mixer.music.unload()