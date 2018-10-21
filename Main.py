import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from point import Point
from point import get_points_extremums
from point import create_random_point
from point import calculate_distance
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
    print("4. Cluster")

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

def clusterization(points, centroids):
    clusters_dic = cluster_K_means(points, centroids)
    show_clusterization_result(clusters_dic)

def show_clusterization_result(clusters_dic):
    for points in clusters_dic.values():
        xx = list()
        yy = list()
        for point in points:
            xx.append(point.x)
            yy.append(point.y)
        plt.plot(xx, yy, '.')

    centroids = clusters_dic.keys()
    xx_c = list()
    yy_c = list()
    for centroid in centroids:
        xx_c.append(centroid.x)
        yy_c.append(centroid.y)
        plt.plot(xx_c, yy_c, 'ro')

    plt.show()

def cluster_K_means(points, centroids):
    while True:
        clusters_dic = split_by_centroids(points, centroids)
        normalized_centroids = get_normalized_centroids(clusters_dic)

        if centroids == normalized_centroids:
            return clusters_dic
        else:
            centroids = normalized_centroids

def get_normalized_centroids(clusters_dic):
    norm_centroids = list()
    for points in clusters_dic.values():
        norm_centroid = get_normalized_centroid(points)
        norm_centroids.append(norm_centroid)
    return norm_centroids

def get_normalized_centroid(points):
    norm_x = 0
    norm_y = 0
    for point in points:
        norm_x += point.x
        norm_y += point.y
    norm_x = norm_x / len(points)
    norm_y = norm_y / len(points)

    return Point(norm_x, norm_y)

def split_by_centroids(points, centroids):
    clusters_dic = dict()
    for centroid in centroids:
        clusters_dic[centroid] = list()

    for point in points:
        closer_centroid = centroids[0]
        closer_centroid_distance = calculate_distance(point, closer_centroid)
        for centroid in centroids:
            distance = calculate_distance(point, centroid)
            if distance < closer_centroid_distance:
                closer_centroid_distance = distance
                closer_centroid = centroid
        
        clusters_dic[closer_centroid].append(point)

    return clusters_dic

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
        choose_dots_in_chart = True
        if choose_dots_in_chart:
            show_points_plot(points, centroids, True)
        else:
            add_centroid(centroids)
    elif command == 4:
        clusterization(points, centroids)
    else:
        print("Incorrect command!")
    
    print("- - - - - - - - - - - - -")