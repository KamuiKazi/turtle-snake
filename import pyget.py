import os
import sndhdr
import turtle
import random
import pygame

win_width = 1900
win_height = 1080
play_width = 450
play_height = 275
grid_size = win_height // 15

sx = (win_width - play_width) // 2
sy = win_height - play_height





class Apple(object):
    def __init__(self, x, y,):
        self.x = x
        self.y = y

class Snake_Head(object):
    def __init__(self, face, fd, sx, sy):
        self.face = 1
        self.sx = 75
        self.sy = 15

def Move_Forward():
    r =  Snake_Head.face
    if r = 1:
       nx = Snake_Head.sx + 1
    if r = 2:
       ny = Snake_Head.sy - 1
    if r = 3:
       nx = Snake_Head.sx - 1
    if r = 4:
       ny = Snake_Head.sy + 1
    return Snake_Head(sx = nx, sy = ny)
    

def create_grid():
    grid = [[(0,0,0) for _ in range(30)] for _ in range(150)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in snake_body:
                c = snake_body[(j,i)]
                grid[i][j] = c
    return grid

def draw_grid():

    for i in range(len(grid)):
        turtle.setpos((sx, sy + i*grid_size), (sx+play_width, sy+ i*grid_size))
        turtle.setheading(270)
        turtle.pencolor((128,128,128))
        turtle.pendown
        turtle.forward(play_height)
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))
    pass

def valid_space():
    pass

def check_lost():
    pass

def draw_body():
    snake_body = (1,2)
    pass

def remove_trail():
    pass

def draw_window():
    pass

def get_apple():
    X = (1, 150, random.choice())
    Y = (1, 30, random.choice())
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
        
        apple_locations = {}
        grid = create_grid(apple_location)

        grid = create_grid(current_apple)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if move_time/1000 > move_speed:
            move_time = 0
            Move_Forward(Snake_Head)

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

def main_menu(win):
    run = True
    pass



















win = window.resize(nlines=win_width, ncols=win_height)
main_menu(win)
