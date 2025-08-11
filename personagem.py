import pygame

class Jogador:
    def __init__(self, x , y, largura, altura):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.config_rec = {"x": x, "y": y}
        self.velocidade = 5
        self.velocidade_correnteza = 0
        imagem = pygame.image.load("imagens_jogo\Chaves.png").convert_alpha()
        self.imagem = pygame.transform.scale(imagem, (largura, altura))  # Redimensiona para caber no retângulo
        self.barreira_morte = pygame.Rect(-100 , 0, 1, 640)
    
    def mover(self, teclas, obstaculos):
        movimento = pygame.Vector2(0, 0)
        movimento.x = - self.velocidade_correnteza

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            movimento.y = -self.velocidade
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            movimento.y = self.velocidade
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            movimento.x = - self.velocidade*1.5
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            movimento.x = self.velocidade
        
        self.rect.x += movimento.x
        for obstaculo in obstaculos:
            if self.rect.colliderect(obstaculo):
                if movimento.x > 0:  # Indo para a direita
                    self.rect.right = obstaculo.left
                if movimento.x < 0:  # Indo para a esquerda
                    self.rect.left = obstaculo.right

        # Agora move no eixo Y e checa colisões
        self.rect.y += movimento.y
        for obstaculo in obstaculos:
            if self.rect.colliderect(obstaculo):
                if movimento.y > 0:  # Indo para baixo
                    self.rect.bottom = obstaculo.top
                if movimento.y < 0:  # Indo para cima
                    self.rect.top = obstaculo.bottom

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)
    
    def get_velocidade_correnteza(self, velocidade):
        self.velocidade_correnteza = velocidade
    
    def get_colisao_barreira_morte(self): #retorna true se a colisao ocorrer
        condicao = self.rect.colliderect(self.barreira_morte)
        if condicao:
            self.rect.x = self.config_rec["x"]  # Muda a posição horizontal
            self.rect.y = self.config_rec["y"]  # Muda a posição vertical
        return condicao
        
