import pygame
from pygame.transform import scale

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale ):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('O.png.jpg')
        self.image = pygame.transform.scale(img, (float(img.get_width() * scale), float(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

def draw(self):
    screen.blit(self.image, self.rect)


player = Soldier(200,200,0.9)
player2 = Soldier(400,200,0.9)



run = True
while run:



    player.draw()
    player2.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()