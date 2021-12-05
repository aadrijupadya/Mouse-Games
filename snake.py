import pygame
import random
import time
pygame.init
pygame.font.init()
endgame = False
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption('Snake game')
foodx = (random.randint(0,300) // 10 ) * 10
foody = (random.randint(0,300) // 10 ) * 10
snakex = (random.randint(0,300) // 10 ) * 10
snakey = (random.randint(0,300) // 10 ) * 10
flag = 0
score = 0
white = (255,255,255)
score_str = '0'
snakelist = []
snakelist.append([snakex,snakey])
def show_text(msg,X,Y,color):
    fontobj=pygame.font.SysFont("freesans",50)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj,(X,Y))

while True:
    snakelist.insert(0,[snakex,snakey])
    snakelist.pop()
    screen.fill((0,0,1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                flag = 1
            if event.key == pygame.K_UP:
                flag = 2
            if event.key == pygame.K_LEFT:
                flag = 3
            if event.key == pygame.K_RIGHT:
                flag = 4
    food = pygame.draw.rect(screen, (255,0,0), (foodx,foody,10,10))
    for segment in snakelist:
        print(segment)
        snakehead = pygame.draw.rect(screen, (0,255,0), segment+[10,10])
    if flag == 1:
        snakey+=2
    if flag == 2:
        snakey-=2
    if flag == 3:
        snakex-=2
    if flag == 4:
        snakex+=2
    if snakex < 0:
        endgame = True
    if snakex > 300:
        endgame = True
    if snakey > 300:
        endgame = True
    
    if snakey < 0:
        endgame = True
    
    for i in range(1,len(snakelist),1):
        if snakex==snakelist[i][0] or snakey==snakelist[i][1]:
            break
    if snakehead.colliderect(food):
        score+=1
        score_str = str(score)
        foodx = (random.randint(0,300) // 10 ) * 10
        foody = (random.randint(0,300) // 10 ) * 10
        food = pygame.draw.rect(screen, (255,0,0), (foodx,foody,10,10))
        snakelist.append([snakex,snakey])

    show_text(score_str,10,10,white)
    if endgame:
        show_text('GAME OVER',0,100,white)
        pygame.display.update()
        break
    snakehead = pygame.draw.rect(screen,(0,255,0),(snakex, snakey,10,10))

    pygame.display.update()
