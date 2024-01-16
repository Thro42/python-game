#game.py
import pygame
import sys
import math

class Game:
    def __init__(self, sceenwith: int):
        self.sceenWith = sceenwith
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    #def loop(self):
