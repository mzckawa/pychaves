import pygame
from pygame.locals import *
from sys import exit
import random
from random import randint
from personagem import Jogador

width = 860
height = 640
screen = pygame.display.set_mode((width, height))

chaves = Jogador(400, 400, 100, 100)

class Collectible:

    def __init__(self, x_pos, y_pos, imagem, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.imagem = pygame.transform.scale(imagem, (self.width, self.height))
        self.collided = False
        self.out_of_screen = False

    def draw_collec(self):
        screen.blit(self.imagem, (self.x_pos, self.y_pos))

    def movement(self):

        self.x_pos -= 10

        if self.x_pos < -2 * self.width: # in order to make the collectible disappear from the screen, but stop being drawn
            self.out_of_screen = True

        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50) 

def creating_collectibles(list_all_collects, i):
    
    list_all = list_all_collects[i]['lista completa']
    list_y = [380, 450, 520, 590]
    available_y = list_y[::]
    img = list_all_collects[i]['imagem']
    wid = list_all_collects[i]['width']
    hei = list_all_collects[i]['height']
    
    # defining a random number of appearances for the collectibles
    amount_collect = randint(1, 2)

    while len(list_all) < amount_collect:

        x_collect = width # we want the collectibles to always go from the right side to the left side
        y_collect = random.choice(available_y) # generating a random y-axis position for the collectible

        # adding the random-yet-adequate y-axis position to the list of positions
        available_y.remove(y_collect)

        # creating the objects of the class Collectible with the generated random positions
        collectible = Collectible(x_collect, y_collect, img, wid, hei)

        # adding the newly-created collectible to the list with the other collectibles of the same kind
        list_all.append(collectible)

    return list_all, list_y

# creating a list in order to store the particular attributes of the different types of objects used during the game

list_all_collects = [{'nome': 'sanduiche', 'points': 1, 'imagem': "imagens_jogo/sanduiche.png", 'lista completa': [], 'lista pos y' :[], 'width': 55, 'height': 40}, {'nome': 'passagem', 'points': 1, 'imagem': "imagens_jogo/passagem.png", 'lista completa': [], 'lista pos y' :[], 'width': 45, 'height': 28}, {'nome': 'tamarindo', 'points': 0, 'imagem': "imagens_jogo/tamarindo.png", 'lista completa': [], 'lista pos y' :[], 'width': 40, 'height': 55}, {'nome': 'bola', 'points': -1, 'imagem': "imagens_jogo/bola.png", 'lista completa': [], 'lista pos y' :[], 'width': 75, 'height': 75}]
list_probabilities = [0, 0, 0, 0, 1, 2, 3]
# filling the lists created inside the dictionaries 

def PrimeiroPreenchimento():

    for i in range(4):

        list_all_collects[i]['imagem'] = pygame.image.load(list_all_collects[i]['imagem']).convert_alpha()
        list_all_collects[i]['lista completa'], list_all_collects[i]['lista pos y'] = creating_collectibles(list_all_collects, i)
    
def PreenchSeguintes(obstaculos):

    for i in range(4):

        if not list_all_collects[i]['lista completa']: # if there aren't any objects of this type available, let's go through their creation process again!

            list_all_collects[i]['lista completa'], list_all_collects[i]['lista pos y'] = creating_collectibles(list_all_collects, i)

        remaining_all = []
        remaining_y_pos = []

        for collectible in list_all_collects[i]['lista completa']:

            # creating the collision conditional
            if chaves.rect.colliderect(collectible.rect):

                collectible.collided = True
                
            # keeping on drawing the collectible, if it was not caught by the player or if it's an obstacle
            if ((i != 3 and not collectible.collided) or i == 3) and not collectible.out_of_screen:
                
                collectible.draw_collec()
                collectible.movement()
                remaining_all.append(collectible)
                remaining_y_pos.append(collectible.y_pos)

            if i == 3: # adicionando os objetos bola à lista de obstáculos
            
                obstaculos.append(collectible.rect)

        # recreating the list of all collectibles only with the ones actually available
        
        list_all_collects[i]['lista completa'] = remaining_all
        list_all_collects[i]['lista pos y'] = remaining_y_pos
        # recreating the list of all collectibles only with the ones actually available
        
        list_all_collects[i]['lista completa'] = remaining_all
        list_all_collects[i]['lista pos y'] = remaining_y_pos