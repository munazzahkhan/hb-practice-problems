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

# Ashley Trinh's Solution

"""ASCII graphics library."""


class Canvas:
    """A canvas can store shapes and render them to the screen.

    Attributes:
        - elements (list): A list of shapes and other elements
          that have been added to the canvas
        - width (int): The width of the canvas
        - height (int): The height of the canvas
    """

    def __init__(self, width, height):
        """Initialize a canvas.

        Return:
            None
        """

        self.elements = []
        self.width = width
        self.height = height

    def _update_data(self):
        """Update the characters in self._data

        Return:
            None
        """

        data = [
                [
                    None for _ in range(self.width)
                ]
                for _ in range(self.height)
            ]

        for element in self.elements:
            # TODO: this assumes that all 'elements' will be rendered
            # the same way. But what about circles, lines, etc.? We likely 
            # won't be able to use the same algorithm for any of those
            # types of shapes.
            #
            # Instead it's probably a better idea to give each type of
            # shape its own render method and have the canvas call it
            for x in range(element.start_x, element.end_x + 1):
                for y in range(element.start_y, element.end_y + 1):
                    if 0 <= x < self.width and 0 <= y < self.height:
                        data[y][x] = element.fill_char

        return data

    def add(self, shape):
        """Add a shape to the canvas.

        Arguments:
            - shape (Shape): The shape to add

        Return:
            None
        """

        if not isinstance(shape, Shape):
            raise TypeError(
                f'Canvas.add is not supported with type \'{type(shape)}\''
            )

        self.elements.append(shape)

    def clear(self):
        """Clear all shapes from the canvas."""

        self.elements = []

    def render(self):
        """Render the contents of the canvas.

        Contents are rendered to standard output.
        """

        for row in self._update_data():
            print(''.join([ch or ' ' for ch in row]))


class Shape:
    """An abstract class that all shapes should inherit from.
    
    We should probably have every shape inherit start_x, start_y,
    end_x, and end_y, but due to an abundance of caution, I'll
    leave it open-ended until we're sure that all shapes will
    share these attributes.
    """


class Rectangle(Shape):
    """A rectangle.

    Attributes:
        - start_x (int): The x-coordinate for the top left corner of
          the rectangle
        - start_y (int): The y-coordinate for the top left corner of
          the rectangle
        - end_x (int): The x-coordinate for the bottom right corner
          of the rectangle
        - end_y (int): The y-coordinate for the bottom right corner
          of the rectangle
        - fill_char (str): The character used to fill the rectangle
    """

    def __init__(self,
                 start_x: int,
                 start_y: int,
                 end_x: int,
                 end_y: int,
                 fill_char: str) -> None:
        """Initialize a rectangle.

        Arguments:
            - start_x (int): The x-coordinate for the top left corner of
            the rectangle
            - start_y (int): The y-coordinate for the top left corner of
            the rectangle
            - end_x (int): The x-coordinate for the bottom right corner
            of the rectangle
            - end_y (int): The y-coordinate for the bottom right corner
            of the rectangle
            - fill_char (str): The character used to fill the rectangle

        Return:
            None
        """

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

    def set_fill_char(self, char):
        """Update the fill character.

        Arguments:
            - char (str): The new fill char

        Return:
            None
        """

        self.fill_char = char

    def translate(self, axis, num):
        """Translate the rectangle.

        Arguments:
            - axis (str): Either 'x' or 'y'
            - num (int): A positive or negative integer

        Return:
            None
        """

        if axis not in ('x', 'y'):
            raise TypeError('First argument must be one of (\'x\', \'y\')')

        if axis == 'x':
            self.start_x += num
            self.end_x += num
        elif axis == 'y':
            self.start_y += num
            self.end_y += num