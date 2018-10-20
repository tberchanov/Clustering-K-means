class Point:
    x = -1.0
    y = -1.0

    def __init__(self, x = -1, y = -1):
        self.x = x
        self.y = y

    def __str__(self):
        return '({:-f}; {:-f})'.format(self.x, self.y)

    def __repr__(self):
        return str(self)