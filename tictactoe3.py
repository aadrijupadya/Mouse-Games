import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('tictactoe')
screen.fill((0,0,1))
tttdict = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
def draw_X(X,Y):
    pygame.draw.line(screen,(255,255,255), (X,Y), (X+200,Y+200))
    pygame.draw.line(screen,(255,255,255), (X+200,Y), (X,Y+200))
def draw_circle(X,Y):
    pygame.draw.circle(screen, (255,255,255),(X,Y),(75))
win = False
flag = 'X'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if flag == 'X':
                
                if 0 <= x <= 200 and 0 <= y <= 200:
                    if tttdict[1] == '':
                        tttdict[1] = 'X'
                        draw_X(0,0)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
                if 200 < x <= 400 and 0 <= y <= 200:
                    if tttdict[2] == '':
                        tttdict[2] = 'X'
                        draw_X(200,0)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
                    
                if 400 < x <= 600 and 0 <= y <= 200:
                    if tttdict[3] == '':
                        tttdict[3] = 'X'
                        draw_X(400,0)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
                if 0 <= x <= 200 and 200 < y <= 400:
                    if tttdict[4] == '':
                        tttdict[4] = 'X'
                        draw_X(0,200)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
                if 200 < x <= 400 and 200 < y <= 400:
                    if tttdict[5] == '':
                        tttdict[5] = 'X'
                        draw_X(200,200)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
                if 400 < x <= 600 and 200 < y <= 400:
                    if tttdict[6] == '':
                        tttdict[6] = 'X'
                        draw_X(400,200)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
                if 0 <= x <= 200 and 400 < y <= 600:
                    if tttdict[7] == '':
                        tttdict[7] = 'X'
                        draw_X(0,400)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
                if 200 < x <= 400 and 400 < y <= 600:
                    if tttdict[8] == '':
                        tttdict[8] = 'X'
                        draw_X(200,400)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
                if 400 < x <= 600 and 400 < y <= 600:
                    if tttdict[9] == '':
                        tttdict[9] = 'X'
                        draw_X(400,400)
                        flag = 'O'
                    else:
                        print('spot is full, choose another')
            if flag == 'O':
                if 0 <= x <= 200 and 0 <= y <= 200:
                    if tttdict[1] == '':
                        tttdict[1] = 'O'
                        draw_circle(100,100)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
                if 200 < x <= 400 and 0 <= y <= 200:
                    if tttdict[2] == '':
                        tttdict[2] = 'O'
                        draw_circle(300,100)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
                if 400 < x <= 600 and 0 <= y <= 200:
                    if tttdict[3] == '':
                        tttdict[3] = 'O'
                        draw_circle(500,100)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
                if 0 <= x <= 200 and 200 < y <= 400:
                    if tttdict[4] == '':
                        tttdict[4] = 'O'
                        draw_circle(100,300)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
                if 200 < x <= 400 and 200 < y <= 400:
                    if tttdict[5] == '':
                        tttdict[5] = 'O'
                        draw_circle(300,300)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
                if 400 < x <= 600 and 200 < y <= 400:
                    if tttdict[6] == '':
                        tttdict[6] = 'O'
                        draw_circle(500,300)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
                if 0 <= x <= 200 and 400 < y <= 600:
                    if tttdict[7] == '':
                        tttdict[7] = 'O'
                        draw_circle(100,500)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
                if 200 < x <= 400 and 400 < y <= 600:
                    if tttdict[8] == '':
                        tttdict[8] = 'O'
                        draw_circle(300,500)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
                if 400 < x <= 600 and 400 < y <= 600:
                    if tttdict[9] == '':
                        tttdict[9] = 'O'
                        draw_circle(500,500)
                        flag = 'X'
                    else:
                        print('spot is full, choose another')
    if tttdict[1] != '' and tttdict[2] != '' and tttdict[3] != '' and tttdict[1] == tttdict[2] and tttdict[1] == tttdict[3]:
        print('player', tttdict[1], 'has won!')
        win = True
        break
    if tttdict[4] != '' and tttdict[5] != '' and tttdict[6] != '' and tttdict[4] == tttdict[5] and tttdict[4] == tttdict[6]:
        print('player', tttdict[4], 'has won!')
        win = True
        break
    if tttdict[7] != '' and tttdict[8] != '' and tttdict[9] != '' and tttdict[7] == tttdict[8] and tttdict[7] == tttdict[9]:
        print('player', tttdict[7], 'has won!')
        win = True
        break
    if tttdict[1] != '' and tttdict[4] != '' and tttdict[7] != '' and tttdict[1] == tttdict[4] and tttdict[1] == tttdict[7]:
        print('player', tttdict[1], 'has won!')
        win = True
        break
    if tttdict[2] != '' and tttdict[5] != '' and tttdict[8] != '' and tttdict[2] == tttdict[5] and tttdict[2] == tttdict[8]:
        print('player', tttdict[2], 'has won!')
        win = True
        break
    if tttdict[3] != '' and tttdict[6] != '' and tttdict[9] != '' and tttdict[3] == tttdict[6] and tttdict[3] == tttdict[9]:
        print('player', tttdict[3], 'has won!')
        win = True
        break
    if tttdict[1] != '' and tttdict[5] != '' and tttdict[9] != '' and tttdict[1] == tttdict[5] and tttdict[1] == tttdict[9]:
        print('player', tttdict[1], 'has won!')
        win = True
        break
    if tttdict[3] != '' and tttdict[5] != '' and tttdict[7] != '' and tttdict[3] == tttdict[5] and tttdict[3] == tttdict[7]:
        print('player', tttdict[3], 'has won!')
        win = True
        break
    spaces = 0
    for x in tttdict:
        if tttdict[x] == '':
            spaces += 1
    if spaces == 0 and win == False:
        print('Tie game')
        break
    if win == True:
        break
    else:
        pass

    pygame.draw.line(screen,(255,255,255), (200,0), (200,600))
    pygame.draw.line(screen,(255,255,255), (400,0), (400,600))
    pygame.draw.line(screen,(255,255,255), (0,200), (600,200))
    pygame.draw.line(screen,(255,255,255), (0,400), (600,400))
    pygame.display.update()
