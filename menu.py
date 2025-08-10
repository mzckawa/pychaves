# importando a biblioteca do pygame
import pygame

# criando a classe que será usada para criar o menu
class classe_menu:

    # definindo os atributos da classe
    def __init__(self, tela_do_jogo):

        # guardando a tela do jogo dentro da minha classe (vou usar a tela do jogo para desenhar as coisas do menu nela)
        self.screen = tela_do_jogo
    
        # guardando as opções do menu para falar para o programa principal onde eu estou e qual opção o jogador vai selecionar (dando ENTER)
        self.options = ["START", "CREDITS"]

        # dizendo qual a opção que está selecionada na tela do jogador por meio de um número (que funciona como um índice, já que estamos usando uma lista)
        self.selected_index = 0

        # criando um atributo que vai servir para rodar o menu dentro de um WHILE até que algumas das opções seja selecionada (fazendo com que eu saia do menu)
        self.running = True

        # criei essa variável para mostrar pro meu programa que eu quero fechar a tela do jogo durante o menu
        self.sair_do_jogo = False

        #README talvez eu nem use isso, já que eu só quero colocar caixas seletoras na tela, e não texto em si
        # guardando uma fonte para ser usada na tela do meu jogo
        self.font = pygame.font.SysFont("Arial", 40)

        # guardando as cores que serão usadas para o menu
        #README talvez eu nem use a cor branca

        self.color_normal = (255, 255, 255) # branco
        
        # tô guardando as cores como tuplas, já que elas nunca vão mudar
        self.color_selected = (255, 0, 0) # vermelho

    # criando funções que serão usadas para o menu
    #README não sei como essas funções vão ser aplicas no código principal, mas talvez o nome delas já existe lá

    # função para desenhar as coisas do menu na tela do jogo
    def desenhar(self):

        # criando a imagem de fundo da tela 
        fundo = pygame.image.load("imagem_menu_jogo.jpg")

        # redimensionando a imagem de fundo - posso mudar as coordenadas depois
        fundo = pygame.transform.scale(fundo, (640, 640))

        # desenhando a imagem na tela
        self.screen.blit(fundo, (110, 0))

        # Define a posição e dimensões do retângulo
        if self.selected_index == 0:

            y_retangulo = 517

        elif self.selected_index == 1:

            y_retangulo = 572

        x_retangulo = 320 # para passar para a opção de baixo, eu vou aumentar 55 na coordenada do retângulo
        largura_ret, altura_ret = 220, 60

        # Define a largura do contorno (10 pixels)
        largura_contorno = 7

        # Cria o retângulo seletor
        retangulo_seletor = pygame.Rect(x_retangulo, y_retangulo, largura_ret, altura_ret)

        # Desenha o retangulo seletor na tela
        pygame.draw.rect(self.screen, self.color_selected, retangulo_seletor, largura_contorno)

    def pegar_eventos_teclado(self):
        
        # carregando os efeitos sonoros do jogo
        #TODO verificar se isso gasta muita memória
        som_selecao_opcoes = pygame.mixer.Sound("som_selecao_opcoes_menu_8bit.wav")
        som_start = pygame.mixer.Sound("som_start_8bit.wav")
        
        # verificando os eventos do teclado
        for evento in pygame.event.get():
            
            # verificando se o jogador quis fechar a tela do jogo
            if evento.type == pygame.QUIT:

                # mudando o valor da variável que define se o menu está rodando na tela do jogo ou não
                # provavelmente eu vou ter que colocar algum comando aqui para fechar a tela do jogo
                self.running = False

                # mudando o valor dessa variável (já que eu quero fechar a tela do jogo durante o menu)
                self.sair_do_jogo = True

            # verificando se alguma tecla do teclado foi pressionada
            elif evento.type == pygame.KEYDOWN:

                # se o evento do teclado for SETA PRA CIMA 
                if evento.key == pygame.K_UP:
                    
                    # Se sim, o seletor das opções vai ir para uma opção acima, ou seja, de índice menor dentro da lista "self.options"
                    self.selected_index -= 1

                    # condição que verifica se estou na opção mais alta (em posição) de todas. Com isso, quando eu apertar a tecla pra cima, o seletor vai para a opção
                    # mais abaixo de todas                    
                    if self.selected_index < 0:
                        
                        # deixei a "len" aí porque, futuramente, talvez eu coloque mais uma opção no menu
                        self.selected_index = len(self.options) - 1

                    som_selecao_opcoes.play()

                # verificando se a tecla clicada foi a SETA PARA BAIXO
                elif evento.key == pygame.K_DOWN:
                    
                    # se sim, isso ocasiona um aumento do index (o que faz o seletor ir para a opção de baixo)
                    self.selected_index += 1
                    
                    # criando condição para verificar se já estou na opção mais abaixo (em posição) de todas para que, se eu clicar na seta pra baixo, eu volte para a opção mais alta
                    if self.selected_index >= len(self.options):
                        
                        # esse é o indice da opção mais alta
                        self.selected_index = 0

                    som_selecao_opcoes.play()

                # verificando se a tecla clicada foi o ENTER
                elif evento.key == pygame.K_RETURN:
                        
                    # verificando qual foi a opção selecionada pelo jogador (por meio da lista com as opções e o índice que eu tô mexendo aqui em cima 👆)
                    #README talvez eu tenha que colocar algum comando aqui dentro para mandar o jogador para a próxima tela do jogo de acordo com
                    # a opção que ele selecionada
                    if self.options[self.selected_index] == "START":
                        
                        # mudando o valor dessa variável para o menu parar de rodar
                        self.running = False

                        som_start.play()

                    elif self.options[self.selected_index] == "CREDITS":
                        
                        # mudando o valor dessa variável para o menu parar de rodar
                        self.running = False
    
    def rodar_menu(self):

        # loop para rodar o menu
        while self.running:
            
            # chamando a função para captar os comandos do teclado do jogador
            self.pegar_eventos_teclado()

            # chamando a função para desenhar o que for necessário de acordo com os comandos do teclado do jogador
            self.desenhar()

            # função para atualizar a tela do jogo
            pygame.display.flip()