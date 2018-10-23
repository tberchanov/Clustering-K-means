import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from point import Point
from point import get_points_extremums
from point import create_random_point
from point import calculate_distance
import numpy as np
import os

DATA_FILES_DIR = "./Data"

def read_file(fileName):
    fileName = DATA_FILES_DIR + '/' + fileName
    file = open(fileName, "r", encoding='windows-1251')
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
    print('1. Read data')
    print("2. Show plot")
    print("3. Add random centroids")
    print("4. Add centroid")
    print("5. Cluster")

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

def choose_data_file():
    data_files = os.listdir(DATA_FILES_DIR)
    i = 1
    for data_file in data_files:  
        print(str(i) + ". " + data_file)
        i += 1

    file_index = input("File: ")
    is_file_index_valid = (not file_index.isdigit()) or int(file_index) < 1
    is_file_index_valid = is_file_index_valid or int(file_index) > len(data_files)
    if is_file_index_valid:
        print('Incorrect file index!')
        return ''

    file_index = int(file_index) - 1
    return data_files[file_index]

def read_data():
    data_file = choose_data_file()
    if not data_file:
        return list()

    lines = read_file(data_file)
    return convert_lines_to_points(lines)

# begin

points = list()
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
        data_points = read_data()
        if data_points:
            points = data_points
            centroids.clear()
    elif command == 2:
        show_points_plot(points, centroids, False)
    elif command == 3:
        generate_random_centroids(points, centroids)
    elif command == 4:
        choose_dots_in_chart = True
        if choose_dots_in_chart:
            show_points_plot(points, centroids, True)
        else:
            add_centroid(centroids)
    elif command == 5:
        clusterization(points, centroids)
    else:
        print("Incorrect command!")
    
    print("- - - - - - - - - - - - -")