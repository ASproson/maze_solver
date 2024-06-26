from graphics import Line, Point

class Cell():
  def __init__(self, win = None):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._x2 = None
    self._y1 = None
    self._y2 = None
    self._win = win
    self.visited = False

  def draw(self, x1, y1, x2, y2):
      self._x1 = x1
      self._x2 = x2
      self._y1 = y1
      self._y2 = y2

      wall_color = lambda has_wall: "black" if has_wall else "white"
      
      # Left wall
      line = Line(Point(x1, y1), Point(x1, y2))
      self._win.draw_line(line, wall_color(self.has_left_wall))
      
      # Top wall
      line = Line(Point(x1, y1), Point(x2, y1))
      self._win.draw_line(line, wall_color(self.has_top_wall))
      
      # Right wall
      line = Line(Point(x2, y1), Point(x2, y2))
      self._win.draw_line(line, wall_color(self.has_right_wall))
      
      # Bottom wall
      line = Line(Point(x1, y2), Point(x2, y2))
      self._win.draw_line(line, wall_color(self.has_bottom_wall))

  def draw_move(self, to_cell, undo = False):
    curr_x = (self._x1 + self._x2) / 2
    curr_y = (self._y1 + self._y2) / 2

    target_x = (to_cell._x1 + to_cell._x2) / 2
    target_y = (to_cell._y1 + to_cell._y2) / 2

    fill_color = "red"
    if undo:
       fill_color = "gray"

    line = Line(Point(curr_x, curr_y), Point(target_x, target_y))
    self._win.draw_line(line, fill_color)
