from grid import Grid
import pygame

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
            if position != False and position not in obstacles:
                obstacles.append(position)
                grid.fillPosition(position, (0,0,0))