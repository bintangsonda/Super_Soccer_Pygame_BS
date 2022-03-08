import pygame
 
BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image= pygame.image.load("assets/ball2.png").convert_alpha()
        self.image=pygame.transform.scale(self.image,(width,height))
        self.velocity = [0,0]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.friction()
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def sticky(self, x,y):
        self.velocity[0] = 0
        self.velocity[1] = 0
        self.rect.x =x+25
        self.rect.y =y+50
    
    #shoot as arrow angle
    def shoot(self, angle):
        tempX = angle
        tempY = angle
        if tempX > 180:
            tempX = 180 - (tempX-180)
        if tempY > 270:
            tempY = 270 - (tempY-270)
        if tempY > 90 :
            tempY = 90 - (tempY-90)
        targetX = (tempX-90)/90
        targetY = (tempY)/90
        self.rect.x += 20
        self.velocity = [targetX * 15, targetY * 15]
    
    #speed of ball
    def friction(self):
        if self.velocity[0] > 0.1:
            self.velocity[0] -= 0.1
        elif self.velocity[0] < -0.1:
            self.velocity[0] += 0.1
        else:
            self.velocity[0] = 0
        
        if self.velocity[1] > 0.1:
            self.velocity[1] -= 0.1
        elif self.velocity[1] < -0.1:
            self.velocity[1] += 0.1
        else:
            self.velocity[1] = 0
