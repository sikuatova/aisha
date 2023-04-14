import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
clock = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE2 = 0
coin_speed = 5

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("image/AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("image/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/car2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
     global SCORE
     self.rect.move_ip(0,SPEED)
     if(self.rect.bottom > 600):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("image/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, coin_speed)
        self.image = pygame.transform.scale(self.image, (30, 30))
        if (self.rect.top > 423):
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/coin2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0,coin_speed)
        self.image = pygame.transform.scale(self.image,(30, 30))
        if(self.rect.top>426):
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
E2 = Car()
C1 = Coin()
C2 = Coin_2()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)
all_sprites.add(C1)
all_sprites.add(C2)

single_sprite = pygame.sprite.Group()
single_sprite.add(C2)

coins = pygame.sprite.Group()
coins.add(C1)

coins_2 = pygame.sprite.Group()
coins_2.add(C2)


#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, coins):
        SCORE2 = SCORE + 1
        SCORE += 1
    if pygame.sprite.spritecollideany(P1, coins_2):
        SCORE2 = SCORE + 3
        SCORE += 3

    if SCORE % 5 == 0 and SCORE > 0:
        SPEED += 0.009

    n = random.randint(1, 10)
    if SCORE % n == 0 and SCORE > 0:
        for entity in single_sprite:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r'C:\Users\Айша\OneDrive\Рабочий стол\1week\8week\sound\lab8_racer_sound_tsis_8_9_racer_sound_crash.wav').play()
          pygame.mixer.Sound(r'C:\Users\Айша\OneDrive\Рабочий стол\1week\8week\sound\lab8_racer_sound_tsis_8_9_racer_sound_music_laugh.wav').play()
          time.sleep(2)

          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          pygame.display.update()

          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    clock.tick(FPS)