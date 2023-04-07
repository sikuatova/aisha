import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Circle")
x, y = 300, 300
clock = pygame.time.Clock()

while True:
    screen.fill("white")
    circle = pygame.draw.circle(screen, ("red"), (x, y), 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if y >= 25: 
            y -= 4
    if pressed[pygame.K_DOWN]: 
        if y <= 575:
            y += 4
    if pressed[pygame.K_LEFT]: 
        if x >= 25:
            x -= 4
    if pressed[pygame.K_RIGHT]: 
        if x <= 575:
            x += 4
    pygame.display.update()
    clock.tick(60)