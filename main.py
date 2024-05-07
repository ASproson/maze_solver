
from graphics import Window, Line, Point

def main():
  win = Window(800, 600)

  # Create Points
  point1 = Point(50, 50)
  point2 = Point(200, 200)
  point3 = Point(100, 300)

  # Create Lines
  line1 = Line(point1, point2)
  line2 = Line(point2, point3)

  # Draw Lines
  win.draw_line(line1, "black")
  win.draw_line(line2, "red")

  win.wait_for_close()

if __name__ == "__main__":
    main()