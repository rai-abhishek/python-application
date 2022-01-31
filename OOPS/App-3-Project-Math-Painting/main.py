from classStructure import Square, Rectangle, Canvas

if __name__ == "__main__":
    canvas = Canvas(height=3500, width=3500,color=(0, 255, 255))

    r = Rectangle(20, 50, 400, 500, (100, 200, 125))
    r.draw(canvas)

    # s = Square(90,65,400,(0, 100, 222))
    # s.draw(canvas)
    canvas.make()
