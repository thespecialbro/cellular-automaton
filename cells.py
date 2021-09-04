# Cellular automaton framework type thing:
# grid of cells;
# each cell consists of at least two states, stored as an integer
# eg: 1 and 0 being alive and dead
# state 0 is always the default state (such as dead for conway's gol)

def sum_array(array):
        # get the sum of all the elements in an array
        sum = 0;
        for n in array:
            sum += n;
        return sum

class Cell:
    def __init__(self, state):
        self.default_state = 0
        self.state = state
        self.next_state = self.default_state

    def set_state(self, neighbor_states):
        # neighbor_states is set up as a 1d array of the relevant neighbors
        # in the order of top left to bottom right
        # for things like conway's gol the order doesn't matter
        if(neighbor_states != None):
            sum = sum_array(neighbor_states)
            #print('sum = ', sum)
            if sum < 2 or sum > 3:
                self.next_state = 0
            else:
                if self.state == 0 and sum == 3 or self.state == 1:
                    self.next_state = 1
                else:
                    self.next_state = 0
        else:
            print("error getting neighbors")
            self.next_state = self.default_state

    def update(self):
        self.state = self.next_state
        self.next_state = self.default_state
# END OF CELL CLASS ==========================

class Grid:
    def __init__(self, grid=None, w=5, h=5):
        if grid == None:
            self.width = w
            self.height = h
            self.grid = [[Cell(0) for _ in range(w)] for _ in range(h)]
        else:
            self.generate_grid_from_array(grid)

    def get_neighbors(self, x, y):
        # get the neighbor_states array based on the xy coords in the grid
        # neighbor array indexes are mapped as follows:
        # 0 1 2
        # 3   4
        # 5 6 7

        neighbors = [0] * 8
        if y >= self.height or x >= self.width:
            return None
        else: # this is a lot longer than the messy version, but it's readable at least
            non_excluded = [1] * 8
            if x == 0: # exclude 0, 3, 5 (left edge) from search
                non_excluded[0] = 0
                non_excluded[3] = 0
                non_excluded[5] = 0

            if x == self.width - 1: # exclude 2, 4, 7 (right edge)
                non_excluded[2] = 0
                non_excluded[4] = 0
                non_excluded[7] = 0

            if y == 0: # exclude 0, 1, 2 (top edge)
                non_excluded[0] = 0
                non_excluded[1] = 0
                non_excluded[2] = 0

            if y == self.height - 1: # exclude 5, 6, 7 (bottom edge)
                non_excluded[5] = 0
                non_excluded[6] = 0
                non_excluded[7] = 0

            n_x = -1 # relative x coord
            n_y = -1 # relative y coord
            for i in range(8):
                if(non_excluded[i] == 1):
                    neighbors[i] = self.grid[y+n_y][x+n_x].state

                # get relative coords based on index i
                n_x += 1
                if n_x == 2:
                    n_x = -1
                    n_y += 1
                if n_x == 0 and n_y == 0:
                    n_x += 1

            return neighbors

    def generate_grid_from_array(self, grid_in):
        # generate a grid of cells from a 2d array of integers
        # representing the cell states
        self.height = len(grid_in)
        self.width = len(grid_in[0])
        grid_out = [[Cell(0) for _ in range(self.width)] for _ in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                grid_out[i][j].state = grid_in[i][j]
        self.grid = grid_out

    def step(self):
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j].set_state(self.get_neighbors(j, i))

        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j].update()

    def print_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                print('#' if self.grid[i][j].state else '.', end=' ')
            print()
# END OF GRID CLASS ==========================

if __name__ == '__main__':
    # Gosper glider gun example
    cells = Grid(grid=
            [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        )

    step_count = 0
    while(step_count < 100):
        print('==================', step_count)
        cells.print_grid()
        cells.step()
        step_count += 1
        
    print('==================', step_count)
    cells.print_grid()
