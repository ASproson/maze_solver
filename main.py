
from graphics import Window, Line, Point
from cell import Cell

def main():
  win = Window(800, 600)

  # # Create Points
  # point1 = Point(50, 50)
  # point2 = Point(200, 200)
  # point3 = Point(100, 300)

  # # Create Lines
  # line1 = Line(point1, point2)
  # line2 = Line(point2, point3)

  # # Draw Lines
  # win.draw_line(line1, "black")
  # win.draw_line(line2, "red")

  c = Cell(win)
  c.has_left_wall = False
  c.draw(50, 50, 100, 100)

  c = Cell(win)
  c.draw(125, 125, 200, 200)

  c = Cell(win)
  c.has_bottom_wall = False
  c.draw(225, 225, 250, 250)

  c = Cell(win)
  c.has_top_wall = False
  c.draw(300, 300, 500, 500)

  win.wait_for_close()

if __name__ == "__main__":
    main()