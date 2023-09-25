import pygame as p
import math
from config import *    
    
class animator:
    def __init__(self,location,owner,n):
        
        self.owner = owner
        self.numbers = n  #idle/run/attack/fall
        self.tick = 0.2
        
        self.right_idle_list = []
        self.left_idle_list = []
        self.right_run_list = []
        self.left_run_list = []
        self.right_attack_list = []
        self.left_attack_list = []
        self.right_fall_list = []
        self.left_fall_list = []
        
        if self.numbers[1]!=0:
            self.run_spritesheet = spritesheet("images/characters/"+ location + "/run.png")
            for i in range(0,self.numbers[1]):
                self.right_run_list.append(self.run_spritesheet.get_sprite(i*self.owner.width,0,self.owner.width,self.owner.height))
                self.left_run_list.append(self.run_spritesheet.get_sprite_inv(i*self.owner.width,0,self.owner.width,self.owner.height))
        
        if self.numbers[2] != 0:
            self.attack_spritesheet = spritesheet("images/characters/"+ location + "/attack.png")
            for i in range(0,self.numbers[2]):
                self.right_attack_list.append(self.attack_spritesheet.get_sprite(i*self.owner.width,0,self.owner.width,self.owner.height))
                self.left_attack_list.append(self.attack_spritesheet.get_sprite_inv(i*self.owner.width,0,self.owner.width,self.owner.height))
        
        if self.numbers[0]!=0:
            self.idle_spritesheet = spritesheet("images/characters/"+ location + "/idle.png")
            for i in range(0,self.numbers[0]):
                self.right_idle_list.append(self.idle_spritesheet.get_sprite(i*self.owner.width,0,self.owner.width,self.owner.height))  
                self.left_idle_list.append(self.idle_spritesheet.get_sprite_inv(i*self.owner.width,0,self.owner.width,self.owner.height))
        
        if self.numbers[3]!=0:
            self.fall_spritesheet = spritesheet("images/characters/"+ location + "/fall.png")
            for i in range(0,self.numbers[3]):
                self.right_fall_list.append(self.fall_spritesheet.get_sprite(i*self.owner.width,0,self.owner.width,self.owner.height))
                self.left_fall_list.append(self.fall_spritesheet.get_sprite_inv(i*self.owner.width,0,self.owner.width,self.owner.height))
        
        
        
     
        
        
        
            
        
    def right_run_animation(self):
        
        if self.owner.animation_loop > self.numbers[1]:
            self.owner.animation_loop = 0
        self.owner.image = self.right_run_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += self.tick
        
    def left_run_animation(self):
        
        if self.owner.animation_loop > self.numbers[1]:
            self.owner.animation_loop = 0
        self.owner.image = self.left_run_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += self.tick
    
    def right_idle_animation(self):
        
        if self.owner.animation_loop > self.numbers[0]:
            self.owner.animation_loop = 0
        self.owner.image = self.right_idle_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += self.tick
        
    def left_idle_animation(self):
        
        if self.owner.animation_loop > self.numbers[0]:
            self.owner.animation_loop = 0
        self.owner.image = self.left_idle_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += self.tick
    
    def left_attack_animation(self):
        
        if self.owner.animation_loop > self.numbers[2]:
            self.owner.animation_loop = 0
        self.owner.image = self.left_attack_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += self.tick
        
    
    def right_attack_animation(self):
        
        if self.owner.animation_loop > self.numbers[2]:
            self.owner.animation_loop = 0
        self.owner.image = self.right_attack_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += self.tick
        
    def right_fall_animation(self):
        
        if self.owner.animation_loop > self.numbers[3]:
            self.owner.animation_loop = 0
        self.owner.image = self.right_fall_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += self.tick        
        
    def left_fall_animation(self):
        
        if self.owner.animation_loop > self.numbers[3]:
            self.owner.animation_loop = 0
        self.owner.image = self.left_fall_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += self.tick  
        
    