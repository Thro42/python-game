import pygame
import pygame.math
import sys
from random import randint
import Player

#Farben
GRAY = (199, 184, 196)
xGRAY = (159, 163, 168)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Game:
    def __init__(self, breite: int, hoehe: int):
        self.game_over = False
        self.youWin = False 
        self.breite = breite
        self.hoehe = hoehe
        size = (breite, hoehe)
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.goundImage = pygame.image.load("LunaLander/Images/ground.png")
        self.spaceImage =  pygame.image.load("LunaLander/Images/stars.png")
        self.platformImage =  pygame.image.load("LunaLander/Images/platform.png")

        self.initPlayer()
        self.clock = pygame.time.Clock()
        self.endScale = 20
        self.platform = pygame.Rect(randint(20, breite-120), hoehe-15, 100, 15 )

    def HandleKeybord(self):
        # Tastatur befele verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:  # Taste wurde gedrückt
                if event.key == pygame.K_UP:
                    self.player.startBoost()
                if event.key == pygame.K_RIGHT:
                    self.player.rotateLeft()
                elif event.key == pygame.K_LEFT:
                    self.player.rotateRight()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.stopRotate()
                if event.key == pygame.K_UP:
                    self.player.stopBoost()

    def darawBackground(self):
        winRect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        goundImage = pygame.transform.scale(self.goundImage, (self.screen.get_width(), self.screen.get_height()))
        spaceImage = pygame.transform.scale(self.spaceImage, (self.screen.get_width(), self.screen.get_height()))
        platformImage = pygame.transform.scale(self.platformImage, (self.platform.width, self.platform.height ))
        self.screen.blit(spaceImage, winRect)
        self.screen.blit(goundImage, winRect)
        self.screen.blit(platformImage, self.platform)
        #pygame.draw.rect(self.screen,GRAY, self.platform,10)


    def initPlayer(self):
        # Init the Player
        p_pos = pygame.math.Vector2(self.screen.get_width()/2, self.screen.get_height()/2)
        p_size = pygame.math.Vector2(48, 96)
        self.player = Player.Player(self, p_pos, p_size)

    def showEnd(self):
        self.darawBackground()
        imgSize = pygame.math.Vector2(self.screen.get_width()/self.endScale, self.screen.get_height()/self.endScale)
        center = pygame.math.Vector2((self.screen.get_width()/2)-(imgSize.x/2), (self.screen.get_height()/2)-(imgSize.y/2))
        # print(imgSize)
        self.endScale -= 3
        if self.endScale <= 1:
            self.endScale = 1
        self.gameover = pygame.image.load("Images/game_over.png")
        self.gameover = pygame.transform.scale(self.gameover, imgSize)
        self.youwinImg = pygame.image.load("Images/youwin.png")
        self.youwinImg = pygame.transform.scale(self.youwinImg, imgSize)
        imgrec = pygame.Rect(center.x, center.y, imgSize.x, imgSize.y)
        if self.youWin:
            self.screen.blit(self.youwinImg, imgrec)
        else:
            self.screen.blit(self.gameover, imgrec)

    def checkLandet(self):
        platform = pygame.Rect(self.platform.x+15,self.platform.y,self.platform.width-30,self.platform.height)
        player = pygame.Rect(self.player.player.x,self.player.player.y,self.player.player.width,self.player.player.height-10)
        #pygame.draw.rect(self.screen,BLUE, platform,1)
        #pygame.draw.rect(self.screen,BLUE, player,1)
        if player.colliderect(platform):
            #pygame.draw.rect(self.screen,RED, platform,1)
            #pygame.draw.rect(self.screen,RED, player,1)
            angle = abs(self.player.angle)
            if angle >= 360:
                angle = 0
            if angle > 180:
                360 - angle
            print("Landing",self.player.speed_y,abs(self.player.speed_x),angle)
            if self.player.speed_y <= 1.1 and abs(self.player.speed_x) <1 and angle < 10:
                self.game_over = True
                self.youWin = True


    def loop(self):
        # -------- Main Program Loop -----------
        while not self.game_over:
            # --- Main event loop
            self.HandleKeybord()
            # self.screen.fill(GRAY)
            self.darawBackground()
            self.player.loop()
            self.checkLandet()
            pygame.display.update()
            self.clock.tick(60)
        print(self.player.speed_y)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Taste wurde gedrückt
                    if event.key == pygame.K_q:
                        sys.exit()
            self.showEnd()
            pygame.display.update()
            self.clock.tick(60)

