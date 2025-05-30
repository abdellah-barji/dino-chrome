import pygame     # ka t3yt 3la l biblyotek dyal pygame
#import os
import random

pygame.init()   #initialisation pygame

secreen_hieght=600    #l3ard dyal l feneter
secreen_width=1100     #tol dyal l feneter
SCREEN=pygame.display.set_mode((secreen_width,secreen_hieght))  #hadi kat tsyb dik lwindow
pygame.display.set_caption('ahssan game hhhh')   #smiya dyal l fenetre

running=[ pygame.image.load(r"img\DinoRun1.png") , pygame.image.load(r"img\DinoRun2.png") ]
#hado bach ki afiche lina tsawr
#homa f list 7itach 2 tsawer # bach dir lwahm dyal dynasor ki t7rk
jumping=pygame.image.load(r"img\DinoJump.png")#tswira dyal ten9az
ducking=[pygame.image.load(r"img\DinoDuck1.png"),pygame.image.load(r"img\DinoDuck2.png")]
#les obstacles
smal_cactus=[pygame.image.load(r"img\SmallCactus1.png"),pygame.image.load(r"img\SmallCactus2.png"),pygame.image.load(r"img\SmallCactus3.png")] 
big_cactus= [pygame.image.load(r"img\LargeCactus1.png"),pygame.image.load(r"img\LargeCactus2.png"),pygame.image.load(r"img\LargeCactus3.png")]
bird=[pygame.image.load(r"img\Bird1.png"),pygame.image.load(r"img\Bird2.png")]
#idafat
cloud=pygame.image.load(r"img\Cloud.png")
background=pygame.image.load(r"img\Track.png")

class Dinosaur:
    x_pos=80
    y_pos=310
    y_pos_duck =340
    JUMP_VEL =8.5    #sor3a dyal l9afz wla tn9iza

    def __init__(self):  #cration d'un objet dinasor
        self.duck_img=ducking   #تخزين قائمة الصور الخاصة  (ducking)
        self.run_img=running
        self.jump_img=jumping

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index=0     # hiya li ra t5lih yb9a yban b7ala yjeri
        self.jump_vel=self.JUMP_VEL
        self.image=self.run_img[0]#radi ya5d tswira lwla
        self.dino_rect=self.image.get_rect()# ki 3ti l7odod dyal tswira
        self.dino_rect.x=self.x_pos #l7odod howa lposition d x
        self.dino_rect.y=self.y_pos  #l7odod howa lposition d y

    def update(self, userInput):  #kat update حالة الديناصور
        #userInput تحدد أي الأزرار مضغوطة من قبل اللاعب
        if self.dino_duck: #dino_duck تساوي True
            self.duck()   #t3yt 3la lfonction dyal hbt kayna lt7t
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index>=10:
            self.step_index=0
            """When step_index = 0 to 4, self.step_index // 5 will be 0, so self.image = self.run_img[0] (first image).
When step_index = 5, self.step_index // 5 will be 1, so self.image = self.run_img[1] (second image).
When step_index = 6 to 9, self.step_index // 5 will still be 1, so self.image = self.run_img[1] (second image)."""

        if userInput[pygame.K_UP] and not self.dino_jump: # howa maykonch deja mn9z
            self.dino_duck = False #ki w9f l7dra
            self.dino_run = False  #ki w9f jri
            self.dino_jump = True  #ki ne9z
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump  or userInput[pygame.K_DOWN]):# la ma knch mn9z wla me7ni radi yjri """kat 3ni treu"""
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image= self.duck_img[self.step_index//5]# b7al sor3a bach ki tbdlo tsawr dyal jri
        self.dino_rect=self.image.get_rect()#ki 3ti l7odod dyal tswira
        self.dino_rect.x=self.x_pos   #l7odod howa lposition d x
        self.dino_rect.y=self.y_pos_duck   #l7odod howa lposition d y
        self.step_index += 1

    def run(self):  # hadi hiya li ka t5lih ytmcha      
        self.image = self.run_img[self.step_index // 5]# b7al sor3a bach ki tbdlo tsawr dyal jri
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img #radi ya5d tswira 
        if self.dino_jump:     #dino_jump = True
            self.dino_rect.y -= self.jump_vel * 4  #هو سرعة القفز. في البداية
            self.jump_vel -= 0.8  #b7al ljadibiya kolma zadt zadt ljadibiya
        if self.jump_vel < - self.JUMP_VEL: #sor3a bach ki hbt
            self.dino_jump = False  
            self.jump_vel = self.JUMP_VEL
    
    def draw(self, SCREEN): #radi tprint la forme dyal dino 3la lwindow
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):  #تحديد خصائص السحابة (موقعها، الصورة، عرضها، ).
        self.x=secreen_width + random.randint(800,1000)# السحابة ستكون دائمًا بداية من الجهة اليمنى للشاشة (أبعد من الحافة اليمنى بمقدار عشوائي بين 800 و 1000 بيكسل).
        self.y= random.randint(50,100)
        self.image=cloud
        self.width=self.image.get_width()#.get_width(): fonction kat3awd taffiche dik tsrwira

    def update(self):  #تقوم بتحديث خصائص السحابة
        self.x -=game_speed#kolma tzadt sor3a dyal game speed katzad sor3a dyal s7aba
        if self.x < -self.width:# fach radi tmchi s7aba radi t3awd tsyb w7da 5ra
            self.x = secreen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self,SCREEN):
        SCREEN.blit(self.image,(self.x,self.y))


class Obstacl:
    def __init__(self,image , type) :
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect() #radi y3ti l7odod l tswira
        self.rect.x = secreen_width  # radi ytsayb chjra f limn dyal chacha

    def update(self):
        self.rect.x -= game_speed  #بطرح game_speed من self.rect.x، يتم تحريك العقبة باتجاه اليسار في كل إطار. وبالتالي، ستتحرك العقبة من اليمين إلى اليسار على الشاشة.
        if self.rect.x < -self.rect.width: #عندما تتحرك العقبة حتى تخرج من الشاشة بالكامل
            obstacles.pop() #ka tms7 bmera machi b7al s7ab

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect) # 3la hassab typ li radi ykon


class SmallCactus(Obstacl): # class wst class SmallCactus radi ta5d les fonction dyal obstacl
    def __init__(self, image): #image radi t5dha tal l5r
        self.type = random.randint(0, 2) 
        super().__init__(image, self.type)
#يستخدم super() لاستدعاء الدالة المُنشئة (__init__) للفئة الأم Obstacl وتمرير متغيرات image و self.type إليها.      
        self.rect.y = 325


class LargeCactus(Obstacl):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacl):
    def __init__(self, image):
        self.type = 0   # hadi bach radi tbda
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)   #bach yb9a ychange mn 0 o 1 
        self.index += 1
        


def main():
    # global ki 3ni anaho had les vaiable sta3malnahom da5il o bra l fonction
    global game_speed , x_pos_bg , y_pos_bg ,points , obstacles #variable globale
    #game_speed   128          x_pos_bg     200
    run=True  #dyal bach ykon fals ysd l fenetre
    clock= pygame.time.Clock() #يتيح لك تحديد معدل التحديث f l5r radi ndiroha 30 fps
    player=Dinosaur()
    CLOUD=Cloud()
    game_speed=14
    x_pos_bg=0
    y_pos_bg=380 
    points =0
    font = pygame.font.Font('freesansbold.ttf', 20)#تم تحديد الخط freesansbold.ttf مع الحجم 20.
    #هذا السطر يقوم بإنشاء خط الكتابة الذي سيستخدم لعرض النصوص في اللعبة.
    obstacles = []
    deth_count=0

    def score():
        global points, game_speed
        points += 1 # radi yb9a yzid f no9at(score)
        if points % 100 == 0: #kolma ywsl l 100 ou 200 ou 500...
            game_speed += 1 #radi tzad sor3a dyal lgame

        text = font.render("Points: " + str(points), True, (0, 0, 0)) #hada dyal scor li fjenb
        #font.render() يقوم بتحويل النص إلى صورة يمكن عرضها على الشاشة 
        #(0, 0, 0) هو اللون الأسود (RGB)
        #font.render(text, antialias, color)
        # ka t9sed jawda dyal keba true zwina false 5ayba

        textRect = text.get_rect() # bach n9ad l7odod
        textRect.center = (1000, 40) # lblasa dyal l7odod
        SCREEN.blit(text, textRect)  # kat afiche scor f jenb\
        
    def BackGround():
        global x_pos_bg, y_pos_bg
        image_width = background.get_width()
#نستخدم لضبط مكان ظهور الصورة الثانية بحيث تظهر مباشرة بعد الصورة الأولى. هذا يمنحك تأثير "الحركة المستمر
        SCREEN.blit(background, (x_pos_bg, y_pos_bg))
        #الصورة الأولى تظهر في المكان (x_pos_bg, y_pos_bg)
        SCREEN.blit(background, (image_width + x_pos_bg, y_pos_bg))#الصورة الثانية تظهر في المكان (image_width + x_pos_bg, y_pos_bg)
        #نضع الصورة الثانية بعد عرض الصورة الأولى
        if x_pos_bg <= -image_width: #mnin radi twli pos < mn imag radi t3awd print  
            SCREEN.blit(background, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0 #  إعادة تعيين x_pos_bg إلى 0 .لكي تبدأ الصورة الأولى من البداية
        x_pos_bg -= game_speed  

    while run: #hiya (while true)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:# إذا كان الحدث هو إغلاق النافذة
                run=False

        SCREEN.fill((255 , 255 , 255))# ملء الشاشة بلون أبيض
        userInput=pygame.key.get_pressed()# les touch li ki wrk 3lihom

        player.draw(SCREEN)  # رسم اللاعب على الشاشة
        player.update(userInput)  #kat t3yt 3la les fonction dyal lclasse li kat update

        if len(obstacles) == 0: #إذا كانت قائمة العقبات فارغة
            if random.randint(0, 2) == 0: # radom 5tart 0  
                obstacles.append(SmallCactus(smal_cactus))# radi t3yt 3la small
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(big_cactus))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(bird))

        for obstacle in obstacles: #bach tb9a t3awd
            obstacle.draw(SCREEN) # affiche lina obstacl
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect): #colliderectتتحقق إذا كان المستطيل الأول  يتداخل مع المستطيل الثاني
                pygame.draw.rect(SCREEN,(225,0,0),player.dino_rect)
                pygame.time.delay(2000) # تأخير لمدة 2 ثانية
                deth_count = deth_count+1
                menu(deth_count) # العودة إلى القائمة مع عدد الموتى

        BackGround()#3yt 3la ri9
        score() # عرض النقاط على الشاشة

        CLOUD.draw(SCREEN)       # # رسم السحابة على الشاشة
        CLOUD.update()            #kat t3yt 3la les fonction dyal lclasse
        #o kat t7rk s7abat


        clock.tick(30) # التحكم في سرعة اللعبة، هنا يعني أن اللعبة ستعمل بسرعة 30 إطارًا في الثانية
        pygame.display.update()# تحديث شاشة اللعبة
        # hadi dima kayna


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
            #يقوم هنا بالحصول على مستطيل يحتوي على خصائص النص (مثل الحجم والموقع) للنص
            scoreRect.center = (secreen_width // 2, secreen_hieght // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (secreen_width // 2, secreen_hieght // 2)
        #secreen_width // 2: يقوم بتحديد نصف عرض الشاشة.
        #secreen_hieght // 2 + 50: يقوم بتحديد نصف ارتفاع الشاشة ويضيف 50 بكسل للانتقال قليلاً إلى أسفل
        #SCREEN.blit(text, textRect)
        SCREEN.blit(running[0], (secreen_width // 2 - 20, secreen_hieght // 2 - 140))
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN: # ka t3ni la wrk 3la ay 7aja radi y3awd ykml
                main()

menu(deth_count=0)