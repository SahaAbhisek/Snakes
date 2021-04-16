import pygame
import random

pygame.init()

#colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(55,125,65)

#game_window
screen_width=660
screen_height=540
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snakes")
pygame.display.update()


# class Background(pygame.sprite.Sprite):
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location


#Drawing Snake
def draw_snake(gameWindow, black, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])


#Showing Scores on gameWindow
myfont=pygame.font.SysFont("arial", 35)
def show_text(text, color, x ,y):
    comment=myfont.render(text,True,color)
    text_rect = comment.get_rect(center=(screen_width//2, y))
    gameWindow.blit(comment,[x,y])


clock=pygame.time.Clock()
#welcome_page
def welcome():
    exit_game=False
    while not exit_game:
        bg=pygame.image.load('images/welcome.jpg')
        gameWindow.blit(bg,(0,40))
        show_text("Press SPACE to play game!",green,100,450)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(60)                


def game_loop():

    #Game_variables
    exit_game=False
    game_over=False
    fps=30
    score=0

    #snake_variables
    snake_x=30          #Snake's initial x co-ordinte
    snake_y=50          #Snake's initial y co-ordinte
    snake_size=10       #Snake's initial size
    velocity_x=0        #Snake's initial x velocity
    velocity_y=0        #Snake's initial y velocity
    velocity_init=5     ##Snake's velocity change

    snake_length=1
    snake_list=[]

    with open('highscore.txt', 'r') as f:
        highscore=f.read()
    #Drawing first food on gameWindow
    food_x = random.randint(20,screen_width-40)         #x-position of food
    food_y = random.randint(20,screen_height-40)        #y-position of food
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

    while not exit_game:
        if game_over==True:
            #writing new high score in 'highscore.txt' 
            with open("highscore.txt",'w') as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            bg2=pygame.image.load('images/bg2.jpg')
            gameWindow.blit(bg2,(0,0))
            #gameWindow.draw.text("hello world", midtop=(400, 0))
            show_text("Game over! Your score: "+str(score),red, 200,200)
            show_text("Press 'Enter' to play again",red, 200,300)
            
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        game_loop()

                    if event.key== pygame.K_q:
                        exit_game=True
                        

        else:

            for event in pygame.event.get():

                if event.type== pygame.QUIT:
                    exit_game=True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x= velocity_init
                        velocity_y= 0
                        
                    if event.key==pygame.K_LEFT:
                        velocity_x= -velocity_init
                        velocity_y= 0
                        
                    if event.key==pygame.K_UP:
                        velocity_x= 0
                        velocity_y= -velocity_init
                        
                    if event.key==pygame.K_DOWN:
                        velocity_x= 0
                        velocity_y= velocity_init

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y            
            
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=10
                snake_length+=10
                if score>int(highscore):
                    highscore = score

                #print("score=",score,highscore)
                food_x = random.randint(20,screen_width-40)
                food_y = random.randint(20,screen_height-40)

                
                
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            

            snake_list.append(head)
            if len(snake_list)>snake_length:
                del(snake_list[0])

            if head in snake_list[:-1]:
                game_over=True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
            
            

            gameWindow.fill(white)
            bg=pygame.image.load('images/bg6.jpg')
            gameWindow.blit(bg,(0,40))
            #BackGround = Background('bg6.jpg', [0,0])

            #gameWindow.fill([255, 255, 255])
            #gameWindow.blit(BackGround.image, BackGround.rect)
            show_text("Score="+str(score)+"  Highscore="+ str(highscore),red,5,5)
            draw_snake(gameWindow, black, snake_list, snake_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()

