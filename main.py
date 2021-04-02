#Setup starts
import pygame, sys
from SpriteLoader import *
from pygame.locals import *
from Cat import *
from Knight import *


pygame.init()
screen_info = pygame.display.Info()
size_x = 800
size_y = 600
screen = pygame.display.set_mode((size_x, size_y))
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
color = (230, 220, 190)
#SEtup end

#images
cat_images = []
man_images = {}

#cat images:
def get_images():
    cat_sheet = Spritesheet('runningcat.png')
    man_sheet = Spritesheet('knight.png')
    directions = ["n","e","w","s"]
    for i in range(4):
        for j in range(2):
            cat_images.append(cat_sheet.get_image(j * 512, i * 256, 512, 256))
            cat_images[-1] = pygame.transform.smoothscale(cat_images[-1], (180, 90))
          

    #Man
    for i in range(len(directions)):
        for j in range(8):
            man_images[directions[i] + str(j)] = man_sheet.get_image(j*69.9, i*90, 69.9, 90)

#main funcions
def main():
    #get images
    get_images()
    cat = Cat((-90, random.randint(50, height-50)), cat_images)
    player = Player((width//2, height//2), man_images)



    #exit screen
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            player.up()
        if keys[K_DOWN]:
            player.down()
        if keys[K_LEFT]:
            player.left()
        if keys[K_RIGHT]:
            player.right()
        player.update()

        #frame rate
        cat.update()
        screen.fill(color)
        cat.draw(screen)
        player.draw(screen)
        pygame.display.flip()

    

    



if __name__ == "__main__":
    main()