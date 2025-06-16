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
            window = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []
        
        self.create_cells()
    
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
    