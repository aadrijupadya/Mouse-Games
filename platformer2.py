#Better Version of the game (no glitches)
import pygame
import time
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((760,400))
pygame.display.set_caption("Bare min")

black=(0,0,0)

man=pygame.image.load('char.png')
man=pygame.transform.scale(man, (20,20))

tile=pygame.image.load("freescifiplatform/png/Tiles/Tile (1).png")
tile=pygame.transform.scale(tile, (40,40))

coin=pygame.image.load('coin.jpeg')
coin=pygame.transform.scale(coin, (40, 40))

#layer = [1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1]

##TwoDlayer = [[1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,1],
##             #[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##             [0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0],
##             [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##             [1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1],
##             [0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0],
##             #[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##             [1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1]]

TwoDlayer = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
             [1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1],
             [1,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,0,0,1],
             [1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1],
             [1,2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2,1],
             [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1],
             [1,0,0,2,0,0,2,0,0,2,0,0,2,0,0,2,0,0,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],    
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
x1=40
y1=320

jumpcount=0
counter=0

right=False
left=False
up=False
canRight=False
canLeft=False
canJump=False

tilelist=[]
coinlist=[]
collected=[]

white=(255, 255, 255)
black=(0, 0, 0)
green=(0, 255, 0)

def collision():
    global fall
    global right
    global up
    global left
    global canRight
    global canLeft
   
    for i in tilelist:
        if i.colliderect(m):
            #print(m.bottom,i.top)
            #print(m.left, i.right)
            #print(m.top,i.bottom)
            if m.bottom==i.top+1:
                fall=False
            if m.top+4==i.bottom:
                #print("Hii")
                up=False
            if i.top+1<m.bottom and m.right==i.left+1:
                #print("ey")
                canRight=False
                right=False
            if i.top+1<m.bottom and m.left+1==i.right:
                #print('Hi')
                left=False
                canLeft=False

    for i in coinlist:
        if m.colliderect(i):
            x=i.left
            y=i.top
            collected.append((x,y))
            #print(i.left, i.top)

def show_text(string, x, y, color):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(string, True, color)
    textRect = text.get_rect() 
    textRect.center = (x, y)
    screen.blit(text, textRect)
   
while True:
    ##screen.fill(black)
    m=screen.blit(man, (x1,y1))

    x=0
    y=360
   
    fall=True
    canRight=True
    canLeft=True

    tilelist=[]
    coinlist=[]
   
##    for i in layer:
##        if i==1:
##            t=screen.blit(tile, (x,360))
##            tilelist.append(t)
##            x+=40
##        else:
##            x+=40
   
    for i in TwoDlayer:
        for j in i:
            if j==1:
                t=screen.blit(tile, (x,y))
                tilelist.append(t)

            elif j==2:
                if (x,y) not in collected:
                    c=screen.blit(coin, (x,y))
                    coinlist.append(c)
                else:
                    pass
            x+=40
        x=0
        y-=40

    if len(collected)==22:
        for i in range(4):
            time.sleep(2)
            screen.fill(white)
            show_text("LEVEL COMPLETED!", 350,150, green)
            time.sleep(2)
            screen.fill(black)
            show_text("LEVEL COMPLETED!", 350,150, green)
            time.sleep(2)
    collision()
   
    if x1<0:
        x1=0
       
    if x1+40>760:
       x1=720
      
    if canLeft and left:
        x1-=1
       
    if canRight and right:
            x1+=1
           
    if up:
        y1-=5
        jumpcount+=1
        if jumpcount==50:
            up=False
            jumpcount=0
   
    if fall:
        y1+=1
   
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==KEYDOWN:
            if event.key==K_RIGHT:
                    right=True
                    left=False
            elif event.key==K_LEFT:
                left=True
                right=False
            elif event.key==K_UP:
                if fall==False:
                    up=True
        elif event.type==KEYUP:
                right=False
                left=False
                up=False
           
    pygame.display.update()
