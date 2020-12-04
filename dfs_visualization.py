import pygame
from pygame.draw import line, rect
from pygame.time import Clock
import numpy
import random

width, height = 720, 480
rez = 20
rows = height // rez
cols = width // rez

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Depth First Search')

grid = []


class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.neighbours = []

    def draw(self):
        if self.visited == False:
            rect(display, (220, 220, 220), (self.x * rez, self.y * rez, rez, rez))
        else:
            rect(display, (220, 100, 220), (self.x * rez, self.y * rez, rez, rez))

    def visit(self):
        self.visited = True

    def unvisit(self):
        self.visited = False

    def update_neighbours(self):
        if self.x - 1 > -1:
            self.neighbours.append(grid[self.x - 1][self.y])

        if self.x + 1 < cols:
            self.neighbours.append(grid[self.x + 1][self.y])

        if self.y - 1 > -1:
            self.neighbours.append(grid[self.x][self.y - 1])

        if self.y + 1 < rows:
            self.neighbours.append(grid[self.x][self.y + 1])


for i in range(cols):
    grid.append([])
    for j in range(rows):
        grid[i].append(Node(i, j))


def draw_grid():
    for i in range(rez, width, rez):
        for j in range(rez, height, rez):
            line(display, (51, 51, 51), (i, 0), (i, height), 2)
            line(display, (51, 51, 51), (0, j), (width, j), 2)


def dfs(grid, node):
    node.visit()
    node.update_neighbours()
    draw(grid, node)
    for n in node.neighbours:
        if not n.visited:
            dfs(grid, n)


def draw(grid, node):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j].draw()

    rect(display, (90, 90, 220), (node.x * rez, node.y * rez, rez, rez))
    draw_grid()
    pygame.display.flip()


def main():
    run = True
    start_node = grid[5][5]
    clock = Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        dfs(grid, start_node)
        # start_node.visit()
        # start_node.update_neighbours()
        # for neighbor in start_node.neighbours:
        #     if not neighbor.visited:
        #         start_node = neighbor

        pygame.display.flip()


if __name__ == "__main__":
    main()
