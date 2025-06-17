import pygame
from pygame.transform import scale # This import is not strictly necessary as pygame.transform.scale is used directly

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')

#set framerate
clock = pygame.time.Clock()
FPS = 60


#define player action variables
Moving_Left = False
Moving_Right = False

# Define colors (added at 00:14 in the video)
BG = (144, 201, 120) # Example background color

# Define draw_bg function (added at 00:14 in the video)
def draw_bg():
    screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
    def __init__(self,char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = [] # FIX: Corrected capitalization here. This was the typo from the video! (1:39 in video)
        self.index = 0 # Added at 1:52 in video

        # Determine number of idle frames based on your screenshots
        num_idle_frames = 0
        if self.char_type == 'player':
            num_idle_frames = 4 # player/idle has 0.png, 1.png, 2.png, 3.png (4 frames)
        elif self.char_type == 'enemy':
            num_idle_frames = 1 # enemy/idle has only 0.png (1 frame)


        # Loop to load animation frames (added at 2:10 in video)
        # Using num_idle_frames to correctly load only existing images
        for i in range(num_idle_frames):
            img_path = f'img/{self.char_type}/idle/{i}.png' # Path to image
            try:
                img = pygame.image.load(img_path)
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                self.animation_list.append(img)
            except FileNotFoundError:
                print(f"Error: File '{img_path}' not found. Please ensure it exists and has the correct .png extension.")
                # This error means a specific image is missing or misnamed.
                # If this error still occurs after renaming 0.jpg and adjusting range,
                # then other image files might be missing or misnamed.
                # For now, we'll let it try to continue but be aware.
                pass # Continue trying to load other images even if one is missing

        # self.image and self.rect setup (Lines 41-45 in original code, 4:05 in video)
        # Ensure that animation_list is not empty before trying to access an index
        if self.animation_list:
            self.image = self.animation_list[self.index]
        else:
            print(f"Critical Error: No images loaded for {self.char_type} idle animation. Displaying a placeholder.")
            self.image = pygame.Surface((50, 50)) # Generic red square placeholder
            self.image.fill((255, 0, 0)) 
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, Moving_Left, Moving_Right):
        #Reset movement Variables
        dx = 0
        dy = 0
         
        #assign movement variables if moving left or right
        if Moving_Left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if Moving_Right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        
        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Soldier('player', 200,200,0.17, 5)
enemy = Soldier('enemy', 400,200,0.17, 5)

#Lets Run it
run = True
while run:

    clock.tick(FPS)
    # Clear screen and draw elements for the current frame
    draw_bg() # Draws background (24:45 in video)

    player.draw()
    enemy.draw()
    player.move(Moving_Left, Moving_Right)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        # Keyboard Presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Moving_Left = True
            elif event.key == pygame.K_d:
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