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

        pygame.draw.rect(self.screen, blue, [self.padding, self.padding, (self.size - self.padding * 2),  (self.size - self.padding * 2)])

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

        if x > 10 or x < 1 and y > 10 or y < 1:
            return False

        return(x,y)

    def fillPosition(self, position, color):
        pygame.draw.rect(self.screen, color, [((position[0] - 1) * self.stepSize + self.padding), ((position[1] - 1) * self.stepSize  + self.padding), (self.stepSize), (self.stepSize) ] )
        pygame.display.update()

if __name__ == "__main__":
    screen = pygame.display.set_mode([800, 600])
    grid = Grid(screen, [10, 10])
    grid.drawGrid()

    obstacles = []
    selectingObstacles = False

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            selectingObstacles = True
        if event.type == pygame.MOUSEBUTTONUP:
            selectingObstacles = False
        
        if selectingObstacles == True:
            position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
            if position not in obstacles:
                obstacles.append(position)
                grid.fillPosition(position, (0,0,0))
                print(obstacles)