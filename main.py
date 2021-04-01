#Setup starts
import pygame, sys
from SpriteLoader import *
from pygame.locals import *
from Cat import *
pygame.init()
screen_info = pygame.display.Info()
size_x = 800
size_y = 600
screen = pygame.display.set_mode((size_x, size_y))

size = (width, height) = (screen_info.current_w, screen_info.current_h)

clock = pygame.time.Clock()
color = (230, 220, 190)
#SEtup end

#images
cat_images = []


#cat images:
def get_images():
    cat_sheet = Spritesheet('runningcat.png')
    for  i in range(4):
        for j in range(2):
            cat_images.append(cat_sheet.get_image(j * 512, i * 256, 512, 256))
            cat_images[-1] = pygame.transform.smoothscale(cat_images[-1], (180, 90))






#main funcions
def main():
    #get images
    get_images()
    cat = Cat((-90, random.randint(50, height-50)), cat_images)
    cat_image = cat_images[0]
    cat_rect = cat_image.get_rect()

    

    #exit screen
    while True:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit

        #frame rate
        cat.update('self')
        cat.draw(screen)
        screen.fill(color)
        
        pygame.display.flip()

    

    



if __name__ == "__main__":
    main()