import pygame

playing = True 
pygame.init()
pygame.font.init()
Font = pygame.font.SysFont('comicsans', 40, "bold")
Font1 = pygame.font.SysFont('comicsans', 80, "bold")
red_health = 10
yellow_health = 10
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 600))
bg = pygame.image.load('assets/back ship.png')
ship2 = pygame.transform.rotate((pygame.transform.scale((pygame.image.load('assets/ship 1.png')), (70, 70))), 270)
ship1 = pygame.transform.rotate((pygame.transform.scale((pygame.image.load('assets/ship 2.png')), (70, 70))), 90)
sound1 = pygame.mixer.Sound('assets/sound eeffect 1.mp3')
sound2 = pygame.mixer.Sound('assets/sound effect 2.mp3')

red = pygame.Rect(800, 300, 50, 50)
yellow = pygame.Rect(100, 300, 50, 50)
yellow_bullets = []
red_bullets = []

def redmovement(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and (red.x > 500):
        red.x -= 5
    if keys_pressed[pygame.K_RIGHT] and (red.x < 930):
        red.x += 5
    if keys_pressed[pygame.K_UP] and (red.y > 0):
        red.y -= 5
    if keys_pressed[pygame.K_DOWN] and (red.y < 530):
        red.y += 5

def yellowmovement(keys_pressed):
    if keys_pressed[pygame.K_a] and (yellow.x > 0):
        yellow.x -= 5
    if keys_pressed[pygame.K_d] and (yellow.x < 450):
        yellow.x += 5
    if keys_pressed[pygame.K_w] and (yellow.y > 0):
        yellow.y -= 5
    if keys_pressed[pygame.K_s] and (yellow.y < 530):
        yellow.y += 5

while playing: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        # Creating bullets
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(yellow.x+25, yellow.y+32, 10, 5)
                yellow_bullets.append(bullet)
            if event.key == pygame.K_RETURN:
                bullet = pygame.Rect(red.x-10, red.y+32, 10, 5)
                red_bullets.append(bullet)
                
    screen.blit(bg, (0, 0))
  
    # Displaying yellow font 
    text1 = Font.render(str(yellow_health) + " lives", True, "white")
    screen.blit(text1, (10, 0))
    # Displaying red font
    text2 = Font.render(str(red_health) + " lives", True, "white")
    screen.blit(text2, (850, 0))
    
    screen.blit(ship2, (red.x, red.y))
    screen.blit(ship1, (yellow.x, yellow.y))
    keys_pressed = pygame.key.get_pressed()
    redmovement(keys_pressed)
    yellowmovement(keys_pressed)
    
    # Drawing yellow bullets
    for bullet in yellow_bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)
        bullet.x += 10
        if bullet.colliderect(red):
            yellow_bullets.remove(bullet)
            red_health -= 1
        elif bullet.x > 1000:
            yellow_bullets.remove(bullet)
    
    # Drawing red bullets
    for bullet in red_bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)
        bullet.x -= 10
        if bullet.colliderect(yellow):
            red_bullets.remove(bullet)
            yellow_health -= 1
        elif bullet.x < 0:
            red_bullets.remove(bullet)
            
    #displaying who won
    winner_text = ""
    if yellow_health <=0:
        winner_text = "red wins"
        text1 = Font1.render(winner_text, True, "white")
        screen.blit(text1, (275, 50))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        
    if red_health <=0:
        winner_text = "yellow wins"
        text1 = Font1.render(winner_text, True, "white")
        screen.blit(text1, (275, 50))
        pygame.display.update()
        pygame.time.delay(3000)       
        pygame.quit()
        
    pygame.display.update()
