import pygame 

pygame.init()

screen = pygame.display.set_mode((800, 640))

chaves_img = pygame.image.load('chaves_1.jpg').convert()
chaves_img = pygame.transform.scale(chaves_img, (chaves_img.get_width() * 3, chaves_img.get_height() * 2))
chaves_img = pygame.transform.flip(chaves_img, False, True)
chaves_img.set_colorkey((0, 0, 0))

running = True
x = 0 
clock = pygame.time.Clock()
delta_time = 0.1

while running:

    screen.fill((255, 205, 255))

    chaves_img.set_alpha(max(0, 255))
    screen.blit(chaves_img, (x, 30))

    # x += 10 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.wait(1)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
