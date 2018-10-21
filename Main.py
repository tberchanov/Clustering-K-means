import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from point import Point
from point import get_points_extremums
from point import create_random_point
import numpy as np

# Only for system, where need absolute path
PATH_PREFIX = "/home/anatoly/Desktop/Clustering/"
FILE_NAME = "s2.txt"

def read_file(fileName):
    file = open(FILE_NAME,"r", encoding='windows-1251')
    lines = file.readlines()
    file.close()
    return lines

def convert_lines_to_points(lines):
    points = list()
    for line in lines:
        line = line.replace("\n", "")
        point = convert_line_to_point(line)
        points.append(point)
    return points

def convert_line_to_point(line):
    point = Point()
    for i in line.split(" "):
        i = i.strip()

        # is empty
        if (not i):
            continue

        coordinate = float(i)
        if (point.x == -1):
            point.x = coordinate
        else:
            point.y = coordinate
        
    return point

def show_points_plot(points, centroids, add_picker):
    xx = list()
    yy = list()
    for point in points:
        xx.append(point.x)
        yy.append(point.y)
        
    if add_picker:
        blue_point, = plt.plot(xx, yy, '.', zorder=-1, picker=line_picker)
    else:
        blue_point, = plt.plot(xx, yy, '.', zorder=-1)

    xx_c = list()
    yy_c = list()
    for centroid in centroids:
        xx_c.append(centroid.x)
        yy_c.append(centroid.y)
    red_point, = plt.plot(xx_c, yy_c, 'ro')

    plt.legend([blue_point, red_point], ["Point", "Centroid"])
    
    plt.show()

def line_picker(line, mouseevent):
    x = mouseevent.xdata
    y = mouseevent.ydata
    centroids.append(Point(x, y))

    plt.scatter(x, y, c='red')
    plt.pause(0.05)
    return False, dict()

def show_menu():
    print("0. Exit")
    print("1. Show plot")
    print("2. Add random centroids")
    print("3. Add centroid")
    # print("4. Cluster")

def generate_random_centroids(points, centroids):
    count = input("Count: ")
    
    if count.isdigit():
        count = int(count)
    else:
        print("Invalid count!")
        return
    
    points_extremums = get_points_extremums(points)
    max_x = points_extremums["max_x"]
    max_y = points_extremums["max_y"]
    for i in range(count):
        rand_point = create_random_point(0, max_x, 0, max_y)
        centroids.append(rand_point)

def add_centroid(centroids):
    x = input("X: ")
    y = input("Y: ")
    x = float(x)
    y = float(y)
    centroids.append(Point(x, y))

def onpick(event):
    print('onpick point:', event.xdata, event.ydata)

# begin

lines = read_file(FILE_NAME)
points = convert_lines_to_points(lines)
centroids = list()

isFinished = False
while not isFinished:
    show_menu()
    command = input("Command: ")
    if command.isdigit():
        command = int(command)
    
    if command == 0:
        isFinished = True
    elif command == 1:
        show_points_plot(points, centroids, False)
    elif command == 2:
        generate_random_centroids(points, centroids)
    elif command == 3:
        # add_centroid(centroids)
        show_points_plot(points, centroids, True)
    # elif command == 4:
    #     show_points_plot(points, centroids, True)
    else:
        print("Incorrect command!")
    
    print("- - - - - - - - - - - - -")