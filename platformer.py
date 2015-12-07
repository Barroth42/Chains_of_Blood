#! /usr/bin/python

import pygame
import time
import random
from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 640

 

DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30
switch = False
enemy = False

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
intro_music = "Intro.wav"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 100)

def load_music(x):
	song = pygame.mixer.music.load(x)    #for music
	return(song)
		
def game_display(WIN_WIDTH,WIN_HEIGHT):
	DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
	return(DISPLAY)

def half_width(WIN_WIDTH):
	HALF_WIDTH = int(WIN_WIDTH / 2)
	#HALF_HEIGHT = int(WIN_HEIGHT / 2)
	return(HALF_WIDTH)
	
def half_height(WIN_HEIGHT):
	HALF_HEIGHT = int(WIN_HEIGHT / 2)
	return(HALF_HEIGHT)	
	
def game_intro():						#added by Jorge for intro
    
    load_music(intro_music)
    #pygame.mixer.music.load("Intro.wav")    #for music
    pygame.mixer.music.play(-1,0.0)			#go forever and start at begining
    bg = Surface((32,32))
    bg.convert()
    bg = pygame.image.load("red_background.png")
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit, "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
					game_credit()
                if event.key == pygame.K_p:
                    level_1()
                if event.key == pygame.K_q:
                    raise SystemExit, "QUIT"
                if event.key == pygame.K_s:
					game_story()	
                if event.key == pygame.K_c:
					game_controls()

        #gameDisplay.fill(black)
        screen.blit(bg,(0,0))
        
        #blit
        message_to_screen("Chains of Blood",
                          red,
                          -150,
                          "large")

        message_to_screen("Demo",
                          red,
                          -100,
                          "medium")

        message_to_screen("Press p to play.",
                          red,
                          -50)
                          
        message_to_screen("Press c to view in game controls.",
                          red,
                          10)
                          
        message_to_screen("Press v to veiw credits.",
                          red,
                          40) 
                          
        message_to_screen("Press s to veiw story.",
                          red,
                          70)   
        message_to_screen("Press q to quit.",
                          red,
                          130)                                    
    
        pygame.display.update()
        clock.tick(15)

def game_controls():					#added by Jorge for controls screen
	
	
    bg = Surface((32,32))
    bg.convert()
    bg = pygame.image.load("red_background.png")
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
    
    controls = True

    while controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
				raise SystemExit, "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    controls=False
                if event.key == pygame.K_q:
                    raise SystemExit, "QUIT"
        screen.blit(bg,(0,0))
        #gameDisplay.fill(black)
        message_to_screen("Chains of Blood",
                          red,
                          -150,
                          "large")

        message_to_screen("Game Controls",
                          red,
                          -50)
                          
        message_to_screen("Press left arrow to move to the left.",
                          red,
                          -20)                          
                          
        message_to_screen("Press r arrow to move to the right.",
                          red,
                          10) 
                                                   
        message_to_screen("Press up arrow to jump.",
                          red,
                          40)
           
        message_to_screen("Press r to return to the main menu.",
                          red,
                          100)                          
                          
        message_to_screen("Press q to quit.",
                          red,
                          130)
                          
                
    
        pygame.display.update()
        clock.tick(15)

def game_scores():					#added by Jorge for reads file dispalys scores

    scores = True
    
    bg = Surface((32,32))
    bg.convert()
    bg = pygame.image.load("red_background.png")
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
    
    while scores:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
				raise SystemExit, "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    scores=False
                    game_intro()
                if event.key == pygame.K_q:
                    raise SystemExit, "QUIT"
   
        
        #gameDisplay.fill(black)
        screen.blit(bg,(0,0))
        
        message_to_screen("Chains of Blood",
                          red,
                          -150,
                          "large")

        message_to_screen("High Scores",
                          red,
                          -50)
           
        message_to_screen("Press r to return to the main menu.",
                          red,
                          100)                          
                          
        message_to_screen("Press q to quit.",
                          red,
                          130)
                          
                          
        file_object = open('Scores.txt')
        all_the_text = file_object.read(  )
        message_to_screen(all_the_text, red, 180)
        file_object.close(  )
                
                
    
        pygame.display.update()
        clock.tick(15)

def game_credit():						#added by Jorge for credit screen

    credit = True
    
    bg = Surface((32,32))
    bg.convert()
    bg = pygame.image.load("red_background.png")
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
    
    while credit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
				raise SystemExit, "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    credit=False
                if event.key == pygame.K_q:
                    raise SystemExit, "QUIT"
   
        #gameDisplay.fill(black)
        screen.blit(bg,(0,0))
        
        message_to_screen("Chains of Blood",
                          red,
                          -150,
                          "large")

        message_to_screen("Created by Cory Morales, Andrew Lee, Brain Kidd, and Jorge Benavides",
                          red,
                          -50)
                          
        message_to_screen("Press q to quit.",
                          red,
                          40)
                          
        message_to_screen("Press r to return to the main menu.",
                          red,
                          10)                
    
        pygame.display.update()
        clock.tick(15)            
               
def game_story():						#added by Jorge for story screen
	
    bg = Surface((32,32))
    bg.convert()
    bg = pygame.image.load("red_background.png")
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
	
    story = True

    while story:
		
		
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
				raise SystemExit, "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    story = False
                if event.key == pygame.K_q:
                    raise SystemExit, "QUIT"
        #gameDisplay.fill(black)
        screen.blit(bg,(0,0))
        
        message_to_screen("Chains of Blood",
                          red,
                          -150,
                          "large")

        message_to_screen_left("In a land where only two ruled. The King of the North, Dag, and the King of the South, Oberon.", red, -50, 0)
        message_to_screen_left("Dag had no sons, while Oberon had two sons, Gulag and Asger. One day Dag captured the ", red, -30, 0)
        message_to_screen_left("youngest son Goulac. Oberon instructed Asger to rescue his brother. ", red, -10, -10)
        message_to_screen_left("Asger goes to rescue his brother, but upon reaching the Dags castle he is horrified", red, 10, 0)
        message_to_screen_left(" by a bloody southerner at the gates. The southerner warns him that the castle has been ", red, 30, 0)
        message_to_screen_left("taken over by a plague transforming the inhabitants...", red , 50, 0)
                          
        message_to_screen("Press q to quit.",
                          red,
                          120)
                          
        message_to_screen("Press r to return to the main menu.",
                          red,
                          100)                
    
        pygame.display.update()
        clock.tick(15)     
                                   
def text_objects(text,color,size):		#added by Jorge for text
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    
    return textSurface, textSurface.get_rect()

def message_to_screen_left(msg,color, y_displace=0, x_displace=0, size = "small"):  #added by Jorge to place text on screen align left
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (half_width(WIN_WIDTH))+x_displace, (half_height(WIN_HEIGHT))+y_displace
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg,color, y_displace=0, size = "small"):  #added by Jorge to place text on screen
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (half_width(WIN_WIDTH)), (half_height(WIN_HEIGHT))+y_displace
    gameDisplay.blit(textSurf, textRect)

def BossLevel():
    global cameraX, cameraY

    pygame.init()
    pygame.mixer.music.stop()								#added by Jorge to stop music from intro
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
    pygame.display.set_caption("Chains of Blood!")			#Jorge changed to game name
    timer = pygame.time.Clock()

    up = down = left = right = running = False
    bg = Surface((32,32))
    bg.convert()
    #bg.fill(Color("#000000"))
    bg = pygame.image.load("boss_background.png")
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []
    
    
    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                   P",
        "P                                 MMP",        
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "M":
                m = ExitGame(x, y)
                platforms.append(m)
                entities.add(m)        
            x += 32
        y += 32
        x = 0

    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)
        #screen.blit(bg,(0,0))
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
                
        screen.blit(bg,(0,0))
        #draw background
        #for y in range(32):
            #for x in range(32):
                #screen.blit(bg, (x * 32, y * 32))

        

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)

        
        for e in entities:
            screen.blit(e.image, camera.apply(e))
            
	#s.update()

	#for e in entities:
	 #   if e == w:
	#	e.update()

        pygame.display.update()

def level_3():
    global cameraX, cameraY

    pygame.init()
    pygame.mixer.music.stop()								#added by Jorge to stop music from intro
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
    pygame.display.set_caption("Chains of Blood!")			#Jorge changed to game name
    timer = pygame.time.Clock()

    up = down = left = right = running = False
    bg = Surface((32,32))
    bg.convert()
    #bg.fill(Color("#000000"))
    bg = pygame.image.load("updated_background.png")
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []
    enemy1 = Enemy1(32,32)
    enemy2 = Enemy2(32,32)
    enemy3 = Enemy3(32,32)
    enemy4 = Enemy4(32,32)
    entities.add(enemy1)
    entities.add(enemy2)
    entities.add(enemy3)
    entities.add(enemy4)
    
    
    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P           P           P                  P                                P",
        "P           P           P                  P                         PPPPP  P",
        "P                       P                  P        PPPPPP                  P",
        "P                  PPPPPPPPPPP             P                                P",
        "P      PPPPPPPP                     P                         P             P",
        "P                                   P                  P              PPP   P",
        "P                         P         P                  P                    P",
        "PPPPPPPPPPPPPPPP    PPPPPPPPPPPPPPPPPPPPPPPP    PPPPPPPPPPPPPPPPPPPP        P",
        "P                       P                                       PP          P",
        "P                       P                                                   P",
        "P                 PPPPPPP                                                   P",
        "P                                                                           P",
        "P         PPPPPPPPP             PPPPPPPPPPPPPPPP                  PPPPP     P",
        "P         P                           P                                     P",
        "P         P                           P                                     P",
        "P         P                           P                                     P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPPPPPPPPP",
        "P                                                                           P",
        "P                                                                           P",
        "P           PPPPPPPPPPPPPPP                          PPPPPP                 P",
        "P                                  P                              PPPPP     P",
        "P                                  P                                        P",
        "PMM                                P                                        P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "M":
                m = ExitToBossLevel(x, y)
                platforms.append(m)
                entities.add(m)
            if col == "b":
		    f = Enemy(x, y)
		    platforms.append(f)
		    entities.add(f)        
	    if col == "S":
		s = Switch(x, y)
		platforms.append(s)
		entities.add(s)
            x += 32
        y += 32
        x = 0

    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)
        #screen.blit(bg,(0,0))
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
                
        screen.blit(bg,(0,0))
        # draw background
        #for y in range(32):
            #for x in range(32):
                #screen.blit(bg, (x * 32, y * 32))

        

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)
        enemy1.update(platforms)
        enemy2.update(platforms)
        enemy3.update(platforms)
        enemy4.update(platforms)

        
        for e in entities:
            screen.blit(e.image, camera.apply(e))
            
	#s.update()

	#for e in entities:
	 #   if e == w:
	#	e.update()

        pygame.display.update()

def level_2():
    global cameraX, cameraY

    pygame.init()
    pygame.mixer.music.stop()								#added by Jorge to stop music from intro
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
    pygame.display.set_caption("Chains of Blood!")			#Jorge changed to game name
    timer = pygame.time.Clock()

    up = down = left = right = running = False
    bg = Surface((32,32))
    bg.convert()
    #bg.fill(Color("#000000"))
    bg = pygame.image.load("updated_background.png")
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []
    enemy1 = Enemy1(32,32)
    enemy2 = Enemy2(32,32)
    enemy3 = Enemy3(32,32)
    enemy4 = Enemy4(32,32)
    entities.add(enemy1)
    entities.add(enemy2)
    entities.add(enemy3)
    entities.add(enemy4)
    
    
    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P           P           P                  P                                P",
        "P           P           P                  P                         PPPPP  P",
        "P                       P                  P        PPPPPP                  P",
        "P                  PPPPPPPPPPP             P                                P",
        "P      PPPPPPPP                     P                         P             P",
        "P      P                            P                  P              PPP   P",
        "P      P                  P         P                  P                    P",
        "PPPPPPPPPPPPPPPP    PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP        P",
        "P                       P                                       PP          P",
        "P                       P                                                   P",
        "P                 PPPPPPP                                                   P",
        "P                 P                                                         P",
        "P         PPPPPPPPP                                               PPPPP     P",
        "P         P                                                                 P",
        "P         P                                                                 P",
        "P         P                                                                 P",
        "P         PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP     PPPPPPPPPPPPPPPPP",
        "P                                          P                                P",
        "P                                          P                                P",
        "P                                          P         PPPPPP                 P",
        "P                                          P                      PPPPP     P",
        "P                                          P                                P",
        "P                                        BBP                              MMP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "M":
                m = ExitToLevel_3(x, y)
                platforms.append(m)
                entities.add(m)
            if col == "B":
                b = ExitToBossLevel(x, y)
                platforms.append(b)
                entities.add(b)
                   
	    if col == "S":
		s = Switch(x, y)
		platforms.append(s)
		entities.add(s)
            x += 32
        y += 32
        x = 0

    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)
        #screen.blit(bg,(0,0))
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
                
        screen.blit(bg,(0,0))
        # draw background
        #for y in range(32):
            #for x in range(32):
                #screen.blit(bg, (x * 32, y * 32))

        

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)
        enemy1.update(platforms)
        enemy2.update(platforms)
        enemy3.update(platforms)
        enemy4.update(platforms)

        
        for e in entities:
            screen.blit(e.image, camera.apply(e))
            
	#s.update()

	#for e in entities:
	 #   if e == w:
	#	e.update()

        pygame.display.update()

def level_1():
    global cameraX, cameraY
    global switch
    global enemy
    pygame.init()
    pygame.mixer.music.stop()								#added by Jorge to stop music from intro
    screen = pygame.display.set_mode(game_display(WIN_WIDTH, WIN_HEIGHT), FLAGS, DEPTH)
    pygame.display.set_caption("Chains of Blood!")			#Jorge changed to game name
    timer = pygame.time.Clock()

    up = down = left = right = running = False
    bg = Surface((32,32))
    bg.convert()
    #bg.fill(Color("#000000"))
    bg = pygame.image.load("updated_background.png")
    entities = pygame.sprite.Group()
    player = Player(32, 32)
    platforms = []
    enemy1 = Enemy1(32,32)
    enemy2 = Enemy2(32,32)
    enemy3 = Enemy3(32,32)
    enemy4 = Enemy4(32,32)
    entities.add(enemy1)
    entities.add(enemy2)
    entities.add(enemy3)
    entities.add(enemy4)
    
    
    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P                              EEP",
        "P                                          P                         PPPPP  P",
        "P                                          P        PPPPPP                  P",
        "P         S         PPPPPPPPPPP            P                                P",
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
        "P                     PPPPPP               P                                P",
        "P                                          W                                P",
        "P   PPPPPPPPPPP                    PPPP   PPP                               P",
        "P                                          P                   PPPPPPP      P",
        "P                 PPPPPPPPPPP              P                                P",
        "P                                          P         PPPP                   P",
        "P                                          P                      PPPPP     P",
        "P                                          P                                P",
        "P                                          P                                P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitToLevel_2(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "W":
                w = Wall(x, y)
                platforms.append(w)
                entities.add(w)
            if col == "F":
		    f = Enemy(x, y)
		    platforms.append(f)
		    entities.add(f)        
	    if col == "S":
		s = Switch(x, y)
		platforms.append(s)
		entities.add(s)
            x += 32
        y += 32
        x = 0

    total_level_width  = len(level[0])*32
    total_level_height = len(level)*32
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)
        #screen.blit(bg,(0,0))
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
                
        screen.blit(bg,(0,0))
        # draw background
        #for y in range(32):
            #for x in range(32):
                #screen.blit(bg, (x * 32, y * 32))

        

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)
        enemy1.update(platforms)
        enemy2.update(platforms)
        enemy3.update(platforms)
        enemy4.update(platforms)

        
        for e in entities:
            screen.blit(e.image, camera.apply(e))
            
	s.update()

	for e in entities:
	    if e == w:
		e.update()

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
    return Rect(-l+half_width(WIN_WIDTH), -t+(half_height(WIN_HEIGHT)), w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+half_width(WIN_WIDTH), -t+(half_height(WIN_HEIGHT)), w, h

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
        #self.image.fill(Color("#00FF00"))
        self.image = pygame.image.load("Player_Right.png")
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
            self.image = pygame.image.load("Player_Left.png")
        if right:
            self.xvel = 8
            self.image = pygame.image.load("Player_Right.png")
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 300: self.yvel = 300
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
	global switch
	global enemy
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
				
                
                if isinstance(p, ExitToLevel_2):
					level_2() 
                if isinstance(p, ExitToLevel_3):
                    level_3()
                if isinstance(p, ExitToBossLevel):
					BossLevel() 
                if isinstance(p, ExitGame):
					game_scores()    
		if isinstance(p, Switch):
		    switch = True
		if isinstance(p, Enemy):
			enemy = True
		if isinstance(p, Wall):
		    if(switch == True):
			switch = True

		    else:
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
		else:
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
        
class Enemy1(Entity):		#added by Jorge
    def __init__(self, x, y):
        Entity.__init__(self)
        self.yVel = 0
        self.xVel = 2 # start moving immediately
        self.image = Surface((32,32))
        #self.image.fill(Color("#00FF00"))
        self.image.convert()
        self.rect = Rect(400, 382, 32, 32)
        self.onGround = False
        

    def update(self, platforms):
        if not self.onGround:
            self.yVel += 0.3
        
        # no need for right_dis to be a member of the class,
        # since we know we are moving right if self.xVel > 0
        right_dis = self.xVel > 0

        # create a point at our left (or right) feet 
        # to check if we reached the end of the platform
        m = (1, 1) if right_dis else (-1, 1)
        self.image = pygame.image.load("Skeleton_Left.png")
        p = self.rect.bottomright if right_dis else self.rect.bottomleft
        fp = map(sum, zip(m, p))

        # if there's no platform in front of us, change the direction
        collide = any(p for p in platforms if p.rect.collidepoint(fp))
        if not collide:
            self.xVel *= -1
            self.image = pygame.image.load("Skeleton_Right.png")
        self.rect.left += self.xVel # increment in x direction
        self.collide(self.xVel, 0, platforms) # do x-axis collisions
        self.rect.top += self.yVel # increment in y direction
        self.onGround = False; # assuming we're in the air
        self.collide(0, self.yVel, platforms) # do y-axis collisions

    def collide(self, xVel, yVel, platforms):
        for p in platforms:
            
            if pygame.sprite.collide_rect(self, p):
                if xVel > 0: 
                    self.rect.right = p.rect.left
                    self.xVel *= -1 # hit wall, so change direction
                if xVel < 0: 
                    self.rect.left = p.rect.right
                    self.xVel *= -1 # hit wall, so change direction
                if yVel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                if yVel < 0:
                    self.rect.top = p.rect.bottom
                    
class Enemy2(Entity):		#added by Jorge
    def __init__(self, x, y):
        Entity.__init__(self)
        self.yVel = 0
        self.xVel = 2 # start moving immediately
        self.image = Surface((32,32))
        #self.image.fill(Color("#00FF00"))
        self.image.convert()
        self.rect = Rect(600, 320, 32, 32)
        self.onGround = False

    def update(self, platforms):
        if not self.onGround:
            self.yVel += 0.3

        # no need for right_dis to be a member of the class,
        # since we know we are moving right if self.xVel > 0
        right_dis = self.xVel > 0
        self.image = pygame.image.load("Skeleton_Right.png")
        
        # create a point at our left (or right) feet 
        # to check if we reached the end of the platform
        m = (1, 1) if right_dis else (-1, 1)
        p = self.rect.bottomright if right_dis else self.rect.bottomleft
        fp = map(sum, zip(m, p))

        # if there's no platform in front of us, change the direction
        collide = any(p for p in platforms if p.rect.collidepoint(fp))
        if not collide:
            self.xVel *= -1

        self.rect.left += self.xVel # increment in x direction
        self.collide(self.xVel, 0, platforms) # do x-axis collisions
        self.rect.top += self.yVel # increment in y direction
        
        self.onGround = False; # assuming we're in the air
        self.collide(0, self.yVel, platforms) # do y-axis collisions

    def collide(self, xVel, yVel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xVel > 0: 
                    self.rect.right = p.rect.left
                    self.xVel *= -1 # hit wall, so change direction
                if xVel < 0: 
                    self.rect.left = p.rect.right
                    self.xVel *= -1 # hit wall, so change direction
                if yVel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                if yVel < 0:
                    self.rect.top = p.rect.bottom

class Enemy3(Entity):		#added by Jorge
    def __init__(self, x, y):
        Entity.__init__(self)
        self.yVel = 0
        self.xVel = 2 # start moving immediately
        self.image = Surface((32,32))
        #self.image.fill(Color("#00FF00"))
        self.image = pygame.image.load("Skeleton_Right.png")
        self.image.convert()
        self.rect = Rect(900, 320, 32, 32)
        self.onGround = False

    def update(self, platforms):
        if not self.onGround:
            self.yVel += 0.3

        # no need for right_dis to be a member of the class,
        # since we know we are moving right if self.xVel > 0
        right_dis = self.xVel > 0
        self.image = pygame.image.load("Skeleton_Right.png")
        
        # create a point at our left (or right) feet 
        # to check if we reached the end of the platform
        m = (1, 1) if right_dis else (-1, 1)
        p = self.rect.bottomright if right_dis else self.rect.bottomleft
        fp = map(sum, zip(m, p))

        # if there's no platform in front of us, change the direction
        collide = any(p for p in platforms if p.rect.collidepoint(fp))
        if not collide:
            self.xVel *= -1

        self.rect.left += self.xVel # increment in x direction
        self.collide(self.xVel, 0, platforms) # do x-axis collisions
        self.rect.top += self.yVel # increment in y direction
        self.onGround = False; # assuming we're in the air
        self.collide(0, self.yVel, platforms) # do y-axis collisions

    def collide(self, xVel, yVel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xVel > 0: 
                    self.rect.right = p.rect.left
                    self.xVel *= -1 # hit wall, so change direction
                if xVel < 0: 
                    self.rect.left = p.rect.right
                    self.xVel *= -1 # hit wall, so change direction
                if yVel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                if yVel < 0:
                    self.rect.top = p.rect.bottom
                    
class Enemy4(Entity):		#added by Jorge
    def __init__(self, x, y):
        Entity.__init__(self)
        self.yVel = 0
        self.xVel = 2 # start moving immediately
        self.image = Surface((32,32))
        #self.image.fill(Color("#00FF00"))
        self.image = pygame.image.load("Skeleton_Right.png")
        self.image.convert()
        self.rect = Rect(1700, 320, 32, 32)
        self.onGround = False

    def update(self, platforms):
        if not self.onGround:
            self.yVel += 0.3

        # no need for right_dis to be a member of the class,
        # since we know we are moving right if self.xVel > 0
        right_dis = self.xVel > 0

        # create a point at our left (or right) feet 
        # to check if we reached the end of the platform
        m = (1, 1) if right_dis else (-1, 1)
        p = self.rect.bottomright if right_dis else self.rect.bottomleft
        fp = map(sum, zip(m, p))

        # if there's no platform in front of us, change the direction
        collide = any(p for p in platforms if p.rect.collidepoint(fp))
        if not collide:
            self.xVel *= -1

        self.rect.left += self.xVel # increment in x direction
        self.collide(self.xVel, 0, platforms) # do x-axis collisions
        self.rect.top += self.yVel # increment in y direction
        self.onGround = False; # assuming we're in the air
        self.collide(0, self.yVel, platforms) # do y-axis collisions

    def collide(self, xVel, yVel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xVel > 0: 
                    self.rect.right = p.rect.left
                    self.xVel *= -1 # hit wall, so change direction
                if xVel < 0: 
                    self.rect.left = p.rect.right
                    self.xVel *= -1 # hit wall, so change direction
                if yVel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                if yVel < 0:
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

class ExitToLevel_2(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))
        
class ExitToLevel_3(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF")) 

class ExitToBossLevel(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))       

class ExitGame(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))

class Wall(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0025FF"))

    def update(self):
	if(switch == True):
	    self.image.fill(Color("#000000"))

class Switch(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#008592"))

    def update(self):
	if(switch == True):
	    self.image.fill(Color("#001283"))
	    
class Enemy(Platform):
    def __init__(self, x, y):
       Platform.__init__(self, x, y)
       self.image.fill(Color("#008592"))
       self.yVel = 0
       self.xVel = 2 # start moving immediately

    def update(self):
        self.yVel += 0.3

        # no need for right_dis to be a member of the class,
        # since we know we are moving right if self.xVel > 0
        right_dis = self.xVel > 0

        # create a point at our left (or right) feet 
        # to check if we reached the end of the platform
        m = (1, 1) if right_dis else (-1, 1)
        p = self.rect.bottomright if right_dis else self.rect.bottomleft
        fp = map(sum, zip(m, p))

        # if there's no platform in front of us, change the direction
        collide = any(p for p in platforms if p.rect.collidepoint(fp))
        if not collide:
            self.xVel *= -1

        self.rect.left += self.xVel # increment in x direction
        self.collide(self.xVel, 0, platforms) # do x-axis collisions
        self.rect.top += self.yVel # increment in y direction
        self.onGround = False; # assuming we're in the air
        self.collide(0, self.yVel, platforms) # do y-axis collisions

    def collide(self, xVel, yVel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xVel > 0: 
                    self.rect.right = p.rect.left
                    self.xVel *= -1 # hit wall, so change direction
                if xVel < 0: 
                    self.rect.left = p.rect.right
                    self.xVel *= -1 # hit wall, so change direction
                if yVel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                if yVel < 0:
                    self.rect.top = p.rect.bottom	    
	    
	    		
if __name__ == "__main__":
    game_intro()
    
