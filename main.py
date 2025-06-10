import pygame
from pygame.transform import scale # This is okay, though often transform is used as pygame.transform

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')



#define player action variables
Moving_Left = False
Moving_Right = False





class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale speed): # Removed the trailing comma from 'scale,'
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/player/idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale))) # Changed float() to int() as scale expects integer dimensions
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # This 'draw' method needs to be inside the Soldier class
    def draw(self):
        screen.blit(self.image, self.rect)


player = Soldier(200,200,0.2)


run = True
while run:
    # Drawing needs to happen before event handling and display update
    player.draw()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Keyboard Presses
        if event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Moving_Left = True
        if event.key == pygame.K_d:
                Moving_Right = True
                if event.key == pygame.K_ESCAPE:
                    run = False
             




        #Keyboard button Released
        if event.type  == pygame.KEYUP:
            if event.key == pygame.K_a:
                Moving_Left = False
        if event.key == pygame.K_d:
                Moving_Right = False




    pygame.display.update()

pygame.quit()

