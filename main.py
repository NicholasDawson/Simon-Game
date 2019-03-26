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
time_delay = 400

def show_pattern():
    '''
    1 = green
    2 = red
    3 = yellow
    4 = blue
    '''

    draw_screen()
    pygame.time.delay(1000)

    for x in pattern:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

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

    click_listener()


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

def click_listener():
    clicks = 0
    player_pattern = []

    while clicks <= len(pattern):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 50 < x < 300 and 150 < y < 400 and green_time == 0:
                    print('GREEN CLICK')
                    draw_screen(g = light_green)
                    green_sound.play()
                    pygame.time.delay(time_delay)
                    green_sound.stop()
                    draw_screen()
                    player_pattern.append(1)
                    check_pattern(player_pattern)
                elif 300 < x < 550 and 150 < y < 400 and red_time == 0:
                    print('RED CLICK')
                    red_color = light_red
                    red_sound.play()
                    player_pattern.append(2)
                    check_pattern(player_pattern)
                elif 50 < x < 300 and 400 < y < 650 and yellow_time == 0:
                    print('YELLOW CLICK')
                    yellow_color = light_yellow
                    yellow_sound.play()
                    player_pattern.append(3)
                    check_pattern(player_pattern)
                elif 300 < x < 550 and 400 < y < 650 and blue_time == 0:
                    print('BLUE CLICK')
                    blue_color = light_blue
                    blue_sound.play()
                    player_pattern.append(4)
                    check_pattern(player_pattern)

def new_pattern():
    pattern.append(random.randint(1, 4))
    show_pattern()


def check_pattern(player_pattern):
    if len(player_pattern) == len(pattern) and player_pattern == pattern:
        score += 1
        new_pattern()
    elif len(player_pattern) != len(pattern):
        print('TODO')

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


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
