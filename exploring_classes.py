
# today, my goal is to explore classes and make collectibles that appear randomly on the screen and move from the right side of the screen to the left
# later, these colletibles will be represented as sprites, but, for now, I'm just going to draw some shapes on the screen and work on the fundamental logic
import pygame
from pygame.locals import *
from sys import exit
import random
from random import randint

# defining my screen's measures
width = 860
height = 640
screen = pygame.display.set_mode((width, height))

# creating the player
player_x = 20
player_y = 2 * height//3

# creating the collectible's class

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
    list_y = [fifth_height, fifth_height * 2, fifth_height * 3, fifth_height * 4]
    img = list_all_collects[i]['imagem']
    wid = list_all_collects[i]['width']
    hei = list_all_collects[i]['height']
    
    # defining a random number of appearances for the collectibles
    amount_collect = randint(1, 3)

    while len(list_all) < amount_collect:

        x_collect = width # we want the collectibles to always go from the right side to the left side
        y_collect = random.choice(list_y) # generating a random y-axis position for the collectible

        # adding the random-yet-adequate y-axis position to the list of positions
        list_y.append(y_collect)

        # creating the objects of the class Collectible with the generated random positions
        collectible = Collectible(x_collect, y_collect, img, wid, hei)

        # adding the newly-created collectible to the list with the other collectibles of the same kind
        list_all.append(collectible)

    return list_all, list_y

# naming some RGB tuples
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
light_green = (128, 200, 128)
pink = (255, 0, 255)
lilac = (200, 162, 200)

fifth_height = height // 5 # the actual screen starts at 300

# creating a list in order to store the particular attributes of the different types of objects used during the game

list_all_collects = [{'nome': 'sanduiche', 'points': 1, 'imagem': "imagens_jogo/sanduiche.png", 'lista completa': [], 'lista pos y' :[], 'width': 70, 'height': 50}, {'nome': 'passagem', 'points': 1, 'imagem': "imagens_jogo/passagem.png", 'lista completa': [], 'lista pos y' :[], 'width': 70, 'height': 50}, {'nome': 'tamarindo', 'points': 0, 'imagem': "imagens_jogo/tamarindo.png", 'lista completa': [], 'lista pos y' :[], 'width': 30, 'height': 50}, {'nome': 'bola', 'points': -1, 'imagem': "imagens_jogo/bola.png", 'lista completa': [], 'lista pos y' :[], 'width': 50, 'height': 50}]

# filling the lists created inside the dictionaries 

for i in range(4):

    list_all_collects[i]['imagem'] = pygame.image.load(list_all_collects[i]['imagem']).convert_alpha()
    list_all_collects[i]['lista completa'], list_all_collects[i]['lista pos y'] = creating_collectibles(list_all_collects, i)
    

# creating a clock

clock = pygame.time.Clock()

while True:

    clock.tick(20)

    screen.fill(light_green)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # controlling the player

    player_x_speed = 10
    player_y_speed = 10

    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:

        player_y -= player_y_speed

    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:

        player_y += player_y_speed

    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:

        player_x += player_x_speed

    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:

        player_x -= player_x_speed

    # drawing the player
    player = pygame.draw.rect(screen, pink, (player_x, player_y, 100, 100))

    # drawing the collectibles based on which of them were already collected or lost

    for i in range(4):

        if not list_all_collects[i]['lista completa']: # if there aren't any objects of this type available, let's go through their creation process again!

            list_all_collects[i]['lista completa'], list_all_collects[i]['lista pos y'] = creating_collectibles(list_all_collects, i)

        remaining_all = []
        remaining_y_pos = []

        for collectible in list_all_collects[i]['lista completa']:

            # creating the collision conditional
            if player.colliderect(collectible.rect):

                collectible.collided = True
                
            # keeping on drawing the collectible, if it was not caught by the player or if it's an obstacle
            if ((i != 3 and not collectible.collided) or i == 3) and not collectible.out_of_screen:
                
                collectible.draw_collec()
                collectible.movement()
                remaining_all.append(collectible)
                remaining_y_pos.append(collectible.y_pos)

        # recreating the list of all collectibles only with the ones actually available
        
        list_all_collects[i]['lista completa'] = remaining_all
        list_all_collects[i]['lista pos y'] = remaining_y_pos
        # recreating the list of all collectibles only with the ones actually available
        
        list_all_collects[i]['lista completa'] = remaining_all
        list_all_collects[i]['lista pos y'] = remaining_y_pos


    pygame.display.flip()