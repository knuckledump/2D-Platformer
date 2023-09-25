import pygame as p
from config import *
from animator import *
from ui import *
from particle_system import *
import math


class player(p.sprite.Sprite):
    def __init__(self,g,x,y):
        
        self.game = g
        self.groups = self.game.all_sprites
        self._layer = PLAYER_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 64
        self.height = 77
        self.animator = animator('player',self,(5,4,0,4))
        self.image =  self.animator.right_idle_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.animation_loop = 0
        self.facing = 'right'
        self.x_speed = 0
    
        self.can_go_left = True
        self.can_go_right = True
        
        self.is_airbound = True
        
        self.jump_timer = 0

        self.attack_timer = ATTACK_TIMER_CD

        self.health = 10
        self.healthbar = player_health_bar(self.game)

        self.gun = player_gun(self.game, self)
    
    def update(self):
        
        self.rotate_gun()
        self.check_if_dead()        
        self.check_if_airbound()
        self.gravity()
        self.collision()
        self.keys()
        self.mouvement()
        self.jump()
        self.animate()
        self.reset_mouvement_permission()
        self.attack_timer_tick()
        self.x_speed = 0
        
    def keys(self):
        
        keys = p.key.get_pressed()
        if keys[p.K_d] and self.can_go_right:
            self.x_speed = PLAYER_SPEED
            self.facing = 'right'
        if keys[p.K_q] and self.can_go_left:
            self.x_speed = -PLAYER_SPEED
            self.facing = 'left'
        
        if keys[p.K_z] and not self.is_airbound and self.jump_timer <=0:
            self.jump_timer = 5
        
        if keys[p.K_SPACE] and self.attack_timer >= ATTACK_TIMER_CD:
            mouse_x,mouse_y = p.mouse.get_pos()
            projectile(self.game,self,(mouse_x,mouse_y))
            self.attack_timer = 0
            
    def mouvement(self):
        
        self.rect.x += self.x_speed
        for item in self.game.all_sprites:
            item.rect.x -= self.x_speed
    
    def animate(self):
        if self.x_speed ==0:
            if self.facing =='right':
                self.animator.right_idle_animation()
            elif self.facing =='left':
                self.animator.left_idle_animation()
        else:
            if self.facing =='right':
                self.animator.right_run_animation()
            elif self.facing =='left':
                self.animator.left_run_animation()
        
        if self.is_airbound and self.jump_timer<0:
            if self.facing =='right':
                self.animator.right_fall_animation()
            elif self.facing =='left':
                self.animator.left_fall_animation()
        
    
    def collision(self):
        wall_hits = p.sprite.spritecollide(self, self.game.insides, False)
        if wall_hits:
            for hit in wall_hits:
                if self.rect.x > hit.rect.x:
                    self.can_go_left = False
                    if self.x_speed < 0:
                        self.x_speed = 0
                else:
                    self.can_go_right = False
                    if self.x_speed > 0:
                        self.x_speed = 0

        projectile_hits = p.sprite.spritecollide(self, self.game.projectiles, False)
        if projectile_hits:
            if projectile_hits[0].owner != self:
                self.health -= 1
                projectile_hits[0].kill()

        ennemy_hits = p.sprite.spritecollide(self, self.game.bugs, False)
        if ennemy_hits:
            if ennemy_hits[0].attack_cd >=5:
                self.health -= 1
                self.jump_timer = 10
                ennemy_hits[0].attack_cd = 0
                
    def gravity(self):
        if self.is_airbound: 
            for item in self.game.all_sprites:
                if item != self.game.player:
                    item.rect.y -= 10
            
    def reset_mouvement_permission(self):
        self.can_go_left = True
        self.can_go_right = True
    
    def check_if_airbound(self):
        block_hits = p.sprite.spritecollide(self, self.game.blocks, False)
        plateform_hits = p.sprite.spritecollide(self, self.game.plateforms, False)
        
        if block_hits and self.rect.y < block_hits[0].rect.y - self.height //2:
            self.is_airbound = False
        else:
            if plateform_hits and self.rect.y < plateform_hits[0].rect.y - self.height // 2:
                self.is_airbound = False
            else:
                self.is_airbound = True
        
    def jump(self):
        if self.jump_timer > 0:
            for item in self.game.all_sprites:
                if item != self.game.player:
                    item.rect.y += 25
            self.jump_timer -= 0.4

    def attack_timer_tick(self):
        if self.attack_timer < ATTACK_TIMER_CD:
            self.attack_timer += ATTACK_TIMER_TICK

    def check_if_dead(self):
        if self.health <= 0:
            self.kill()
            self.game.playing = False

    def rotate_gun(self):
        self.gun.kill()
        self.gun = player_gun(self.game,self)
        
        
                                       
class turret(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self._layer = PLAYER_LAYER
        self.groups = self.game.ennemies, self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.height = 25
        self.width = 88
        self.image = spritesheet("images/characters/turret/turret.png").get_sprite(0,75,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

        self.activated = False
        self.attack_timer = TURRET_ATTACK_TIMER_CD

        self.barrel = turret_barrel(self.game,self)

        self.health = 3
        self.healthbar = ennemy_healthbar(self.game,self)

    def update(self):
        self.rotate_barrel()
        self.check_if_dead()
        self.serach_for_player()
        self.attack_timer_tick()
        if self.activated and self.attack_timer >= TURRET_ATTACK_TIMER_CD:
            self.attack()
        
    def serach_for_player(self):
        if self.rect.x - TURRET_DECTECTION_RADIUS <= self.game.player.rect.x <= self.rect.x + TURRET_DECTECTION_RADIUS:
            if self.rect.y - TURRET_DECTECTION_RADIUS <= self.game.player.rect.y <= self.rect.y + TURRET_DECTECTION_RADIUS:
                self.activated = True
            else:
                self.activated = False
        else:
            self.activated = False

    def attack(self):
        turret_projectile(self.game,self, (self.game.player.rect.x, self.game.player.rect.y))
        self.attack_timer = 0

    def attack_timer_tick(self):
        if self.attack_timer < TURRET_ATTACK_TIMER_CD:
            self.attack_timer += TURRET_ATTACK_TIMER_TICK
    
    def check_if_dead(self):
        if self.health <=0:
            self.healthbar.kill()
            self.barrel.kill()
            self.kill()
    
    def rotate_barrel(self):
        self.barrel.kill()
        self.barrel = turret_barrel(self.game,self)


class turret_barrel(p.sprite.Sprite):
    def __init__(self,g,o):
        self.owner = o
        self.game = g
        self.groups = self.game.all_sprites
        self._layer = PLAYER_LAYER + 1
        p.sprite.Sprite.__init__(self,self.groups)

        self.width = 50
        self.height = 12
        self.image = spritesheet("images/characters/turret/barrel.png").get_sprite(49,44,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.owner.rect.x + self.owner.width//2
        self.rect.y = self.owner.rect.y - 10

        self.angle = math.atan((self.game.player.rect.y - self.rect.y)/(self.game.player.rect.x - self.rect.x))
        if self.rect.x > self.game.player.rect.x:
            self.angle += math.pi
        elif self.rect.y > self.game.player.rect.y:
            self.angle += 2*math.pi

        self.image = p.transform.rotate(self.image, -math.degrees(self.angle))

        self.rect.x = self.owner.rect.x + self.owner.width//2
        self.rect.y = self.owner.rect.y - 10
    


class projectile(p.sprite.Sprite):
    def __init__(self,g,o,target):
        self.game = g
        self.groups = self.game.projectiles, self.game.all_sprites
        self._layer = PLAYER_LAYER
        p.sprite.Sprite.__init__(self,self.groups)

        self.width = 24
        self.height = 18
        self.image = spritesheet("images/entities/bullet.png").get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()

        self.owner = o
        self.rect.x = self.owner.rect.x + self.owner.width//2
        self.rect.y = self.owner.rect.y + self.owner.height//2

        self.target_x = target[0]
        self.target_y = target[1]

        self.angle = math.atan((self.target_y - self.rect.y)/(self.target_x - self.rect.x))
        if self.rect.x > self.target_x:
            self.angle += math.pi
        elif self.rect.y > self.target_y:
            self.angle += 2*math.pi

        self.image = p.transform.rotate(self.image, -math.degrees(self.angle))

    def update(self): 
        self.mouvement()
        self.check_if_outside()
        self.collide()
        
    def mouvement(self):
        self.rect.x += PROJECTILE_SPEED * math.cos(self.angle)
        self.rect.y += PROJECTILE_SPEED * math.sin(self.angle)

    def check_if_outside(self):
        if self.rect.x > WIDTH +50 or self.rect.x < -50 or self.rect.y < -50 or self.rect.y >HEIGHT +50:
            self.kill()

    def collide(self):
        hits = p.sprite.spritecollide(self, self.game.ennemies, False)
        if hits:
            if hits[0] != self.owner:
                hits[0].health -= 1 
                self.kill()
                particle(self.game, self.rect.x + self.width//2 , self.rect.y + self.height//2)

class turret_projectile(projectile):
    def __init__(self,g,o,target):
        projectile.__init__(self,g,o,target)
        self.image = spritesheet("images/entities/turret_bullet.png").get_sprite(0,0,self.width,self.height)
        self.image = p.transform.rotate(self.image, -math.degrees(self.angle))

        
class player_gun(p.sprite.Sprite):
    def __init__(self,g,o):
        self.game = g
        self._layer = PLAYER_LAYER +1
        self.groups = self.game.all_sprites 
        p.sprite.Sprite.__init__(self,self.groups)

        self.owner = o 

        self.width = 50
        self.height = 20
        self.image = spritesheet("images/entities/player_gun.png").get_sprite(0,0,self.width,self.height)         
        self.rect = self.image.get_rect()
        self.rect.x = self.owner.rect.x 
        self.rect.y = self.owner.rect.y + self.owner.height//2

        mx, my = p.mouse.get_pos()
        if mx != self.rect.x :
            self.angle = math.atan((my - self.rect.y)/(mx - self.rect.x))
        else:
            self.angle = 0
            
        if self.rect.x > mx:
            self.angle += math.pi
        elif self.rect.y > my:
            self.angle += 2*math.pi

        self.image = p.transform.rotate(self.image, -math.degrees(self.angle))

class bug(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self._layer = PLAYER_LAYER 
        self.groups = self.game.all_sprites, self.game.ennemies, self.game.bugs
        p.sprite.Sprite.__init__(self,self.groups)

        self.width = 64
        self.height = 77
        self.animator = animator('bug',self,(4,4,0,0))
        self.image =  self.animator.right_idle_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  

        self.animation_loop = 0
        self.facing = "right"
        self.can_go_left = True
        self.can_go_right = True

        self.x_speed = 0
        self.activated = False
        self.health = 3
        self.healthbar = ennemy_healthbar(self.game,self)

        self.attack_cd = 5

    def update(self):
        self.mouvement()
        self.serach_for_player()

        if self.activated:
            self.collision()
            self.mouvement()
        else:
            self.x_speed = 0

        self.animate()
        self.reset_mouvement_permission()
        self.check_if_dead()
        self.attack_timer()

        self.rect.x += self.x_speed

    def serach_for_player(self):
        if self.rect.x - BUG_DECTECTION_RADIUS <= self.game.player.rect.x <= self.rect.x + BUG_DECTECTION_RADIUS:
            self.activated = True
        else:
            self.activated = False

    def mouvement(self):
        if self.rect.x > self.game.player.rect.x and self.can_go_left and self.rect.x - self.game.player.rect.x > BUG_SPEED:
            self.x_speed = -BUG_SPEED
            self.facing = 'left'
        elif self.rect.x < self.game.player.rect.x and self.can_go_right and self.game.player.rect.x - self.rect.x > BUG_SPEED:
            self.x_speed = BUG_SPEED
            self.facing = 'right'
        else:
            self.x_speed = 0

    def animate(self):
        if self.x_speed ==0:
            if self.facing =='right':
                self.animator.right_idle_animation()
            elif self.facing =='left':
                self.animator.left_idle_animation()
        else:
            if self.facing =='right':
                self.animator.right_run_animation()
            elif self.facing =='left':
                self.animator.left_run_animation()

    def collision(self):
        wall_hits = p.sprite.spritecollide(self, self.game.insides, False)
        if wall_hits:
            for hit in wall_hits:
                if self.rect.x > hit.rect.x:
                    self.can_go_left = False
                    if self.x_speed < 0:
                        self.x_speed = 0
                else:
                    self.can_go_right = False
                    if self.x_speed > 0:
                        self.x_speed = 0

    def reset_mouvement_permission(self):
        self.can_go_left = True
        self.can_go_right = True

    def check_if_dead(self):
        if self.health <=0:
            self.kill()

    def attack_timer(self):
        if self.attack_cd <= 5:
            self.attack_cd += 0.1
        
    


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            