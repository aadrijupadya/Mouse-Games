import pygame
import random
import time
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('flappy bird')
x_bird = 300
y_bird = 300
y_bird_change = 4
score_str = '0'
x = 600
y = 400
z = 200
var = 1
l = random.randint(20,400)
a = random.randint(20,400)
b = random.randint(20,400)
white = (255,255,255)
red = (255,0,0)

x_change = 2
y_change = 2
z_change = 2
score = 0
endgame = False
def show_text(msg,X,Y,color):
    fontobj=pygame.font.SysFont("freesans",50)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj,(X,Y))
while True:
    if var == 1:
        time.sleep(1)
        var+=1
    else:
        pass
    screen.fill((0,0,1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_bird_change = -4
                y_bird+=y_bird_change
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                y_bird_change = 4
    bird = pygame.draw.circle(screen,(255,255,0), (x_bird,y_bird), (10))
    rect1 = pygame.draw.rect(screen,(255,255,0), (x,0,30,l))
    rect2 = pygame.draw.rect(screen,(255,255,0), (x,600-(400-l),30,400-l))
    rect3 = pygame.draw.rect(screen,(255,255,0), (y,0,30,a))


    rect4 = pygame.draw.rect(screen,(255,255,0), (y,600-(400-a),30,400-a))
    rect5 = pygame.draw.rect(screen,(255,255,0), (x,0,30,l))
    rect6 = pygame.draw.rect(screen,(255,255,0), (z,0,30,b))

    pygame.draw.rect(screen,(255,255,0), (z,600-(400-b),30,400-b))

    x-=x_change
    y-=y_change
    z-=z_change



    if x <= 0:
        score += 1
        score_str = str(score)
##        
        x = 600
        l = random.randint(20,400)
        rect1 = pygame.draw.rect(screen,(255,255,0), (x,0,30,l))
        rect2 = pygame.draw.rect(screen,(255,255,0), (x,600-(400-l),30,400-l))
   
    if y <= 0:
        score += 1
        score_str = str(score)
##        show_text(('Score:',score_str),10,10)
        y = 600
        a = random.randint(20,400)
        rect3 = pygame.draw.rect(screen,(255,255,0), (y,0,30,a))
        rect4 = pygame.draw.rect(screen,(255,255,0), (y,600-(400-a),30,400-a))
    if z <= 0:
        score += 1
        score_str = str(score)
##        show_text(('Score:',score_str),10,10)
        z = 600
        b = random.randint(20,400)
        rect5 = pygame.draw.rect(screen,(255,255,0), (z,0,30,b))
        rect6 = pygame.draw.rect(screen,(255,255,0), (z,600-(400-b),30,400-b))
    show_text(score_str,10,10,white)

     ##if x <= x_bird <= x+30:
##        if l <= y_bird <= 600-(400-l):
##            continue
##        else:
##            ##show_text('GAME OVER!',10,10)
##            print('game over')  
##            break
    if bird.colliderect(rect1) or bird.colliderect(rect2):
        endgame = True
        
    ##if y <= x_bird <= y+30:
##        if a <= y_bird <= 600-(400-a):
##            continue
##        else:
##            ##show_text('GAME OVER!',10,10)
##            print('game over')  
##            break
    if bird.colliderect(rect3) or bird.colliderect(rect4):
        endgame = True
##    if z <= x_bird <= z+30:
##        if b <= y_bird <= 600-(400-b):
##            continue
##        else:
##            ##show_text('GAME OVER!',10,10)
##            print('game over')  
##            break
    if bird.colliderect(rect5) or bird.colliderect(rect6):
        endgame = True
    if y_bird >= 600:
        ##show_text('GAME OVER!',10,10)
        print('game over')  
        break
    if y_bird <= 0:
        ##show_text('GAME OVER!',10,10)
        print('game over')  
        break
            

    if endgame == True:
        show_text('GAME OVER',150,300,red)
        pygame.display.update()
        break
        
    y_bird+=y_bird_change
    pygame.display.update()
    
