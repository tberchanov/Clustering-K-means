import matplotlib.pyplot as plt
from point import Point
from point import get_points_extremums
from point import create_random_point


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

def show_points_plot(points):
    xx = list()
    yy = list()
    for point in points:
        xx.append(point.x)
        yy.append(point.y)
    plt.plot(xx, yy, '.')
    plt.show()

def show_menu():
    print("0. Exit")
    print("1. Show plot")
    print("2. Add random points")
    # print("3. Add point")
    # print("4. Cluster")

def generate_random_points():
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
        points.append(rand_point)

# begin

lines = read_file(FILE_NAME)
points = convert_lines_to_points(lines)

isFinished = False
while not isFinished:
    show_menu()
    command = input("Command: ")
    if command.isdigit():
        command = int(command)
    
    if command == 0:
        isFinished = True
    elif command == 1:
        show_points_plot(points)
    elif command == 2:
        generate_random_points()
    # elif command == 3:
    #     show_plot(spam_tupples[:20], "Top 20 spam words")
    # elif command == 4:
    #     show_plot(ham_tupples[:20], "Top 20 ham words")
    else:
        print("Incorrect command!")
    
    print("- - - - - - - - - - - - -")