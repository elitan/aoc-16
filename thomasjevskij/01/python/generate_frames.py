import numpy as np
import pygame
import sys

pygame.init()

size = width, height = 300, 350
screen = pygame.display.set_mode(size)
offsets = o_x, o_y = 50, 256

white = (255, 255, 255)
green = (64, 255, 64)
black = (0, 0, 0)

screen.fill(black)

with open('input.txt') as f:
    instructions = f.readline().split(', ')
    
rotations = { 'L': np.mat('0, -1; 1, 0'), 'R': np.mat('0, 1; -1, 0') }
direction = np.array([0, 1])
direction.shape = (2, 1)
position = np.array([0, 0])
position.shape = (2, 1)    
position2 = np.array([0, 0])
position2.shape = (2, 1)

visited = set()
visited.add((position2[0, 0] + o_x, o_y - position2[1, 0]))

i = 0
done = False
for instruction in instructions:
    p1_0 = (position[0, 0] + o_x, o_y - position[1, 0])
    
    direction = np.matmul(rotations[instruction[0]], direction)         
    position += int(instruction[1:]) * direction
    p1_1 = (position[0, 0] + o_x, o_y - position[1, 0])

    pygame.draw.line(screen, white, p1_0, p1_1)
    pygame.image.save(screen, 'frames/frame{0:03d}.png'.format(i))
    i += 1

    if not done:
        for ii in range(int(instruction[1:])):
            p2_0 = (position2[0, 0] + o_x, o_y - position2[1, 0])
            position2 += direction
            p2_1 = (position2[0, 0] + o_x, o_y - position2[1, 0])
            if p2_1 in visited:
                done = True
                pygame.draw.line(screen, green, p2_0, p2_1)
                pygame.image.save(screen, 'frames/frame{0:03d}.png'.format(i))
                break
            else:
                visited.add(p2_1)
                pygame.draw.line(screen, green, p2_0, p2_1)
                pygame.image.save(screen, 'frames/frame{0:03d}.png'.format(i))
            
            i += 1
    

#pygame.draw.line(screen, black, (0, 0), (256, 256))

pygame.image.save(screen, 'test.png')

pygame.quit()
sys.exit()
