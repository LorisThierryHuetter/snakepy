import pygame
import neat
import time
import os
import random
import threading
import time

# initiates pygame
pygame.init()

# FPS number
FPS = 60
# fps time clock
fps = pygame.time.Clock()
# makes a variable with the loaded grid picture as background
bg = pygame.image.load("copyrightfreegrid.png")

# class for cubes
class food(object):     # TODO: make better and usefull snake class
    food = 0

# class for the snake
class snake(object):    # TODO: make better and usefull snake class
    size = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y

# TODO: make a food spawning function

# TODO: make a 2D array which saves what is on every block, like is there a snake on block 0,4 or food on block 2,3 etc.

# TODO: find out a way for the snake to grow and the body to move

def snakebody(win, block, blocksize, Gridvalues, previousPosition): # TODO: fix this, it laggs behind
    # TODO: Comment this function
    #Gridvalues[previousPosition[1]][previousPosition[0]] = 1
    #posX = previousPosition[0]
    #posY = previousPosition[1]
    #pygame.draw.rect(win, (255, 0, 0), ((block * posX), (block * posY), blocksize, blocksize))
    return 0

# TODO: Make everything into functions with correct returns

def screen():
    # window size
    WIN_WIDTH = 900
    WIN_HEIGTH = 900

    # displaying the window
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGTH))

    # game window title
    pygame.display.set_caption("Machine learning Pygame")

    # game icon (from: https://pixabay.com/vectors/anatomy-biology-brain-thought-mind-1751201/)
    icon = pygame.image.load("brain.png")
    pygame.display.set_icon(icon)

    # returns the win value
    return win

# function to check which direction the player is currently moving or wants to move
def directionCheck(event, direction, countdown):
    # whenever a key gets pressed
    if event.type == pygame.KEYDOWN:
        # specifying between the possible keys pressed, possible is: left, right, up, down
        if event.key == pygame.K_RIGHT:
            # prevents the snake from going backwards
            if direction == "left":
                print("cant move there")
            else:
                # setting the direction
                direction = "right"
                print("Moving right")
                # adding 10 to the countdown, so it will immediatly set the condition for the snake to be moved
                countdown = countdown + 10
        if event.key == pygame.K_LEFT:
            if direction == "right":
                print("cant move there")
            else:
                direction = "left"
                print("Moving left")
                countdown = countdown + 10
        if event.key == pygame.K_UP:
            if direction == "down":
                print("cant move there")
            else:
                direction = "up"
                print("Moving up")
                countdown = countdown + 10
        if event.key == pygame.K_DOWN:
            if direction == "up":
                print("cant move there")
            else:
                direction = "down"
                print("Moving down")
                countdown = countdown + 10

    return direction, countdown


def movement(countdown, posX, posY, direction):
    # after 10 cycles or having pressed a direction key
    if countdown > 10:
        # countdown gets reset to 0 for another run
        countdown = 0
        # sets the timetomove boolean to true so the snake can move
        timetomove = True
    else:
        # pauses the game for a 10th of a second until it cycles through again
        time.sleep(0.1)
        # sets the timetomove on false again if it was on true before
        timetomove = False
    previousPosition = [posX, posY]
    # runs when the boolean is set on true
    if timetomove:
        # runs when this is the current direction
        if direction == "right":
            # basically checking that the snake is not on the edge of the screen
            if posX <= 6:
                # letting the snake move one block in that direction
                posX = posX + 1
            else:
                # runs when the snake is on the edge of the screen and resets the position to the other side
                posX = 0
        if direction == "left":
            if posX >= 1:
                posX = posX - 1
            else:
                posX = 7
        if direction == "up":
            if posY >= 1:
                posY = posY - 1
            else:
                posY = 7
        if direction == "down":
            if posY <= 6:
                posY = posY + 1
            else:
                posY = 0
    else:
        # TODO: Remove debug
        print("Coordinates are: ", posX, posY)

    return countdown, posX, posY, previousPosition

# the main game function
def main():
    # taking win from function
    win = screen()

    # blocksize in px
    blocksize = 108
    # space between blocks in px
    block = 113
    # snake head position
    posX = 0
    posY = 0

    # 2 dimensional array saving conditions and values of every field
    gridX = 0
    gridY = 0
    Gridvalues = [[0 for x in range(8)] for y in range(8)]

    # Values:
    # 0 means empty
    # 1 means snake head
    # 2 means snake body
    # 3 means food

    # 2D array example
    # y = 2
    # x = 3
    # Matrix = [[0 for x in range(y)] for y in range(x)]
    # Matrix[2][1] = 3
    # print(Matrix[2][1])

    # game loop
    flag = True
    # initial direction
    direction = "right"
    # ingame clock
    clock = pygame.time.Clock()

    # movement countdown
    countdown = 10
    # movement boolean, if it is true the snake will move
    timetomove = False

    while flag:
        # initial screen load color
        win.fill([0, 0, 0])
        # screen loading with the specified background image on position 0, 0
        win.blit(bg, (0, 0))


        # for every even that happens
        for event in pygame.event.get():
            #print(event)

            # stores both return values from the function
            directionVal = directionCheck(event, direction, countdown)
            # splits up the both values from the array into the variables used here
            direction = directionVal[0]
            countdown = directionVal[1]

        # adding 1 to countdown after every cycle
        countdown = countdown + 1

        movementVal = movement(countdown, posX, posY, direction)
        countdown = movementVal[0]
        posX = movementVal[1]
        posY = movementVal[2]
        previousPosition = movementVal[3]

        # draws the rectangle which is actually a square
        # win is that it will be drawn in the screen
        # RGB numbers
        # block is multyplied by posX,
        # block is the pixel amount until the next block spot and posX and posY is the amount of blocks to move
        # blocksize sets the size of the block
        pygame.draw.rect(win, (255, 0, 0), ((block * posX), (block * posY), blocksize, blocksize))

        snakebody(win, block, blocksize, Gridvalues, previousPosition) # TODO: Fix the second block lagging behind instead of being a body part

        # update function
        draw_window(win)
        # the fps tick
        fps.tick(FPS)

def draw_window(win):
    # graphical updates will only then be re-rendered on the screen
    pygame.display.update()
# running main and with that the game
main()