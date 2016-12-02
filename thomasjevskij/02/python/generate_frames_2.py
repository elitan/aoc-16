import pygame
import sys
from collections import defaultdict

def draw_grid(screen, intensities):
    r = pygame.Rect(0, 0, 100, 100)
    for j in range(5):
        r.left = 0
        for i in range(5):
            c = intensities[(j, i)]
            c = sorted((0, int(c * 255 / 277), 255))[1]
            c = (c, c, c)
            pygame.draw.rect(screen, c, r, 0)
            r.left += 100
        r.top += 100
    r.left = col * 100
    r.top = row * 100
pygame.init()

intensities = defaultdict(int)

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

black = (0, 0, 0)
green = (64, 255, 64)
red = (255, 64, 64)

screen.fill(black)

functions = { 'U': lambda row, col: (row - 1, col),
              'D': lambda row, col: (row + 1, col),
              'L': lambda row, col: (row, col - 1),
              'R': lambda row, col: (row, col + 1) }

with open('input.txt') as f:
    lines = [l.strip() for l in f.readlines()]

row, col = 2, 0

p2 = []
for line in lines:
    for character in line:
        
        new_row, new_col = functions[character](row, col)
        if sum(map(abs, (2 - new_row, 2 - new_col))) < 3:
            row, col = new_row, new_col
        intensities[(row, col)] += 1
    p2.append((row, col))

print(max(intensities.values()))
draw_grid(screen, intensities)
for i, c in reversed(list(enumerate(p2))):
    pygame.draw.circle(screen, (0, int(255 / 5) * i, 0), (c[1]*100+50, c[0]*100+50), 5*(1+i))
pygame.image.save(screen, 'problem2.png')

pygame.quit()
sys.exit()
