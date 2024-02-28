import pygame as pg
import sys
import settings

class Game:
    def __init__(self):
        pg.init()
        
    def new_game(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == self.global_trigger:
                self.global_trigger = True
            

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

            