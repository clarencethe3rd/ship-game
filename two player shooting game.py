import pygame
playing = True 
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000,600))
bg=pygame.image.load('assets/back ship.png')
ship1=pygame.transform.rotate((pygame.transform.scale((pygame.image.load('assets/ship 1.png')),(70,70))),270)
ship2=pygame.transform.rotate((pygame.transform.scale((pygame.image.load('assets/ship 2.png')),(70,70))),90)
sound1=pygame.mixer.Sound('assets/sound eeffect 1.mp3')
sound2=pygame.mixer.Sound('assets/sound effect 2.mp3')
yellow = pygame.Rect(800,300,50,50)
red = pygame.Rect(100,300,50,50)
def redmovement(keys_pressed):
    if keys_pressed[pygame.K_a] and (red.x>0):
        red.x -= 5
    if keys_pressed[pygame.K_d] and (red.x<500):
        red.x += 5
        
    if keys_pressed[pygame.K_w] and (red.y>0):
        red.y -= 5
    if keys_pressed[pygame.K_s] and (red.y<550):
        red.y += 5
        
while playing == True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    screen.blit(bg,(0,0))
    screen.blit(ship2,(red.x,red.y))
    screen.blit(ship1,(yellow.x,yellow.y))
    keys_pressed = pygame.key.get_pressed()
    redmovement(keys_pressed)
    
    
    pygame.display.update()
    