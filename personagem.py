import pygame

class Jogador:
    def __init__(self, x , y, largura, altura):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.velocidade = 5
        imagem = pygame.image.load("Chaves.png").convert_alpha()
        self.imagem = pygame.transform.scale(imagem, (largura, altura))  # Redimensiona para caber no retângulo
    
    def mover(self, teclas, obstaculos):
        movimento = pygame.Vector2(0, 0)
        movimento.x = - self.velocidade

        if teclas[pygame.K_w]:
            movimento.y = -self.velocidade
        if teclas[pygame.K_s]:
            movimento.y = self.velocidade
        if teclas[pygame.K_a]:
            movimento.x = - self.velocidade*1.5
        if teclas[pygame.K_d]:
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