import os
import pygame
import turtle
import random

window = pygame.window()
win_width = 1900
win_height = 1080
play_width = 480
play_height = 360
tile_size = 40
sx = (win_width - play_width) / 2
sy = (win_height - play_height) / 2
csx =  0
csy = 0
snake_body = {(4,5),(3,5)}
grid = ((play_width/tile_size), (play_height/tile_size))


class Apple(object):
    def __init__(self, x, y,):
        self.x = x
        self.y = y

class Snake_Head(object):
    def __init__(self, face, fd, sx, sy):
        self.face = 1
        self.sx = 1
        self.sy = 1

def Move_Forward():
    r =  Snake_Head.face
    if r == 1:
       nx = Snake_Head.sx + 1
    if r == 2:
       ny = Snake_Head.sy - 1
    if r == 3:
       nx = Snake_Head.sx - 1
    if r == 4:
       ny = Snake_Head.sy + 1
    return Snake_Head(sx = nx, sy = ny)
    

def create_grid(apple_location = {}):
    grid = [[(0,0,0) for _ in range(12)] for _ in range(9)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in apple_location:
                c = apple_location[(j,i)]
                grid[i][j] = c
    return grid

def valid_space(snake_body, grid):
    accepted_pos = [[(j, i) for j in range(12) if grid[i][j] == (0,0,0)] for i in range(9)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = snake_body

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

def draw_grid():

    for i in range(len(grid)):
        turtle.setpos((sx, sy + i * grid), (sx + play_width, sy+ i * grid))
        turtle.setheading(270)
        turtle.pencolor((128,128,128))
        turtle.pendown
        turtle.forward(play_height)
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * tile_size, sy),(sx + j * tile_size, sy + play_height))
    pass

def valid_space():
    pass

def check_lost():
    head = Snake_Head(sx,sy)
    if head in snake_body:
        winner = False
    return winner

def Grow():
    old_tail = snake_body.pop
    snake_body.add(old_tail)
    Move_Forward
    snake_body.add(old_tail)
    pass
    

def remove_trail():
    pass

def draw_window():
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, (sx + 20, sy + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (sx + j * tile_size, sy + i * tile_size, tile_size, tile_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (sx, sy, play_width, play_height), 5)

    draw_grid(surface, grid)

def get_apple():
    if not Apple == (7, 5): 
        X = (0, 12, random.choice())
        Y = (0, 9, random.choice())
    return Apple(X, Y)

def main():

    grid = create_grid()
    next_apple = False
    run = True
    current_apple = get_apple()
    score = 0
    clock = pygame.time.Clock()
    move_time = 0
    move_speed = 0.3

    


    

    while run:
        
        apple_location = {}
        grid = create_grid(apple_location)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()
        head = (Snake_Head(sx), Snake_Head(sy))
        if move_time/1000 > move_speed:
            move_time = 0
            Move_Forward(Snake_Head)

        if head == current_apple():
            Grow


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not(Snake_Head(face=1) == True):
                        Snake_Head(face=3)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if not(Snake_Head(face=3) == True):
                        Snake_Head(face=1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not(Snake_Head(face=2) == True):
                        Snake_Head(face=4)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if not(Snake_Head(face=4) == True):
                        Snake_Head(face=2)          
    pass

def draw_text_middle(surface, text, size, image):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, image)

def main_menu(win):
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle(win, 'Press Any Key', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()
    pass


win = pygame.display.set_mode((play_width, play_height))

pygame.display.set_caption('Ekans')
main_menu(win)
