import random
import math

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

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return (self.x == other.x) and (self.y == other.y)

def get_points_extremums(points):
    if not points:
        print("List is empty")
        return
    
    min_x = points[0].x
    max_x = points[0].x
    min_y = points[0].y
    max_y = points[0].y
    
    for point in points:
        if point.x < min_x:
            min_x = point.x
        if point.x > max_x:
            max_x = point.x

        if point.y < min_y:
            min_y = point.y
        if point.y > max_y:
            max_y = point.y

    return {"min_x" : min_x, "max_x" : max_x,
            "min_y" : min_y, "max_y" : max_y}

def create_random_point(min_x, max_x, min_y, max_y):
    rand_x = random.randint(min_x, max_x - 1) + random.random()
    rand_y = random.randint(min_y, max_y - 1) + random.random()
    return Point(rand_x, rand_y)

def calculate_distance(p1, p2):
    return math.sqrt(math.pow(p1.x - p2.x, 2) +
                     math.pow(p1.y - p2.y, 2))