import pygame
import pygame.math
import math
import Game

class Player:
    def __init__(self, game: Game, pos: pygame.math.Vector2, size: pygame.math.Vector2):
        self.game = game
        self.life = True
        self.boost_on = False
        self.draw_center = False
        self.speed_y = 0
        self.speed_x = 0
        self.gavety = 0.01
        self.angle = 0
        self.rotateSpeed = 0
        self.posistion = pos
        self.size = size
        self.image_off = pygame.image.load("LunaLander/Images/space-ship-off.png")
        self.image_on = pygame.image.load("LunaLander/Images/space-ship-on.png")
        self.player = pygame.Rect(pos.x - (size.x/2), pos.y - (size.y/2), size.x, size.y)
    
    def startBoost(self):
        self.boost_on = True

    def stopBoost(self):
        self.boost_on = False

    def rotateRight(self):
        self.rotateSpeed = 1

    def rotateLeft(self):
        self.rotateSpeed = -1

    def stopRotate(self):
        self.rotateSpeed = 0

    def rotate(self):
        self.angle += self.rotateSpeed 
        if self.angle > 360:
            self.angle = self.angle - 360
        if self.angle < 0:
            self.angle = 360 - self.angle

    def draw(self):
        if self.boost_on:
            image = pygame.transform.scale(self.image_on, self.size)
        else:
            image = pygame.transform.scale(self.image_off, self.size)
        image = pygame.transform.rotate(image, self.angle)
        self.player = image.get_rect(center=self.player.center)
        self.game.screen.blit(image, self.player)

    def move(self):
        self.speed_y += self.gavety
        dlt_x = 0
        dlt_y = 0
        if self.boost_on:
            if self.speed_y < 0:
                dir = -1
            else:
                dir = 1
            F = self.gavety * 2.9
            dlt_y = (F * math.sin(math.radians(self.angle-90))) + self.gavety
            dlt_x = (F * math.cos(math.radians(self.angle-90))) * -1
            self.speed_y += dlt_y
            self.speed_x += dlt_x
        else:
            dlt_y = self.gavety
            self.speed_y += self.gavety
        print(" Speed", self.speed_x, self.speed_y, self.angle)
        self.posistion.y += self.speed_y
        if self.posistion.y <= 0:
            self.posistion.y = 0
        if self.posistion.y >= (self.game.screen.get_height()-38):
            self.game.game_over = True
            self.posistion.y = (self.game.screen.get_height()-38)
        self.posistion.x += self.speed_x
        if self.posistion.x < 0:
          self.posistion.x = self.game.screen.get_width() - self.posistion.x
        if self.posistion.x > self.game.screen.get_width():
            self.posistion.x = self.posistion.x - self.game.screen.get_width() 
        pos = self.posistion
        self.player = pygame.Rect(pos.x - (self.size.x/2), pos.y - (self.size.y/2), self.size.x, self.size.y)

    def loop(self):
        self.rotate()
        self.move()
        self.draw()
