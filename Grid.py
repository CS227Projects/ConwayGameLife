class Grid:
    def __init__(self, grid_size):
        self.grid = []
        for i in range(grid_size):
            self.grid.append([0] * grid_size)

    # resets the living tiles
    def clear(self):
        size = len(self.grid)
        self.grid = []
        for i in range(size):
            self.grid.append([0] * size)

    # returns the length of the board
    def get_size(self):
        return len(self.grid)

    # determines if a tile is considered living based on proximity
    # puts the new living tiles into a list and overwrites the grid with it after
    # all are checked to prevent interference of new tiles in process
    def grid_check(self):
        temp = [row[:] for row in self.grid]
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                if self.grid[i][j] == 1:
                    temp[i][j] = self.proximity_check(i, j, True)
                else:
                    temp[i][j] = self.proximity_check(i, j, False)
        self.grid = temp

    # returns true if the tile at row, col is alive.
    def is_alive(self, row, col):
        return self.grid[row][col] == 1

    # returns true if any living cells are found
    def is_life(self):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                if self.grid[i][j] == 1:
                    return True
        return False

    # counts the number of neighbors adjacent, above, below, left, and right of
    # tile at row, col
    # if living: continues living if 2 or 3 neighbors. Dies otherwise
    # if dead: revives if has 3 neighbors
    def proximity_check(self, row, col, living):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (row + i) >= 0 and (row+i) < self.get_size():
                    if (col + i) >= 0 and (col+1) < self.get_size():
                        if self.grid[i+row][j+col] == 1 and not (i == 0 and j == 0):
                            count += 1

        if living:
            if 2 <= count <= 3:
                return 1
            return 0

        if count == 3:
            return 1
        return 0

    # makes the tile at row, col living
    def set_grid(self, row, col):
        self.grid[row][col] = 1
