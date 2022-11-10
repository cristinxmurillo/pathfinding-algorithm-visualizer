from numpy import empty
from pyparsing import original_text_for


class Algorithm:
    def __init__(self, gridSize, obstacles, origin, goal) -> None:
        self.gridSize = gridSize
        self.obstacles = obstacles
        self.origin = origin
        self.goal = goal

class Djikstra(Algorithm):
    def run(self):
        Q = [] 
        visited = []

        Q.append(self.origin)

        while Q != []:
            current = Q[0]
            currentNeighbors = [[current[0] + 1, current[1]], [current[0] - 1, current[1]], [current[0], current[1] + 1], [current[0], current[1] - 1]]
            for neighbor in currentNeighbors:
                if (neighbor[0] >= 1 and neighbor[0] <= self.gridSize) and (neighbor[1] >= 1 and neighbor[1] <= self.gridSize):
                    if neighbor not in visited and neighbor not in Q and neighbor not in self.obstacles:
                        Q.append(neighbor)
            
            if Q[0] == self.goal:
                return visited
            
            visited.append(Q.pop(0))
        return visited


if __name__ == "__main__": 
    obstacles = [[2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9]]
    origin = [5, 10]
    goal = [5, 8]
    print(Djikstra(10, obstacles, origin, goal).run())

