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

    def test_entrance_exit(self):
        m = Maze(0,0,5,5,10,10)
        self.assertFalse(m.cells[0][0].has_top_wall)
        self.assertFalse(m.cells[4][4].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()