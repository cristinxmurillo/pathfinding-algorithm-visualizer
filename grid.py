import pygame

class Grid:

    # color palette
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (159, 172, 230)
    red = (255, 0, 0)

    def __init__(self, screen, gridSize):
        self.gridSize = gridSize
        self.screen = screen
        self.size = 600
        self.padding = 20
        pygame.display.set_caption("Pathfinding algorithm visualizer")
     
    def getStepSizes(self):
        #Grid will always be (600px, 600px) with padding of 20px
        horizontalStepSize = (self.size - self.padding * 2)/self.gridSize[0]
        verticalStepSize = (self.size - self.padding * 2)/self.gridSize[1]
        
        return [horizontalStepSize, verticalStepSize]

    def drawGrid(self):
        
        horizontalStepSize, verticalStepSize = self.getStepSizes()
        
        self.screen.fill(grid.white)

        pygame.draw.rect(self.screen, grid.blue, [self.padding, self.padding, (self.size - self.padding * 2),  (self.size - self.padding * 2)])

        # grid drawing
        # vertical lines 
        for i in range(0, self.gridSize[0] + 1):
            pygame.draw.line(self.screen, grid.black, (self.padding + horizontalStepSize * i, self.padding), (self.padding + horizontalStepSize * i, self.size - self.padding), 1)
        for i in range(0, self.gridSize[0] + 1):
            pygame.draw.line(self.screen, grid.black, (self.padding, self.padding + verticalStepSize * i), (self.size - self.padding, self.padding + verticalStepSize * i), 1)

        pygame.display.update()
        
if __name__ == "__main__":
    screen = pygame.display.set_mode([800, 600])
    grid = Grid(screen, [5, 5])
    grid.drawGrid()

    while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()