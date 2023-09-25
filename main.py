import pygame as p
import sys
from sprites import *
from environment import *
from config import *


class game:
    
    def __init__(self):
        self.screen = p.display.set_mode((WIDTH,HEIGHT))
        p.mouse.set_visible(False)
        self.clock = p.time.Clock()
        self.running = True
        self.playing = False
    
    def create_map(self):
        for j in range(len(LVL1)):
            for i in range(len(LVL1[j])):
                if LVL1[j][i] == 'b':
                    block(self,i,j)
                    if LVL1[j-1][i] =='d':
                        decoration(self,i,j-1,'up')
                    if LVL1[j+1][i] == 'd' or LVL1[j+1][i] == 'i':
                        decoration(self,i,j+1,'down')
                        
                if LVL1[j][i] == "i":
                    inside(self,i,j)
                    
                if LVL1[j][i] == 'p':
                    if LVL1[j][i+1] == 'b' or LVL1[j][i+1] =='i':
                       if LVL1[j][i-1] == '.':
                           plateform(self,i,j,'left')
                       else:
                           plateform(self,i,j,'mid_left')
                    if LVL1[j][i-1]=='b' or LVL1[j][i-1] == 'i':
                        if LVL1[j][i+1] =='.':
                            plateform(self,i,j,'right')
                        else:
                            plateform(self,i,j,'mid_right')
                    if LVL1[j][i-1] == 'p' and LVL1[j][i+1] == '.':
                        plateform(self,i,j,'right')
                    if LVL1[j][i+1] == 'p' and LVL1[j][i-1] == '.':
                        plateform(self,i,j,'left')
                    if LVL1[j][i+1] == 'p' and LVL1[j][i-1] == 'p':
                        plateform(self,i,j,'mid')
                    
                if LVL1[j][i]=='1':
                    bush(self,i,j)
                if LVL1[j][i]=='2':
                    big_bush(self,i,j)
                if LVL1[j][i]=='3':
                    tree(self,i,j)
                if LVL1[j][i]=='4':
                    big_tree(self,i,j)
                if LVL1[j][i]=='5':
                    rock(self,i,j)
                
                if LVL1[j][i] == 'T':
                    turret(self,i*TILESIZE,j*TILESIZE+39)
                if LVL1[j][i] == 'B':
                    bug(self,i*TILESIZE, j*TILESIZE)
            
    def new(self):
        self.playing = True

        self.all_sprites = p.sprite.LayeredUpdates()
        self.blocks = p.sprite.LayeredUpdates()
        self.backgrounds = p.sprite.LayeredUpdates()
        self.decorations = p.sprite.LayeredUpdates()
        self.insides = p.sprite.LayeredUpdates()
        self.plateforms = p.sprite.LayeredUpdates() 
        self.ennemies = p.sprite.LayeredUpdates()
        self.bugs = p.sprite.LayeredUpdates()
        self.projectiles = p.sprite.LayeredUpdates()
        self.ui = p.sprite.LayeredUpdates()
        self.effects = []

        background(self,1)
        background(self,2)
        background(self,0)
        self.player = player(self,WIDTH//2,HEIGHT//2)
        self.create_map()
        
        
    def events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
        
    def update(self):
        self.all_sprites.update()

    def draw_cursor(self):
        mx , my = p.mouse.get_pos()
        self.screen.blit(cursor_img, (mx - 15, my - 15))
          
    def draw(self):
        self.screen.fill(BLACK)
        self.backgrounds.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.draw_cursor()

        for effect in self.effects:
            effect.update()
            
        self.clock.tick(FPS) 
        p.display.update()
        
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    

g = game()
g.new()

while g.running:
    g.main()

p.quit()
sys.exit()
