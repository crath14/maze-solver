from cell import Cell
import time
import random


class Maze:
    def __init__(
            self, 
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window = None,
            seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        

        if seed:
            random.seed(seed)

        self.create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell(self.window)
                column.append(cell)
            self.cells.append(column)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.draw_cell(i,j)
    
    def draw_cell(self, i, j):
        if self.window is None:
            return
        cell_x1 = self.cell_size_x * i +self.x1
        cell_y1 = self.cell_size_y * j + self.y1
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y

        self.cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        
        self.animate()

    def animate(self):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(0.05)
    
    def __break_entrance_and_exit(self):
        if self.num_rows == 0 or self.num_cols == 0:
            return
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0,0)
        self.cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self.draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            next_index_list = []

            if i > 0 and not self.cells[i - 1][j].visited: #left
                next_index_list.append((i - 1, j))
            
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited: #right
                next_index_list.append((i + 1, j))
           
            if j > 0 and not self.cells[i][j - 1].visited: #up
                next_index_list.append((i, j - 1))
            
            if j < self.num_rows -1 and not self.cells[i][j + 1].visited: # down
                next_index_list.append((i, j + 1))
            
            if len(next_index_list) == 0:
                self.draw_cell(i,j)
                return
            
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            if next_index[0] == i + 1:              #right cell
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
            if next_index[0] == i - 1:              #left cell
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:              #down cell
                self.cells[i][j + 1].has_top_wall = False
                self.cells[i][j].has_bottom_wall = False
            if next_index[1] == j - 1:              #up cell
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False
            
            self.__break_walls_r(next_index[0], next_index[1])
    
    def __reset_cells_visited(self):
        for column in self.cells:
            for cell in column:
                cell.visited = False