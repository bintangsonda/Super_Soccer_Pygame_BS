import pygame
BLACK = (0,0,0)
TRANSPARENT = (255,255,255,1)

class Arrow(pygame.sprite.Sprite):
    #This class represents a arrow. It derives from the "Sprite" class in Pygame.
    curPos = 0

    def __init__(self, startPos):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.curPos = startPos
        self.image = pygame.image.load("assets/arrow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
    

    def appear(self,x,y):
        self.image = pygame.image.load("assets/arrow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect.x = x
        self.rect.y = y
    
    #set the rotation of arrow
    def aim(self):
        self.image=pygame.transform.rotate(self.image,self.curPos)
        self.curPos+=2
        if self.curPos >= 360:
            self.curPos=0
    
    def transparent(self):
        self.image.fill(TRANSPARENT)
        self.image.set_colorkey(TRANSPARENT)
        self.rect = self.image.get_rect()