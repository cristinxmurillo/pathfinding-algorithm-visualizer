from grid import Grid
from algorithms import Algorithm, Djikstra
import pygame
import time

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
    algorithm = False
    finished = False

    print('selecting obstacles')

    active = False

    while(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    active = True

            ## STATE SELECTION ##
            #  State rotation from 
            #  Obstacle Selection -> Origin Selection -> Goal Selection -> Applying pathfinding algorithm -> Restart grid
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
                        algorithm = True
                        print('applying algorithm')
                        print("Obstacles: ", obstacles)
                        print("Origin: ", origin)
                        print("Goal: ", goal)
                    elif algorithm == True:
                        algorithm = False
                    elif finished == True:
                        print('restarting...')
                        grid.drawGrid()
                        obstacles = []
                        origin = []
                        goal = []
                        finished = False
                        selectingObstacles = True
                        print('\n\nselecting obstacles')

            #When in a 'selecting' state, flag for selection or de-selection    
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
        
        #Actions for each state
        if selectingObstacles == True: 
            if activeSelecting == True:
                position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
                if position != False: position = [position[0], position[1]]
                if position != False and position not in obstacles:
                    obstacles.append(position)
                    grid.fillPosition(position, (0,0,0))
            elif deselecting == True: 
                position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
                if position != False: position = [position[0], position[1]]
                if position != False and position in obstacles:
                    obstacles.remove(position)
                    grid.fillPosition(position, (6,213,193))
        elif selectingOrigin == True:
            position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
            if position != False: position = [position[0], position[1]]
            if activeSelecting == True and position != False and origin == [] and position not in obstacles:
                origin = position
                grid.fillPosition(origin, (173, 122, 43))
            elif deselecting == True:
                if position == origin:
                    grid.fillPosition(origin, (6,213,193))
                    origin = []
        elif selectingGoal == True:
            position = grid.findMousePositionInGrid(pygame.mouse.get_pos())
            if position != False: position = [position[0], position[1]]
            if activeSelecting == True and position != False and goal == [] and position not in obstacles:
                goal = position
                grid.fillPosition(goal, (173, 81, 78))
            elif deselecting == True:
                if position == goal:
                    grid.fillPosition(goal, (6,213,193))
                    goal = []
        elif algorithm:
            djikstra = Djikstra(grid.gridSize[0], obstacles, origin, goal)
            visited = djikstra.run()
            for coordenate in visited:
                grid.fillPosition(coordenate, (173, 81, 78))
                time.sleep(0.05)
            algorithm =  False
            finished = True