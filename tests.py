import unittest

from maze import Maze

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    self.assertEqual(len(m1._cells), num_cols)
    self.assertEqual(len(m1._cells[0]), num_rows)

  def test_maze_create_cells_small(self):
    num_cols = 2
    num_rows = 2
    m2 = Maze(0, 0, num_rows, num_cols, 4, 4)
    self.assertEqual(len(m2._cells), num_cols)
    self.assertEqual(len(m2._cells[0]), num_rows)

  def test_maze_create_cells_xl(self):
    num_cols = 24
    num_rows = 12
    m2 = Maze(0, 0, num_rows, num_cols, 4, 4)
    self.assertEqual(len(m2._cells), num_cols)
    self.assertEqual(len(m2._cells[0]), num_rows)


if __name__ == "__main__":
  unittest.main()