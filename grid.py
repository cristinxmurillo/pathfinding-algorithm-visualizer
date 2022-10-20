import pygame

def drawGrid(gridSize):

    # color palette
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (159, 172, 230)
    red = (255, 0, 0)

    # display configs
    size = 600
    padding = 20
    horizontalStepSize = (size - padding * 2)/gridSize[0]
    verticalStepSize = (size - padding * 2)/gridSize[1]
    screen = pygame.display.set_mode([size, size], pygame.RESIZABLE)
    pygame.display.set_caption("Pathfinding algorithm visualizer")
    screen.fill(white)

    pygame.draw.rect(screen, blue, [padding, padding, (size - padding * 2),  (size - padding * 2)])

    # grid drawing
    # vertical lines 
    for i in range(0, gridSize[0] + 1):
        pygame.draw.line(screen, black, (padding + horizontalStepSize * i, padding), (padding + horizontalStepSize * i, size - padding), 1)
    for i in range(0, gridSize[0] + 1):
        pygame.draw.line(screen, black, (padding, padding + verticalStepSize * i), (size - padding, padding + verticalStepSize * i), 1)

    pygame.display.update()
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

if __name__ == "__main__":
    drawGrid([100, 100])