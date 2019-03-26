import pygame
import time
import random
                
# init pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
font = pygame.font.Font('Gameplay.ttf', 20)
title_font = pygame.font.Font('Gameplay.ttf', 50)

# load and set the logo
logo = pygame.image.load("simon_logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Simon")

# define colors
red = (100, 0, 0)
light_red = (255, 0, 0)
green = (0, 100, 0)
light_green = (0, 255, 0)
yellow = (100, 100, 0)
light_yellow = (255, 255, 0)
blue = (0, 0, 100)
light_blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# current colors
green_color = green
red_color = red
yellow_color = yellow
blue_color = blue

# blink time
green_time = 0
red_time = 0
yellow_time = 0
blue_time = 0

# define color sounds
green_sound = pygame.mixer.Sound('green.wav')
red_sound = pygame.mixer.Sound('red.wav')
yellow_sound = pygame.mixer.Sound('yellow.wav')
blue_sound = pygame.mixer.Sound('blue.wav')

# define screen
screen = pygame.display.set_mode((600, 700))

# define running variable
running = True

# score and pattern variable
score = 0
pattern = []
player_pattern = []

def show_pattern(pattern):
    '''
    1 = green
    2 = red
    3 = yellow
    4 = blue
    '''
    
    time_delay = 400
    
    for x in pattern:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.time.delay(time_delay)
        
        if x == 1:
            draw_screen(g = light_green)
            green_sound.play()
            pygame.time.delay(time_delay)
            green_sound.stop()
            draw_screen()
        elif x == 2:
            draw_screen(r = light_red)
            red_sound.play()
            pygame.time.delay(time_delay)
            red_sound.stop()
            draw_screen()
        elif x == 3:
            draw_screen(y = light_yellow)
            yellow_sound.play()
            pygame.time.delay(time_delay)
            yellow_sound.stop()
            draw_screen()
        elif x == 4:
            draw_screen(b = light_blue)
            blue_sound.play()
            pygame.time.delay(time_delay)
            blue_sound.stop()
            draw_screen()

    pygame.time.delay(time_delay)
            
        
def draw_screen(g = green, r = red, y = yellow, b = blue):
    # refresh display
    screen.fill(black)

    # draw elements
    score_text = font.render('Score: ' + str(score), True, white)
    screen.blit(score_text, (450, 50))

    pygame.draw.rect(screen, g, pygame.Rect(50, 150, 250, 250))
    pygame.draw.rect(screen, r, pygame.Rect(300, 150, 250, 250))
    pygame.draw.rect(screen, y, pygame.Rect(50, 400, 250, 250))
    pygame.draw.rect(screen, b, pygame.Rect(300, 400, 250, 250))

    pygame.display.update()


def wait_for_start():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP and event.key == 32:
                waiting = False
                break

        start_text1 = title_font.render('Press SPACE', True, white)
        start_text2 = title_font.render('to start!', True, white)
        screen.blit(start_text1, (110, 300))
        screen.blit(start_text2, (150, 375))
        pygame.display.update()
    
wait_for_start()

pattern.append(random.randint(1, 4))
show_pattern(pattern)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]

            if 50 < x < 300 and 150 < y < 400 and green_time == 0:
                print('GREEN CLICK')
                green_color = light_green
                green_sound.play()
                player_pattern.append(1)
            elif 300 < x < 550 and 150 < y < 400 and red_time == 0:
                print('RED CLICK')
                red_color = light_red
                red_sound.play()
                player_pattern.append(2)
            elif 50 < x < 300 and 400 < y < 650 and yellow_time == 0:
                print('YELLOW CLICK')
                yellow_color = light_yellow
                yellow_sound.play()
                player_pattern.append(3)
            elif 300 < x < 550 and 400 < y < 650 and blue_time == 0:
                print('BLUE CLICK')
                blue_color = light_blue
                blue_sound.play()
                player_pattern.append(4)
            

    # reset colors
    if green_color == light_green:
        if green_time == 0:
            green_time = time.clock()
        else:
            if time.clock() > green_time + 0.4:
                green_color = green
                green_sound.stop()
                green_time = 0
                
    if red_color == light_red:
        if red_time == 0:
            red_time = time.clock()
        else:
            if time.clock() > red_time + 0.4:
                red_color = red
                red_sound.stop()
                red_time = 0
                
    if yellow_color == light_yellow:
        if yellow_time == 0:
            yellow_time = time.clock()
        else:
            if time.clock() > yellow_time + 0.4:
                yellow_color = yellow
                yellow_sound.stop()
                yellow_time = 0
                
    if blue_color == light_blue:
        if blue_time == 0:
            blue_time = time.clock()
        else:
            if time.clock() > blue_time + 0.4:
                blue_color = blue
                blue_sound.stop()
                blue_time = 0
    
    # check pattern
    if player_pattern != []:
        if player_pattern != pattern[len(player_pattern)-1]:
            running = False
    if player_pattern == pattern:
        score += 1
        player_pattern = []
        pattern.append(random.randint(1, 4))
        show_pattern(pattern)

    # refresh display
    screen.fill(black)

    # draw elements
    score_text = font.render('Score: ' + str(score), True, white)
    screen.blit(score_text, (450, 50))

    pygame.draw.rect(screen, green_color, pygame.Rect(50, 150, 250, 250))
    pygame.draw.rect(screen, red_color, pygame.Rect(300, 150, 250, 250))
    pygame.draw.rect(screen, yellow_color, pygame.Rect(50, 400, 250, 250))
    pygame.draw.rect(screen, blue_color, pygame.Rect(300, 400, 250, 250))

    pygame.display.update()
    clock.tick(60)


pygame.display.quit()
pygame.quit()


