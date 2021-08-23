class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __repr__(self):
        return "pt(%r, %r)" % (self.x, self.y)

    def __add__(self, other):
        summation = Point()
        summation.x = self.x + other.x
        summation.y = self.y + other.y
        return summation
