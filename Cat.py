import pygame, random, turtle
turtlif = input("Do you want to have a pointing system (It will be very messy)Y or N:")
if turtlif.upper == 'Y':
    points = 0
    point = turtle.Turtle()
    point.penup()
    point.goto(0,30)


x = int(input("What do you want the game level to be?(5 to 10) :"))
class Cat(pygame.sprite.Sprite):
    def __init__(self, pos, images):
        super().__init__()
        self.images = images
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = [x, 0]
        
    def update(self):
        frame = pygame.time.get_ticks() // 60 % 8
        self.image = self.images[frame]
        self.rect.move_ip(self.speed)
        if self.rect.left > pygame.display.Info().current_w:
            self.rect.right = 0
            self.rect.centery = random.randint(50, pygame.display.Info().current_h- 50)
            
            
            if turtlif.upper == 'Y':
                global points
                points+= 1
                point.clear()
                point.write("Points: {}".format(points), align="center", font=("Courier", 24, "normal"))

    def draw(self, screen):
        screen.blit(self.image, self.rect)