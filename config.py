import pygame as p

class spritesheet:
    def __init__(self,file):
        self.sheet = p.image.load(file)
        
    def get_sprite(self,x,y,width,height):
        sprite = p.Surface([width,height])
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey((0,0,0))
        return(sprite)
    
    def get_sprite_inv(self,x,y,width,height):
        copy = self.sheet.copy()
        sprite = p.Surface([width,height])
        sprite.blit(p.transform.flip(copy,True,False),(0,0),(x,y,width,height))
        sprite.set_colorkey((0,0,0))
        return(sprite)



WIDTH = 1600    #25 TILE
HEIGHT = 1024   #16 TILE
FPS = 60
TILESIZE = 64

BLACK = (0,0,0)
WHITE = (255,255,255)
cursor_img = spritesheet("images/ui/cursor.png").get_sprite(0,0,30,30)

TERRAIN_LAYER = 4
PLAYER_LAYER = 5

PLAYER_SPEED = 8
PROJECTILE_SPEED = 10

ATTACK_TIMER_CD = 5
ATTACK_TIMER_TICK = 0.2

TURRET_ATTACK_TIMER_CD = 8
TURRET_ATTACK_TIMER_TICK = 0.2
TURRET_DECTECTION_RADIUS = 600

BUG_SPEED = 5
BUG_DECTECTION_RADIUS = 300


LVL1 = [
'......................................................' ,
'......................................................' ,
'.........2.d.....3.d.....1...4....ddd..dd.1...........' ,
'......pppbbbbppbbbbbbbbppbbbbbbbbbbbbbbbbbbbpp..dd....' ,
'.........dd.......d.........ddd.........dd....pbbbp...' ,
'..1.dd..................................T..5...d......' ,
'bbbbbbpp...............................ppbbbbbp.......' ,
'iiiiii.............................dd....d.dd.........' ,
'iiiiii...........................pbbbbpp..............' , 
'iiiiiip..................T.2......d...................' ,
'iiiiiid...4.ddd.......ppbbbbbbpp......................' ,
'iiiiiibbbbbbbbbbbpp.....d..dd.........................' ,
'iiiiiiiiiiiiiiiii.....................................' ,
'iiiiiiiiiiiiiiiii...ddd.....dddd..ddd.dd..dd...4......' ,
'iiiiiiiiiiiiiiiiibbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb' , 
'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii' ,
'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii' ,
'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii' ,
'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii' ,
'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii' ,
'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii' ,
'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii' , 
]
