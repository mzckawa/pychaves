
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

    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 50
        self.height = 50
        self.speed = 10
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.collected = False
        self.lost = False

    def draw_collec(self):
        pygame.draw.rect(screen, lilac, self.rect)

    def movement(self):

        self.x_pos -= self.speed

        if self.x_pos < -2 * self.width: # in order to make the collectible disappear from the screen, but stop being drawn
            self.lost = True

        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 50, 50) 

    def get_velocidade(self, velocidade):

        self.speed = velocidade




# naming some RGB tuples
black = (0, 0, 0)
white = (255, 255, 255)
light_green = (128, 200, 128)
pink = (255, 0, 255)
lilac = (200, 162, 200)

fifth_height = height // 5

 # atstarts at 300

def creating_collectibles(classcollec):
    
    list_all = []
    list_y = [fifth_height, fifth_height * 2, fifth_height * 3, fifth_height * 4]
    
    # defining a random number of appearances for the collectibles
    amount_collect = randint(1, 3)

    while len(list_all) < amount_collect:

        x_collect = width # we want the collectibles to always go from the right side to the left side
        y_collect = random.choice(list_y) # generating a random y-axis position for the collectible

        # adding the random-yet-adequate y-axis position to the list of positions
        list_y.append(y_collect)

        # creating the objects of the class Collectible with the generated random positions
        collectible = classcollec(x_collect, y_collect)

        # adding the newly-created collectible to the list with the other collectibles of the same kind
        list_all.append(collectible)

    return list_all, list_y

# creating lists to store the collectibles more easily

class Collectible1(Collectible):

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

    def draw_collec(self):
        pygame.draw.rect(screen, white, self.rect)

   
class Collectible2(Collectible):

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        

    def draw_collec(self):
        pygame.draw.rect(screen, lilac, self.rect)

class Collectible3(Collectible):

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        

    def draw_collec(self):
        pygame.draw.rect(screen, black, self.rect)

class Collectible3(Collectible):

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        

    def draw_collec(self):
        pygame.draw.rect(screen, black, self.rect)

all_collects_1, y_pos_collec_1 = creating_collectibles(Collectible1)
all_collects_2, y_pos_collec_2 = creating_collectibles(Collectible2)
all_collects_3, y_pos_collec_3 = creating_collectibles(Collectible3)

# creating a clock

clock = pygame.time.Clock()

while True:

    clock.tick(30)

    screen.fill(light_green)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # controlling the player

    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:

        player_y -= 10

    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:

        player_y += 10

    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:

        player_x += 10

    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:

        player_x -= 10

    # drawing the player
    player = pygame.draw.rect(screen, pink, (player_x, player_y, 100, 100))

    # drawing the collectibles based on which of them were already collected or lost

    remaining_collect_1 = []
    remaining_y_pos_1 = []

    remaining_collect_2 = []
    remaining_y_pos_2 = []

    remaining_collect_3 = []
    remaining_y_pos_3 = []

    for collectible in all_collects_1:

        # creating the collision conditional
        if player.colliderect(collectible):
            collectible.collected = True

        # keeping on drawing the collectible, if it was not caught by the player
        if not collectible.collected:
            collectible.draw_collec()
            collectible.movement()

        if not collectible.collected and not collectible.lost:

            remaining_collect_1.append(collectible)
            remaining_y_pos_1.append(collectible.y_pos)

    # recreating the list of all collectibles only with the ones actually available
    all_collects_1 = remaining_collect_1
    y_pos_collec_1 = remaining_y_pos_1

    if not all_collects_1 and not y_pos_collec_1: # let's go all over again!

        all_collects_1, y_pos_collec_1 = creating_collectibles(Collectible1)


    for collectible in all_collects_2:

        # creating the collision conditional
        if player.colliderect(collectible):
            collectible.collected = True

        # keeping on drawing the collectible, if it was not caught by the player
        if not collectible.collected:
            collectible.draw_collec()
            collectible.movement()

        if not collectible.collected and not collectible.lost:

            remaining_collect_2.append(collectible)
            remaining_y_pos_2.append(collectible.y_pos)

    # recreating the list of all collectibles only with the ones actually available
    all_collects_2 = remaining_collect_2
    y_pos_collec_2 = remaining_y_pos_2

    if not all_collects_2 and not y_pos_collec_2: # let's go all over again!

        all_collects_2, y_pos_collec_2 = creating_collectibles(Collectible2)

    for collectible in all_collects_3:

        # creating the collision conditional
        if player.colliderect(collectible):
            collectible.collected = True

        # keeping on drawing the collectible, if it was not caught by the player
        if not collectible.collected:
            collectible.draw_collec()
            collectible.movement()

        if not collectible.collected and not collectible.lost:

            remaining_collect_3.append(collectible)
            remaining_y_pos_3.append(collectible.y_pos)

    # recreating the list of all collectibles only with the ones actually available
    all_collects_3 = remaining_collect_3
    y_pos_collec_3 = remaining_y_pos_3

    if not all_collects_3 and not y_pos_collec_3: # let's go all over again!

        all_collects_3, y_pos_collec_3 = creating_collectibles(Collectible3)

    pygame.display.flip()
