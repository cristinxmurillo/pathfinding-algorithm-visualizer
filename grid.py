from numpy import empty
import pygame
import math

class Grid:
    def __init__(self, screen, gridSize):
        self.gridSize = gridSize
        self.screen = screen
        self.size = 600
        self.padding = 20
        self.stepSize = (self.size - self.padding * 2)/self.gridSize[0]
        pygame.display.set_caption("Pathfinding algorithm visualizer")
     
    def getStepSizes(self):
        #Grid will always be (600px, 600px) with padding of 20px
        horizontalStepSize = (self.size - self.padding * 2)/self.gridSize[0]
        verticalStepSize = (self.size - self.padding * 2)/self.gridSize[1]
        
        return [horizontalStepSize, verticalStepSize]

    def drawGrid(self):   
        # color palette
        black = (0, 0, 0)
        white = (255, 255, 255)
        blue = (159, 172, 230)

        horizontalStepSize, verticalStepSize = self.getStepSizes()
        
        self.screen.fill(white)

        pygame.draw.rect(self.screen, (6,213,193), [self.padding, self.padding, (self.size - self.padding * 2),  (self.size - self.padding * 2)])

        # grid drawing
        # vertical lines 
        for i in range(0, self.gridSize[0] + 1):
            pygame.draw.line(self.screen, black, (self.padding + horizontalStepSize * i, self.padding), (self.padding + horizontalStepSize * i, self.size - self.padding), 1)
        for i in range(0, self.gridSize[0] + 1):
            pygame.draw.line(self.screen, black, (self.padding, self.padding + verticalStepSize * i), (self.size - self.padding, self.padding + verticalStepSize * i), 1)

        pygame.display.update()

    def findMousePositionInGrid(self, mousePosition):
        # positions in grid 20 - 580
        position = [mousePosition[0] - 20, mousePosition[1] - 20]

        x = math.floor(position[0]/((self.size - self.padding)/ self.gridSize[0])) + 1
        y = math.floor(position[1]/((self.size - self.padding)/ self.gridSize[1])) + 1

        if (x > self.gridSize[0] or x < 1) or (y > self.gridSize[1] or y < 1):
            return False

        return(x,y)

    def fillPosition(self, position, color):
        pygame.draw.rect(self.screen, color, [((position[0] - 1) * self.stepSize + self.padding) + 1, ((position[1] - 1) * self.stepSize  + self.padding) + 1, (self.stepSize) - 1, (self.stepSize) - 1] )
        pygame.display.update()