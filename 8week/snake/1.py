import random
import time
import pygame

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
level_font = pygame.font.SysFont("comicsansms", 35)



#to see the score on the screen
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [10, 10])

#to see the level on the screen
def Your_level(level):
    value1 = level_font.render("Level: " + str(level), True, black)
    dis.blit(value1, [10, 40])

#to see our snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#выводит сообщение на экран
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    direction = 'RIGHT'
    change_to = direction

    snake_List = []
    Length_of_snake = 1
    level = 1
    foods = []

    #еда появляется в рандомных местах
    foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
    foodn = round(random.randrange(0, dis_width - 15) / 10) * 10
    foodm = round(random.randrange(0, dis_height - 15) / 10) * 10

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

        #restart or quit the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #move the snake
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Если две клавиши нажаты одновременно
        # мы не хотим, чтобы змея разделялась на две
        # направлений одновременно
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Перемещение змеи
        if direction == 'UP':
            y1-=10
        if direction == 'DOWN':
            y1+=10
        if direction == 'LEFT':
            x1-=10
        if direction == 'RIGHT':
            x1+= 10

        #проигрышь при столкновение с границей
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        dis.fill(blue)
        #draw the food
        if Length_of_snake % 5 !=0:
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        elif Length_of_snake % 5 == 0:
            pygame.draw.rect(dis, green, [foodn, foodm, 15, 15])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        #проигрышь при столкновение в свое тело
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # check for collision with the snake's body
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Your_level(level)

        pygame.display.update()

        # check for collision with food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            Length_of_snake += 1
        if x1 == foodn and y1 == foodm:
            foodn = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foodm = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            Length_of_snake += 2

        #increase the speed and level
        if Length_of_snake >=0 and Length_of_snake < 5:
            snake_speed = 15
            level = 1
        elif Length_of_snake >= 5 and Length_of_snake < 10:
            snake_speed = 20
            level = 2
        elif Length_of_snake >= 10:
            snake_speed = 30
            level = 3

        # fps of the game
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()