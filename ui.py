import pygame as p
from config import *

class ennemy_healthbar(p.sprite.Sprite):
    def __init__(self,g,o):
        self.game = g
        self._layer = PLAYER_LAYER + 1 
        self.groups = self.game.all_sprites, self.game.ui
        p.sprite.Sprite.__init__(self,self.groups)

        self.owner = o
        self.width = 178
        self.height = 16
        self.image_spritesheet = spritesheet("images/ui/enemy_healthbar.png")
        self.image = self.image_spritesheet.get_sprite(0,0,self.width,self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.owner.rect.x + self.owner.width//2 - self.width//2
        self.rect.y = self.owner.rect.y - 30

    def update(self):
        self.rect.x = self.owner.rect.x + self.owner.width//2 - self.width//2
        self.rect.y = self.owner.rect.y - 30
        self.image = self.image_spritesheet.get_sprite(0, self.height*(3-self.owner.health), self.width, self.height)
        if self.owner.health <=0:
            self.kill()

class player_health_bar(p.sprite.Sprite):
    def __init__(self,g):
        self.game = g
        self._layer = PLAYER_LAYER + 1 
        self.groups = self.game.all_sprites, self.game.ui
        p.sprite.Sprite.__init__(self,self.groups)

        self.width = 500
        self.height = 36
        self.image_spritesheet = spritesheet("images/ui/player_healthbar.png")
        self.image = self.image_spritesheet.get_sprite(0,0,self.width,self.height)

        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = HEIGHT - 56
    
    def update(self):
        self.rect.x = 20
        self.rect.y = HEIGHT - 56
        self.image = self.image_spritesheet.get_sprite(0, self.height*(10-self.game.player.health), self.width, self.height)
        if self.game.player.health <=0:
            self.kill()


