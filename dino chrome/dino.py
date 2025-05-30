import pygame     
import random

pygame.init()  

secreen_hieght=600    
secreen_width=1100     
SCREEN=pygame.display.set_mode((secreen_width,secreen_hieght))  
pygame.display.set_caption('ahssan game hhhh')  

running=[ pygame.image.load(r"img\DinoRun1.png") , pygame.image.load(r"img\DinoRun2.png") ]
jumping=pygame.image.load(r"img\DinoJump.png")
ducking=[pygame.image.load(r"img\DinoDuck1.png"),pygame.image.load(r"img\DinoDuck2.png")]
#les obstacles
smal_cactus=[pygame.image.load(r"img\SmallCactus1.png"),pygame.image.load(r"img\SmallCactus2.png"),pygame.image.load(r"img\SmallCactus3.png")] 
big_cactus= [pygame.image.load(r"img\LargeCactus1.png"),pygame.image.load(r"img\LargeCactus2.png"),pygame.image.load(r"img\LargeCactus3.png")]
bird=[pygame.image.load(r"img\Bird1.png"),pygame.image.load(r"img\Bird2.png")]
cloud=pygame.image.load(r"img\Cloud.png")
background=pygame.image.load(r"img\Track.png")

class Dinosaur:
    x_pos=80
    y_pos=310
    y_pos_duck =340
    JUMP_VEL =8.5  

    def __init__(self):  
        self.duck_img=ducking   
        self.run_img=running
        self.jump_img=jumping

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index=0    
        self.jump_vel=self.JUMP_VEL
        self.image=self.run_img[0]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.x_pos 
        self.dino_rect.y=self.y_pos  

    def update(self, userInput): 
        if self.dino_duck: 
            self.duck()   
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index>=10:
            self.step_index=0

        if userInput[pygame.K_UP] and not self.dino_jump: 
            self.dino_duck = False 
            self.dino_run = False  
            self.dino_jump = True  
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump  or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image= self.duck_img[self.step_index//5]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.x_pos  
        self.dino_rect.y=self.y_pos_duck   
        self.step_index += 1

    def run(self):       
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img 
        if self.dino_jump:     
            self.dino_rect.y -= self.jump_vel * 4  
            self.jump_vel -= 0.8  
        if self.jump_vel < - self.JUMP_VEL: 
            self.dino_jump = False  
            self.jump_vel = self.JUMP_VEL
    
    def draw(self, SCREEN): 
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):  
        self.x=secreen_width + random.randint(800,1000)
        self.y= random.randint(50,100)
        self.image=cloud
        self.width=self.image.get_width()

    def update(self):  
        self.x -=game_speed
        if self.x < -self.width:
            self.x = secreen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self,SCREEN):
        SCREEN.blit(self.image,(self.x,self.y))


class Obstacl:
    def __init__(self,image , type) :
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() 
        self.rect.x = secreen_width 

    def update(self):
        self.rect.x -= game_speed  
        if self.rect.x < -self.rect.width: 
            obstacles.pop() 

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect) 


class SmallCactus(Obstacl): 
    def __init__(self, image): 
        self.type = random.randint(0, 2) 
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacl):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacl):
    def __init__(self, image):
        self.type = 0   
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)  
        self.index += 1
        


def main():
    global game_speed , x_pos_bg , y_pos_bg ,points , obstacles 
    run=True  
    clock= pygame.time.Clock() 
    player=Dinosaur()
    CLOUD=Cloud()
    game_speed=14
    x_pos_bg=0
    y_pos_bg=380 
    points =0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    deth_count=0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0: 
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0)) 
      
        textRect = text.get_rect() 
        textRect.center = (1000, 40) 
        SCREEN.blit(text, textRect)  
        
    def BackGround():
        global x_pos_bg, y_pos_bg
        image_width = background.get_width()
        SCREEN.blit(background, (x_pos_bg, y_pos_bg))
        SCREEN.blit(background, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(background, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0 
        x_pos_bg -= game_speed  

    while run: #hiya (while true)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        SCREEN.fill((255 , 255 , 255))
        userInput=pygame.key.get_pressed()

        player.draw(SCREEN) 
        player.update(userInput) 

        if len(obstacles) == 0: 
            if random.randint(0, 2) == 0: 
                obstacles.append(SmallCactus(smal_cactus))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(big_cactus))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(bird))

        for obstacle in obstacles: 
            obstacle.draw(SCREEN) 
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.draw.rect(SCREEN,(225,0,0),player.dino_rect)
                pygame.time.delay(2000)
                deth_count = deth_count+1
                menu(deth_count) 

        BackGround()
        score() 

        CLOUD.draw(SCREEN)      
        CLOUD.update()            


        clock.tick(30) 
        pygame.display.update()


def menu(deth_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if deth_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif deth_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect() 
            scoreRect.center = (secreen_width // 2, secreen_hieght // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (secreen_width // 2, secreen_hieght // 2)
      
        SCREEN.blit(running[0], (secreen_width // 2 - 20, secreen_hieght // 2 - 140))
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()

menu(deth_count=0)
