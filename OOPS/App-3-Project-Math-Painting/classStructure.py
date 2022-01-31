import numpy as np
from PIL import Image


class Square:
    """
    class to create objects for square
    """

    def __init__(self, x, y, side, color):
        self.y = y
        self.x = x
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:
    """
    class to create objects for rectangle
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Canvas:
    """
    classes to draw shapes
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # create a 3D numpy of zeros.
        self.data = np.zeros((5, 4, 3), dtype=np.uint8)
        # change color to user provided value
        self.data[:] = self.color

    def make(self):
        # convert the current array into image
        img = Image.fromarray(self.data, 'RGB')
        img.show()

