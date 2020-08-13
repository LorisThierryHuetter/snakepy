import pygame
import neat
import time
import os
import random
import threading
import time

pygame.init()

FPS = 60
fps = pygame.time.Clock()
red = (255, 0, 0)

bg = pygame.image.load("grid.jpg")

class cube(object):
    w = 0

class snake(object):
    SIZE = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y

#def Bewegung(direction, posX, posY, countdown):
#    if countdown < 10:
#        time.sleep(0.1)
#    else:
#        if direction == "right":
#            if posX <= 6:
#                posX = posX + 1
#            else:
#                posX = 0
#        if direction == "left":
#            if posX >= 1:
#                posX = posX - 1
#            else:
#                posX = 7
#        if direction == "up":
#            if posY >= 1:
#                posY = posY - 1
#            else:
#                posY = 7
#        if direction == "down":
#            if posY <= 6:
#                posY = posY + 1
#            else:
#                posY = 0
#        countdown = 0
#        return direction, posX, posY, countdown

def main():
    # window
    WIN_WIDTH = 900
    WIN_HEIGTH = 900
    block = 113
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGTH))
    s = snake((255, 0, 0), (10, 10))
    pygame.display.set_caption("Machine learning Pygame")

    # other
    blocksize = 108
    posX = 0
    posY = 0

    flag = True

    direction = "left"

    clock = pygame.time.Clock()

    countdown = 0

    while flag:

        win.fill(red)
        win.fill([255, 255, 255])
        win.blit(bg, (0, 0))



        for event in pygame.event.get():
            print(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if direction == "left":
                        print("cant move there")
                    else:
                        direction = "right"
                        countdown = 10
                        print("Moving right")
                if  event.key == pygame.K_LEFT:
                    if direction == "right":
                        print("cant move there")
                    else:
                        direction = "left"
                        countdown = 10
                        print("Moving left")
                if  event.key == pygame.K_UP:
                    if direction == "down":
                        print("cant move there")
                    else:
                        direction = "up"
                        countdown = 10
                        print("Moving up")
                if  event.key == pygame.K_DOWN:
                    if direction == "up":
                        print("cant move there")
                    else:
                        direction = "down"
                        countdown = 10
                        print("Moving down")

            if direction == "right":
                if posX <= 6:
                    posX = posX + 1
                else:
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


        print(posX)

        countdown = countdown + 1



        pygame.draw.rect(win, (255, 0, 0), ((block * posX), (block * posY), blocksize, blocksize))

        Bewegung(direction, posX, posY, countdown)


        pygame.display.update()
        fps.tick(FPS)

def draw_window(win):
    pygame.display.update()

main()