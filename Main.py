import matplotlib.pyplot as plt
from point import Point

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



def show_menu():
    print("0. Exit")
    print("1. Show plot")
    print("2. Add random point")
    print("3. Add point")
    print("4. Cluster")

# begin

lines = read_file(FILE_NAME)
points = convert_lines_to_points(lines)
print(points)

# print(point)

isFinished = True
while not isFinished:
    show_menu()
    command = input("Command: ")
    if command.isdigit():
        command = int(command)
    
    if command == 0:
        isFinished = True
    elif command == 1:
        print(spam_tupples)
    elif command == 2:
        print(ham_tupples)
    elif command == 3:
        show_plot(spam_tupples[:20], "Top 20 spam words")
    elif command == 4:
        show_plot(ham_tupples[:20], "Top 20 ham words")
    elif command == 5:
        message = input("Message: ")
        check_message(message)
    else:
        print("Incorrect command!")
    
    print("- - - - - - - - - - - - -")