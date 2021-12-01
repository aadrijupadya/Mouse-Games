import pygame
import time
import random
from pygame.locals import *
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Pong')
screen.fill((0,0,1))
z = random.randint(0,10)
x = 10
y = 300
cnt = 10
y2 = 300
x2 = 580
flag = 0
bounce_x = 10
bounce_y = z
ball_x = 300
ball_y = 300
score1 = 0
score2 = 0
string_var = '0'
string_var2 = '0'
def show_text(msg,x,y):
    fontobj=pygame.font.SysFont("freesans",15)
    msgobj = fontobj.render(msg, False, 'white')
    screen.blit(msgobj,(x,y))
while True:
    clock = pygame.time.Clock()
    clock.tick(50)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                flag = 1
            if event.key == pygame.K_DOWN:
                flag = 2
            if event.key == pygame.K_w:
                flag = 4
            if event.key == pygame.K_s:
                flag = 5
        if event.type == pygame.KEYUP:
            flag = 3
        
            
    pygame.draw.rect(screen,(255,255,255),(x,y,10,50))
    pygame.draw.circle(screen,(255,255,255),(ball_x,ball_y),10)

    pygame.draw.rect(screen,(255,255,255),(x2,y2,10,50))
     
    if x+10 == ball_x and y <= ball_y < y+50:
        bounce_x = 10
        
    if x2 == ball_x and y2 <= ball_y <= y2+50:
        bounce_x = -10
        
    if ball_y >= 590:
        bounce_y = -10
        
    if ball_y <= 10:
        bounce_y = 10
    ball_x+=bounce_x
    ball_y+=bounce_y

    if y > 550:
        cnt = -10
    if y < 0:
        cnt = 10
    if flag == 1:
        y2-=10
    if flag == 2:
        y2+=10
    if flag == 3:
        y2 = y2
        y = y
    if flag == 4:
        y-=10
    if flag == 5:
        y+=10
    if ball_x > 600:
        n = random.randint(0,10)
        ball_x = 300
        ball_y = 300
        bounce_x * -1
        bounce_y = n
        
        score1 +=1
        string_var = str(score1)
        string_var2 = str(score2)
    show_text(string_var, 280,50)
    show_text(string_var2, 320,50)
    if ball_x < 0:
        n = random.randint(0,2)
        ball_x = 300
        ball_y = 300
        bounce_x * -1
        bounce_y = n
        score2 +=1
        string_var = str(score1)
        string_var2 = str(score2)
    show_text(string_var2, 320,50)
    show_text(string_var, 280,50)
        
        

    
    
    
    pygame.display.update()
    screen.fill((0,0,1))

##things to fix: glitches very randomly, score only visible for half a second
