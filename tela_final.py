import pygame

class classe_tela_final:

    # esse "vitoria" vai ser uma variável booleana para falar se o jogador ganhou ou não
    def __init__(self, tela_do_jogo, vitoria):
        
        self.running = True

        self.screen = tela_do_jogo

        self.fechar_janela = False

        self.vitoria = vitoria
        
    def desenhar_tela_final(self):

        fonte = pygame.font.Font("Press_Start_2P/PressStart2P-Regular.ttf", 35)

        if self.vitoria:

            imagem_selecionada = pygame.image.load("imagens_jogo/tela_vitoria.png")

            imagem_selecionada = pygame.transform.scale(imagem_selecionada, (860, 640))

        else:

            imagem_selecionada = pygame.image.load("imagens_jogo/imagem_derrota.png") # completar aqui com a imagem do fim de derrota

            imagem_selecionada = pygame.transform.scale(imagem_selecionada, (860, 640))
        
        self.screen.blit(imagem_selecionada, (0, 0))

        opcao = "MENU"

        opcao = fonte.render(opcao, True, (255, 255, 255))

        self.screen.blit(opcao, (660, 575))

        # AINDA VOU ADICIONAR UM RETÂNGULO VERMELHO

        # definindo as coordenadas do retangulo seletor
        x_ret_cred, y_ret_cred = 643, 564

        # definindo o tamanho do retangulo seletor
        largura_ret_cred, altura_ret_cred = 170, 55

        # definindo a grossura do contorno do retangulo
        largura_contorno_ret_cred = 7
        
        # criando o retangulo seletor
        retangulo_seletor_creditos = pygame.Rect(x_ret_cred, y_ret_cred, largura_ret_cred, altura_ret_cred)

        # desenha retangulo seletor na tela
        pygame.draw.rect(self.screen, (255, 0, 0), retangulo_seletor_creditos, largura_contorno_ret_cred)

        pygame.display.flip()

    def captar_eventos_teclado(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

                self.fechar_janela = True
            
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    self.running = False

    def rodando_tela_final(self):
        
        self.desenhar_tela_final()

        if self.vitoria:

            pygame.mixer.music.load("music/Happy Whistler.ogg")

        else:

            pygame.mixer.music.load("music/Música Triste.ogg")

        pygame.mixer.music.set_volume(.7)

        pygame.mixer.music.play(-1)

        while self.running:

            self.captar_eventos_teclado()

        pygame.mixer.music.stop()

        pygame.mixer.music.unload()