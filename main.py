
from graphics import Window, Line, Point
from cell import Cell

def main():
  win = Window(800, 600)

    # Create cells
  cell1 = Cell(win)
  cell1.draw(50, 50, 100, 100)

  cell2 = Cell(win)
  cell2.draw(125, 125, 200, 200)

  cell3 = Cell(win)
  cell3.draw(225, 225, 250, 250)

  cell4 = Cell(win)
  cell4.draw(300, 300, 500, 500)

  # Draw lines between cells
  cell1.draw_move(cell2)
  cell2.draw_move(cell3)
  cell3.draw_move(cell4, undo=True)  # Test undo flag

  win.wait_for_close()

if __name__ == "__main__":
    main()