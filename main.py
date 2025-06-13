import pygame
from pygame.transform import scale

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

#define player action variables
Moving_Left = False
Moving_Right = False

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        img = pygame.image.load('img/player/idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, Moving_Left, Moving_Right):
        #Reset movement Variables
        dx = 0
        dy = 0
         
        #assign movement variables if moving left or right
        if Moving_Left:
            dx = -self.speed
        if Moving_Right:
            dx = self.speed
        
        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(self.image, self.rect)


player = Soldier(200,200,0.2, 5)

run = True
while run:
    # Clear screen and draw elements for the current frame
    # A background fill or image load would typically go here
    screen.fill((0, 0, 0)) # Example: fill screen with black
    player.draw()
    player.move(Moving_Left, Moving_Right)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Keyboard Presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Moving_Left = True
            elif event.key == pygame.K_d: # Use elif for exclusive key presses if applicable
                Moving_Right = True
            elif event.key == pygame.K_ESCAPE: # This should be an independent check
                run = False

        # Keyboard button Released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Moving_Left = False
            elif event.key == pygame.K_d: # Corrected indentation for K_d
                Moving_Right = False

    pygame.display.update()

pygame.quit()