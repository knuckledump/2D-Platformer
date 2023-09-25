import pygame as p
import random
from config import *

    
class background(p.sprite.Sprite):
    def __init__(self,g,layer):
        self.game =g
        self.groups = self.game.backgrounds
        self._layer = layer
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.image = spritesheet("images/environment/background_"+str(layer)+".png").get_sprite(0,0,WIDTH,HEIGHT)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
        
class block(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self.groups = self.game.blocks,self.game.all_sprites
        self._layer = TERRAIN_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        pos_x = random.randint(7,10)
        self.image = spritesheet("images/environment/blocks.png").get_sprite(pos_x*TILESIZE,9*TILESIZE,TILESIZE,TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        self.mask = p.mask.from_surface(self.image)
    

class inside(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self.groups = self.game.insides,self.game.all_sprites
        self._layer = TERRAIN_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        decor_des = random.randint(0,500)
        if decor_des <100:
            self.image = spritesheet("images/environment/blocks.png").get_sprite(17*TILESIZE,9*TILESIZE,TILESIZE,TILESIZE)
        elif decor_des >100 and decor_des < 200:
            self.image = spritesheet("images/environment/blocks.png").get_sprite(6*TILESIZE,10*TILESIZE,TILESIZE,TILESIZE)
        elif decor_des > 200 and decor_des < 300:
            self.image = spritesheet("images/environment/blocks.png").get_sprite(7*TILESIZE,10*TILESIZE,TILESIZE,TILESIZE)
        else:
            self.image = spritesheet("images/environment/blocks.png").get_sprite(0*TILESIZE,9*TILESIZE,TILESIZE,TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE
        self.mask = p.mask.from_surface(self.image)
    

class plateform(p.sprite.Sprite):
    def __init__(self,g,x,y,t):
        self.game = g
        self._layer = TERRAIN_LAYER
        self.groups = self.game.plateforms, self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.type = t
        
        self.image = spritesheet("images/environment/blocks.png").get_sprite(7*TILESIZE,4*TILESIZE,TILESIZE,TILESIZE)
        if self.type == 'left':
            self.image = spritesheet("images/environment/blocks.png").get_sprite(5*TILESIZE,4*TILESIZE,TILESIZE,TILESIZE)
        elif self.type == 'right':
            self.image = spritesheet("images/environment/blocks.png").get_sprite(9*TILESIZE,4*TILESIZE,TILESIZE,TILESIZE)
        elif self.type == 'mid_right':
            self.image = spritesheet("images/environment/blocks.png").get_sprite(8*TILESIZE,4*TILESIZE,TILESIZE,TILESIZE)
        elif self.type == 'mid_left':
            self.image = spritesheet("images/environment/blocks.png").get_sprite(6*TILESIZE,4*TILESIZE,TILESIZE,TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        self.mask = p.mask.from_surface(self.image)
        
class decoration(p.sprite.Sprite):
    def __init__(self,g,x,y,t):
        self.game = g
        self._layer = TERRAIN_LAYER
        self.groups = self.game.decorations , self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.type = t
        if self.type == 'up':
            des = random.choice([(9,8,1,1),(9,7,1,1),(4,6,1,1),(5,6,1,1),(6,6,1,1),(0,4,1,1),(1,4,1,1),(4,5,1,1)])
        else:
            des = random.choice([(1,2,1,1),(1,3,1,1),(0,2,1,2),(2,2,1,3)])
        self.image = self.image = spritesheet("images/environment/blocks.png").get_sprite(des[0]*TILESIZE,des[1]*TILESIZE,des[2]*TILESIZE,des[3]*TILESIZE)     
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE

class bush(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self._layer = TERRAIN_LAYER
        self.groups = self.game.decorations , self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.image = spritesheet("images/environment/blocks.png").get_sprite(7*TILESIZE,5*TILESIZE,3*TILESIZE,2*TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x*TILESIZE,(y+1)*TILESIZE)

class big_bush(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self._layer = TERRAIN_LAYER
        self.groups = self.game.decorations , self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.image = spritesheet("images/environment/blocks.png").get_sprite(4*TILESIZE,7*TILESIZE,5*TILESIZE,2*TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x*TILESIZE,(y+1)*TILESIZE)

class tree(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self._layer = TERRAIN_LAYER
        self.groups = self.game.decorations , self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.image = spritesheet("images/environment/blocks.png").get_sprite(0*TILESIZE,5*TILESIZE,4*TILESIZE,4*TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x*TILESIZE,(y+1)*TILESIZE)

class big_tree(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self._layer = TERRAIN_LAYER
        self.groups = self.game.decorations , self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.image = spritesheet("images/environment/blocks.png").get_sprite(10*TILESIZE,0*TILESIZE,8*TILESIZE,9*TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x*TILESIZE,(y+1)*TILESIZE)

class rock(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self._layer = TERRAIN_LAYER
        self.groups = self.game.decorations , self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.image = spritesheet("images/environment/blocks.png").get_sprite(3*TILESIZE,3*TILESIZE,2*TILESIZE,2*TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x*TILESIZE,(y+1)*TILESIZE)
