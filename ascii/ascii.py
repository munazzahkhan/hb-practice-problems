""" 
You'll be in charge of implementing the API for drawing rectangles (and squares). The API must be able to:

  - Render canvas with a specified height and width
      - Print the canvas and any shapes to standard output
  - Add a shape to a canvas
      - shape the shape to add. For now, assume you only have to deal with rectangles
  - Clear all shapes from a canvas
  - Create a rectangle
      - start_x is the X coordinate of the upper-left-hand corner of the rectangle
      - start_y is the Y coordinate of the upper-left-hand corner of the rectangle
      - end_x is the X coordinate of the lower-right-hand corner of the rectangle
      - end_y is the Y coordinate of the lower-right-hand corner of the rectangle
      - fill_char is the character that should be used to draw the rectangle
  - Change a rectangle's fill character
      - char the character to use in order to draw a pre-existing rectangle
  - Translate (move left, right, up, or down)
      - axis which axis ('x' or 'y') should we translate the rectangle on? Translating 
        on the X-axis will cause the rectangle to move left and right. 
        Translating on the Y-axis will cause the rectangle to move up and down.
      - num is how much to move the rectangle. 
        Negative numbers will cause the rectangle to shift left or down. 
        Positive numbers will cause the rectangle to shift right or up. 
"""


def print_canvas(height, width):
    """Given height and width, print the canvas."""

    canvas = create_canvas(height, width)
    print_width(canvas)
    print_sides(canvas, width, height)
    print_width(canvas)


def create_canvas(height, width):
    canvas = []
    row = []

    i = 0
    while i < width:
        row.append("-")
        i += 1
    j = 0 
    while j < height:
        canvas.append(row)
        j += 1

    return canvas


def print_width(canvas):
    top = "".join(canvas[0])
    print(top)


def print_sides(canvas, width, height):
    i = 0
    space = ""
    while i < (width-2):
        space += " "
        i += 1
    j = 0
    while j < (height-2):
        side = "|" + space + "|"
        print(side)
        j += 1


if __name__ == "__main__":
    
    print_canvas(30, 150)