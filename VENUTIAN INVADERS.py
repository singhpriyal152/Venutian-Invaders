import pygame
import random
import math
from pygame import mixer


pygame.init()

#Title and Icon of game
pygame.display.set_caption("Venutian Invaders")
icon= pygame.image.load('bulletbots.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background image.jpg')
mixer.music.load("Backgroundmusic.mp3")
mixer.music.play(-1)
stopbots=False
counter_score1=0
counter_score2=0

#adding main hero
heroImg = pygame.image.load('Spaceship.png')
heroX = 370
heroY = 480
heroX_change = 0


def hero(x, y):
    screen.blit(heroImg, (x, y))



#adding bullets for our hero
bul3Img = pygame.image.load('playerbullet.png')
bul3X = 0
bul3Y = 520
bul3X_change = 0
bul3Y_change = 8
bul3_state = "ready"

def bullets3(x, y):
    global bul3_state
    bul3_state = "fire"
    screen.blit(bul3Img, (x + 16, y + 10))


#adding minibot1
miniImg=pygame.image.load('minispaceship.png')
miniX = 0
miniY= 360
minix_change=1

def minibot(x,y):

    screen.blit(miniImg,(x, y))

#bulletsfor left minibots implementation
bulImg=pygame.image.load('herosbullet.png')

bulX =416
bulY=360
bulx_change=0
buly_change=4
bul_state="ready"

def minibullets(x,y):
    global bul_state
    bul_state="fire"
    screen.blit(bulImg,(x+16, y+10))

#adding minibot2
miniImg2=pygame.image.load('minispaceship.png')
miniX2 = 748
miniY2= 360
minix2_change=1


def minibot2(x,y):
    screen.blit(miniImg2,(x, y))

 #bullets for right mini bots
bul2Img=pygame.image.load('herosbullet.png')

bul2X =416
bul2Y=360
bul2x_change=0
bul2y_change=4
bul_state="ready"

def minibullets2(x,y):
   
    screen.blit(bul2Img,(x+16, y+10))





# displaying score 
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

#collision images
explosionImg= pygame.image.load('explosion3.png')
explosion1X=0
explosion2X=0
explosionY=360

def explosion(x,y):
    screen.blit(explosionImg, (x + 16, y + 10))

# game over text
gameover_font = pygame.font.Font('font.otf', 100)
def game_over_text():
    over_text = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    mixer.music.stop()
    Gameover_Sound = mixer.Sound("gameover3.wav")
    Gameover_Sound.play()    
    
#adding enemies
eneImg = []
eneX = []
eneY = []
eneX_change = []
eneY_change = []
num_of_enemies = 7
eneX_speed=0.1
eneY_speed=4
changeX= 0.005
changeY=0.005

for i in range(num_of_enemies):
    eneImg.append(pygame.image.load('enemy448.png'))
    eneX.append(random.randint(0, 736))
    eneY.append(random.randint(50, 100))
    eneX_change.append(eneX_speed)
    eneY_change.append(eneY_speed)



def aliens(x, y, i):
    screen.blit(eneImg[i], (x, y))



#if collision occurs
def isCollision(eneX, eneY, bul3X, bul3Y,dist):
    distance = math.sqrt(math.pow(eneX - bul3X, 2) + (math.pow(eneY - bul3Y, 2)))
    if distance < dist:
        return True
    else:
        return False






def change():
    global changeX
    global changeY
    changeX+=0.00002
    changeY+=0.002



running = True
while running:

    
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        #if keystroke is pressed

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                heroX_change = -2
            if event.key == pygame.K_RIGHT:
                heroX_change = 2



            if event.key == pygame.K_SPACE:
                if bul3_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                  
                    bul3X = heroX
                    bullets3(bul3X, bul3Y)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                heroX_change = 0



    #Heros Movement

    heroX += heroX_change
    if heroX <= 0:
        heroX = 0
    elif heroX >= 736:
        heroX = 736



    #minibot towards left
    miniX+=minix_change
    
   
    if miniX<=0:
        miniX=0
        minix_change=1
    
    elif miniX>=370:
        miniX=370
        minix_change=-1



    # minibot towards right
    miniX2+=minix2_change
    
    if miniX2>=748:
        miniX2=748
        minix2_change=-1
    elif miniX2<=378:
        miniX2=378
        minix2_change=1


#bullet movement for left minibot

    if bulY<=0:
        bulY=360
        bul_state="ready"
    
    if bul_state is "ready":
        bulX=miniX
   

#bullet movement for right minibot
    if bul2Y<=0:
        bul2Y=360
        bul_state="ready"


    if bul_state is "ready":
        bul2X=miniX2  
    
    if stopbots==False:

        minibullets(bulX,bulY)
        bulY-=buly_change

        minibullets(bul2X,bul2Y)
        bul2Y-=bul2y_change

        minibot(miniX,miniY)
        minibot2(miniX2,miniY2)
        explosion1X=miniX

        explosion1X=miniX2

    else:
        explosion(explosion1X,explosionY)
        explosion(explosion2X,explosionY)


#alien movement

    for i in range(num_of_enemies):

        #Game Over code
        if eneY[i] > 430:
            for j in range(num_of_enemies):
                eneY[j] = 2000
            game_over_text()
            break



        eneX[i] += eneX_change[i]
        if eneX[i] <= 0:
            eneX_change[i] = 0.5 + changeX
            eneY[i] += eneY_change[i] + changeY
        elif eneX[i] >= 736:
            eneX_change[i] = -0.5 - changeX
            eneY[i] += eneY_change[i] + changeY
        
        if(eneY[i]>345):
            stopbots=True

#collision for left minibot
        collision = isCollision(eneX[i], eneY[i], bul3X, bul3Y,27)
        if collision:
   
            
            score_value += 1
            bul3Y = 480
            bul3_state = "ready"
            eneX[i] = random.randint(0, 736)
            eneY[i] = random.randint(50, 150)




        #collision for right minibot
        collision2 = isCollision(eneX[i], eneY[i], bulX, bulY,10)

        if collision2:
            counter_score1+=1
            if(counter_score1>10):
                score_value += 1
                counter_score1=0
              
             
                bulY=360
                bul_state="ready"
                eneX[i] = random.randint(0, 736)
                eneY[i] = random.randint(50, 150)




 #collision for hero
        collision3 = isCollision(eneX[i], eneY[i], bul2X, bul2Y,10)     
        if collision3:
            counter_score2+=1
            
            if(counter_score2>10):
                score_value += 1
                counter_score2=0
            


        aliens(eneX[i], eneY[i], i)

 
    collision4 = isCollision(miniX, miniY, bul3X, bul3Y,27)
    collision5 = isCollision(miniX2, miniY2, bul3X, bul3Y,27)
    
    if stopbots == False:
        if collision4 or collision5:
            score_value-=5
            bul3Y=480
            bul3_state="ready"
        

        

  
    # Bullet Movement for hero
    if bul3Y <= 0:
        bul3Y = 480
        bul3_state = "ready"

    if bul3_state is "fire":
        bullets3(bul3X, bul3Y)
        bul3Y -= bul3Y_change


   
    change()
    

    show_score(textX, testY)
    hero(heroX, heroY)
    pygame.display.update()