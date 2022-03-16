import os
import turtle

win_width = 1900
win_height = 1080
play_width = 450
play_height = 275
grid_size = win_height // 15

sx = (win_width - play_width) // 2
sy = win_height - play_height

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

def draw_snake():
    snake_body = (1,2)
    pass

def remove_trail():
    pass

def draw_window():
    pass

def next_apple():
    pass

def main():
    pass

def main_menu(win):
    run = True
    pass





while run:














win = window.resize(nlines=win_width, ncols=win_height)
main_menu(win)
