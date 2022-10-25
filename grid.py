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

if __name__ == "__main__":
    screen = pygame.display.set_mode([800, 600])
    grid = Grid(screen, [10, 10])
    grid.drawGrid()

    obstacles = []
    origin = []
    goal = []

    selectingObstacles = True
    activeSelecting = False
    deselecting = False
    selectingOrigin = False
    selectingGoal = False
    djikstra = False

    print('selecting obstacles')

    active = False

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    active = True

            if event.type == pygame.KEYUP and active == True:
                if event.key == pygame.K_SPACE:
                    active = False
                    if selectingObstacles == True:
                        selectingObstacles = False
                        selectingOrigin = True
                        print('selecting origin')
                    elif selectingOrigin == True: 
                        selectingOrigin = False
                        selectingGoal = True
                        print('selecting goal')
                    elif selectingGoal == True:
                        selectingGoal = False
                        djikstra = True
                        print('applying algorithm')
                        print("Obstacles: ", obstacles)
                        print("Origin: ", origin)
                        print("Goal: ", goal)
                    elif djikstra == True:
                        djikstra = False
                        print('restarting...')
                        grid.drawGrid()
                        obstacles = []
                        origin = []
                        goal = []
                        #restart grid
                        selectingObstacles = True
                        print('\n\nselecting obstacles')
                        
            if selectingObstacles or selectingGoal or selectingOrigin:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        activeSelecting = True
                    elif event.button == 3:
                        deselecting = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:    
                        activeSelecting = False
                    elif event.button == 3:
                        deselecting = False
        
        if selectingObstacles == True: 
            if activeSelecting == True:
                position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
                if position != False and position not in obstacles:
                    obstacles.append(position)
                    grid.fillPosition(position, (0,0,0))
            elif deselecting == True: 
                position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
                if position != False and position in obstacles:
                    obstacles.remove(position)
                    grid.fillPosition(position, (6,213,193))

        if selectingOrigin == True:
            position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
            if activeSelecting == True and position != False and origin == [] and position not in obstacles:
                origin.append(position)
                grid.fillPosition(position, (173, 122, 43))
            elif deselecting == True:
                if position in origin:
                    grid.fillPosition(position, (6,213,193))
                    origin.remove(position)

        if selectingGoal == True:
            position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
            if activeSelecting == True and position != False and goal == [] and position not in obstacles:
                goal.append(position)
                grid.fillPosition(position, (173, 81, 78))
            elif deselecting == True:
                if position in goal:
                    grid.fillPosition(position, (6,213,193))
                    goal.remove(position)