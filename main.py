from grid import Grid
import pygame

if __name__ == "__main__":
    screen = pygame.display.set_mode([800, 600])
    grid = Grid(screen, [5, 5])
    grid.drawGrid()

    while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   