import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    #def test_maze_create_cells(self):
     #   cols = 12
      #  rows = 10
       # maze1 = Maze(0,0, rows, cols, 10, 10)
        #self.assertEqual(
         #   len(maze1.cells),
          #  cols
        #)
        #self.assertEqual(
         #   len(maze1.cells[0]),
          #  rows
        #)
    
    #def test_zero_rows(self):
       # m = Maze(0,0,0,5,10,10)
        #self.assertEqual(len(m.cells), 5)
        #for col in m.cells:
            #self.assertEqual(len(col), 0)

    #def test_entrance_exit(self):
        #m = Maze(0,0,5,5,10,10)
        #self.assertFalse(m.cells[0][0].has_top_wall)
        #self.assertFalse(m.cells[4][4].has_bottom_wall)
    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1.cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()