import random
import time

class Grid(object):
    grid = []
    alive = '▇'
    dead  = '‏‏‎　'

    def __init__(self, dimension: int = 3):

        if (dimension < 3): # minimum grid size
            dimension = 3

        self.grid = self.random_init(dimension)
                
    def random_init(self, dimension):
        grid = []

        for _ in range(dimension):
            cells = []

            for _ in range(dimension):
                cells.append(random.choice([self.alive, self.dead]))

            grid.append(cells)

        return grid

    def init(self, dimension):
        grid = []

        for _ in range(dimension):
            cells = []

            for _ in range(dimension):
                cells.append(self.alive)

            grid.append(cells)
            
        return grid


    def display(self):
        for row in range(0, len(self.grid)):
            print(*self.grid[row], sep = self.dead)

    def count_neighbors(self, y, x):
        neighbors = 0

        for row in range(y-1, y+2):
            
            if (row < 0 or row > len(self.grid)-1):
                continue

            for col in range(x-1, x+2):
                
                if (col < 0 or (col == x and row == y) or col > len(self.grid)-1):
                    continue
                
                
                if (self.grid[row][col] == self.alive):
                    neighbors += 1

        return neighbors

    def change_state(self, y, x):
        neighbors = self.count_neighbors(y, x)
        
        if (self.grid[y][x] == self.alive):
            if (neighbors < 2):
                self.grid[y][x] = self.dead

            if (neighbors > 3):
                self.grid[y][x] = self.dead
        else:
            if (neighbors == 3):
                self.grid[y][x] = self.alive
    
    def simulate(self, generations = 1):
        length = len(self.grid)

        for _ in range(generations):
            for row in range(length):
                for col in range(length):
                    self.change_state(row, col)
    
        
    def grid_to_string(self):
        string_grid = ''
        for row in range(len(self.grid)):

            for col in range(len(self.grid)):

                string_grid += self.grid[row][col] + self.dead

            string_grid += '\n'

        return string_grid
