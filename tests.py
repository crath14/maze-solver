import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols = 12
        rows = 10
        maze1 = Maze(0,0, rows, cols, 10, 10)
        self.assertEqual(
            len(maze1.cells),
            cols
        )
        self.assertEqual(
            len(maze1.cells[0]),
            rows
        )
    
    def test_zero_rows(self):
        m = Maze(0,0,0,5,10,10)
        self.assertEqual(len(m.cells), 5)
        for col in m.cells:
            self.assertEqual(len(col), 0)


if __name__ == "__main__":
    unittest.main()