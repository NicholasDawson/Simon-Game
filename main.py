import pygame
import random
import time
import sys


########
# INIT #
########

# init pygame, audio mixer, and game clock
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# define constants
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

# init current color vars
green_color = green
red_color = red
yellow_color = yellow
blue_color = blue

# init fonts
gameplay_font_dir = './Assets/Fonts/Gameplay.ttf'
font = pygame.font.Font(gameplay_font_dir, 20)
title_font = pygame.font.Font(gameplay_font_dir, 50)

# init images
logo = pygame.image.load('./Assets/Images/simon_logo.png')
big_logo = pygame.transform.scale(logo, (300, 300))
start_button = pygame.image.load('./Assets/Images/start_button.png')
start_button = pygame.transform.scale(start_button, (240, 90))
again_button = pygame.image.load('./Assets/Images/again_button.png')
again_button = pygame.transform.scale(again_button, (240, 90))
exit_button = pygame.image.load('./Assets/Images/exit_button.png')
exit_button = pygame.transform.scale(exit_button, (240, 90))

# init sounds
green_sound = pygame.mixer.Sound('./Assets/Audio/green.wav')
red_sound = pygame.mixer.Sound('./Assets/Audio/red.wav')
yellow_sound = pygame.mixer.Sound('./Assets/Audio/yellow.wav')
blue_sound = pygame.mixer.Sound('./Assets/Audio/blue.wav')
lose_sound = pygame.mixer.Sound('./Assets/Audio/lose_sfx.wav')

# define game screen init window
screen = pygame.display.set_mode((600, 700))
pygame.display.set_icon(logo)
pygame.display.set_caption('Simon')

# define game global vars
score = 0
pattern = []
time_delay = 500
running = True


#############
# FUNCTIONS #
#############

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
    

def show_pattern():
    # 1 = GREEN
    # 2 = RED
    # 3 = YELLOW
    # 4 = BLUE

    time_delay = 500 - 100 * int(len(pattern) / 5)
    if time_delay <= 100:
        time_delay = 100

    draw_screen()
    pygame.time.delay(1000)

    for x in pattern:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        if x == 1:
            # GREEN
            draw_screen(g = light_green)
            green_sound.play()
            pygame.time.delay(time_delay)
            draw_screen()
            green_sound.stop()
        elif x == 2:
            # RED
            draw_screen(r = light_red)
            red_sound.play()
            pygame.time.delay(time_delay)
            draw_screen()
            red_sound.stop()
        elif x == 3:
            # YELLOW
            draw_screen(y = light_yellow)
            yellow_sound.play()
            pygame.time.delay(time_delay)
            draw_screen()
            yellow_sound.stop()
        elif x == 4:
            # BLUE
            draw_screen(b = light_blue)
            blue_sound.play()
            pygame.time.delay(time_delay)
            draw_screen()
            blue_sound.stop()

        pygame.time.delay(time_delay)


def new_pattern():
    global score
    score = len(pattern)
    pattern.append(random.randint(1, 4))


def check_pattern(player_pattern):
    if player_pattern != pattern[:len(player_pattern)]:
        lose_screen()


def click_listen():
    turn_time = time.time()
    player_pattern = []

    while time.time() <= turn_time + 3 and len(player_pattern) < len(pattern):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 50 < x < 300 and 150 < y < 400:
                    draw_screen(g = light_green)
                    green_sound.play()
                    pygame.time.delay(time_delay)
                    green_sound.stop()
                    draw_screen()
                    player_pattern.append(1)
                    check_pattern(player_pattern)
                    turn_time = time.time()
                elif 300 < x < 550 and 150 < y < 400:
                    draw_screen(r = light_red)
                    red_sound.play()
                    pygame.time.delay(time_delay)
                    red_sound.stop()
                    draw_screen()
                    player_pattern.append(2)
                    check_pattern(player_pattern)
                    turn_time = time.time()
                elif 50 < x < 300 and 400 < y < 650:
                    draw_screen(y = light_yellow)
                    yellow_sound.play()
                    pygame.time.delay(time_delay)
                    yellow_sound.stop()
                    draw_screen()
                    player_pattern.append(3)
                    check_pattern(player_pattern)
                    turn_time = time.time()
                elif 300 < x < 550 and 400 < y < 650:
                    draw_screen(b = light_blue)
                    blue_sound.play()
                    pygame.time.delay(time_delay)
                    blue_sound.stop()
                    draw_screen()
                    player_pattern.append(4)
                    check_pattern(player_pattern)
                    turn_time = time.time()

    if not time.time() <= turn_time + 3:
        lose_screen()

def quit_game():
        running = False
        pygame.display.quit()
        pygame.quit()
        sys.exit()

def lose_screen():
    lose_sound.play()

    global score

    # display lose screen
    screen.fill(black)
    lose_text = title_font.render('You Lose', True, white)
    score_text = title_font.render('Score: ' + str(score), True, white)
    screen.blit(lose_text, (161.5, 50))
    screen.blit(score_text, (((600 - title_font.size('Score: ' + str(score))[0]) / 2), 120))
    screen.blit(again_button, (180, 300))
    screen.blit(exit_button, (180, 450))

    pygame.display.update()

    # reset variables
    score = 0
    global pattern
    pattern = []
    global time_delay
    time_delay = 500
    global running
    running = True

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 180 <= x <= 420 and 300 <= y <= 390:
                    start_menu()
                elif 180 <= x <= 420 and 450 <= y <= 540:
                    quit_game()


def start_menu():
    waiting = True
    logo_bob = 150
    title_text = title_font.render('Simon', True, white)

    bob_direction = True    # true = down, false = up
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 180 <= x <= 420 and 530 <= y <= 620:
                    waiting = False

        # reset screen
        screen.fill(black)

        # display assets
        screen.blit(title_text, (220, 50))
        screen.blit(big_logo, (150, logo_bob))
        screen.blit(start_button, (180, 530))
        pygame.display.update()

        if logo_bob == 150:
            pygame.time.delay(300)
            bob_direction = True
        elif logo_bob == 190:
            pygame.time.delay(300)
            bob_direction = False

        if bob_direction:
            logo_bob += 0.5
        else:
            logo_bob -= 0.5

        clock.tick(60)

    while running:
        new_pattern()
        show_pattern()
        click_listen()


#############
# MAIN CODE #
#############

start_menu()


