import pygame
from random import *

W, H = 90, 60
tile = 10
dy = 0
pygame.init()
screen = pygame.display.set_mode((W * tile, H * tile))
pygame.display.set_caption("Ping_pong")
clock = pygame.time.Clock()
running = True
Fps = 40
board = [10, 240, 30, 140]
board_a = [860, 240, 30, 140]
ball_params = [450, 280]
radius = 20
ball_speed_x = 16
ball_speed_y = 16
speed = 10
player_1_score = 0
player_2_score = 0
ball_speed = [ball_speed_x,ball_speed_y]
timer = 0 
timer_interval = 5              
myfont = pygame.font.Font("images/txt.ttf",40)
while running:
    keys = pygame.key.get_pressed()  

    if keys[pygame.K_w]:
        dy = -speed
    elif keys[pygame.K_s]:
        dy = speed
    else:
        dy = 0
    if board[1] < 0 :
        board[1] = 0
    elif board[1] > (H * tile - board[3]):
        board[1] = H * tile - board[3]
    board[1] += dy
  
    if keys[pygame.K_UP]:
        dy = -speed
    elif keys[pygame.K_DOWN]:
        dy = speed
    else:
        dy = 0
    if board_a[1] < 0 :
        board_a[1] = 0
    elif board_a[1] > (H * tile - board[3]):
        board_a[1] = H * tile - board[3]
    board_a[1] += dy
    ball_params[0] +=ball_speed[0]
    ball_params[1] +=ball_speed[1]
    ball_rect = pygame.Rect(ball_params[0]- radius, ball_params[1]- radius, 2* radius, 2*radius)
    board_rect = pygame.Rect(board[0],board[1],board[2],board[3])
    board_a_rect = pygame.Rect(board_a[0],board_a[1],board_a[2],board_a[3])
    if ball_params[1] - radius < 0 or ball_params[1] + radius > H * tile:
        ball_speed[1] = -ball_speed[1]

    if ball_rect.colliderect(board_rect) or ball_rect.colliderect(board_a_rect):
        ball_speed[0] = -ball_speed[0]
        ball_speed[1] = randint(-3,3)


        
    if ball_params[0] - radius < 0:
        player_2_score += 1
        ball_params = [450,280]
        ball_speed = [ball_speed_x,ball_speed_y]
        pygame.time.delay(1000)
    elif ball_params[0] + radius > W *tile :
        player_1_score += 1
        ball_params = [450,280]
        ball_speed = [ball_speed_x,ball_speed_y]
        pygame.time.delay(1000)
    timer += clock.get_time()  / 1000
    if timer >= timer_interval:
        ball_speed[0] *= 1.2
        ball_speed[1] *= 1.2
        timer = 0

    screen.fill("black")
    player_1_score_text = myfont.render("Player 1 score:"+str(player_1_score),False,"white")
    player_2_score_text = myfont.render("Player 2 score:"+str(player_2_score),False,"white")
    screen.blit(player_1_score_text,(10,10))
    screen.blit(player_2_score_text,(486,10))
    pygame.draw.rect(screen, "gray", board)
    pygame.draw.rect(screen, "gray", board_a)
    pygame.draw.circle(screen, "gray", ball_params, radius)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    clock.tick(Fps)