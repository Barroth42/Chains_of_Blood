#! /usr/bin/python

import pygame
import time
import random
from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

gameDisplay = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption('Chains of Blood')

clock = pygame.time.Clock()

block_size = 20
FPS = 15

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 100)

def game_credit():

    credit = True

    while credit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
				raise SystemExit, "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_intro()
                if event.key == pygame.K_q:
                    raise SystemExit, "QUIT"
   
        gameDisplay.fill(black)
        message_to_screen("Chains of Blood",
                          red,
                          -150,
                          "large")

        message_to_screen("Created by Cory Morales, Andrew Lee, Brain Kidd, and Jorge Benavides",
                          red,
                          -50)
                          
        message_to_screen("Press q to quit.",
                          red,
                          -20)
                          
        message_to_screen("Press r to return to the main menu.",
                          red,
                          10)                
    
        pygame.display.update()
        clock.tick(15)

def game_story():

    story = True
    while story:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
				raise SystemExit, "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_intro()
                if event.key == pygame.K_q:
                    raise SystemExit, "QUIT"
   
        gameDisplay.fill(black)
        message_to_screen("Chains of Blood",
                          red,
                          -150,
                          "large")

        message_to_screen('a /n b',
                          red,
                          -50)
                          
        message_to_screen("Press q to quit.",
                          red,
                          -20)
                          
        message_to_screen("Press r to return to the main menu.",
                          red,
                          10)                
    
        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit, "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    intro = False
                elif event.key == pygame.K_s:
					game_story()    
                elif event.key == pygame.K_c:
					game_credit()
                elif event.key == pygame.K_q:
                    raise SystemExit, "QUIT"
   
        gameDisplay.fill(black)
        message_to_screen("Chains of Blood",
                          red,
                          -150,
                          "large")

        message_to_screen("Press p to play.",
                          red,
                          -50)
        
        message_to_screen("Press s for story.",
                          red,
                          -20)                  
                          
        message_to_screen("Press q to quit.",
                          red,
                          10)
                          
        message_to_screen("Press c to veiw credits.",
                          red,
                          40)                
    
        pygame.display.update()
        clock.tick(15)
               
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (HALF_WIDTH), (HALF_HEIGHT)+y_displace
    gameDisplay.blit(textSurf, textRect)

game_intro()

def main():
    global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()

    up = down = left = right = running = False
    bg = Surface((32,32))
    bg.convert()
    bg.fill(Color("#000000"))
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []

    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P                              EEP",
        "P                                          P                         PPPPP  P",
        "P                                          P        PPPPPP                  P",
        "P                    PPPPPPPPPPP           P                                P",
        "P                                          P                  P             P",
        "P                                          P                       PPPPPP   P",
        "P                                          P   PPPPPPPPP                    P",
        "P    PPPPPPPP                              P                                P",
        "P                                          P                    PP          P",
        "P                          PPPPPPP         P                                P",
        "P                 PPPPPP                   P                                P",
        "P                                          P          PPPPPPP               P",
        "P         PPPPPPP                          P                      PPPPP     P",
        "P                                          P                                P",
        "P                     PPPPPP                                                P",
        "P                                                                           P",
        "P   PPPPPPPPPPP                    PPPP   PPP                               P",
        "P                                          P                   PPPPPPP      P",
        "P                 PPPPPPPPPPP              P                                P",
        "P                                          P         PPPP                   P",
        "P                                                  PP             PPPPP     P",
        "P                                                PP                         P",
        "P                                              P                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "T":
                t = Transfer(x, y)
                platforms.append(t)
                entities.add(t)
            x += 32
        y += 32
        x = 0

    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT: 
				game_intro()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        # draw background
        for y in range(32):
            for x in range(32):
                screen.blit(bg, (x * 32, y * 32))

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32,32))
        self.image.fill(Color("#70CC14"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self, up, down, left, right, running, platforms):
        if up:
            # only jump if on the ground
            if self.onGround: self.yvel -= 10
        if down:
            pass
        if running:
            self.xvel = 12
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#CC1414"))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))

class Transfer(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#000055"))

if __name__ == "__main__":
    main()
