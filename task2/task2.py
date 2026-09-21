from math import isclose
import argparse
parser = argparse.ArgumentParser(
        description='Точки и Эллипс'
)

parser.add_argument(
    'ellipse',
    help='Параметры эллипса'
)

parser.add_argument(
    'points',
    help='Точки расположение'
)

args = parser.parse_args()
ellipse_filepath = args.ellipse
points_filepath = args.points

ellipse_cords = []
with open(ellipse_filepath, 'r') as file:
    for line in file:
        if len(line.split()) > 0:
            ellipse_cords.append(tuple(map(float, line.split())))

points = []
with open(points_filepath, 'r') as file:
    for line in file:
        if len(line.split()) > 0:
            points.append(tuple(map(float, line.split())))

for i in points:
    the_point_is_on = (i[0] - ellipse_cords[0][0])**2/ellipse_cords[1][0]**2 + (i[1] - ellipse_cords[0][1])**2/ellipse_cords[1][1]**2
    if isclose(the_point_is_on, 1):
        print(0)
    elif the_point_is_on < 1:
        print(1)
    elif the_point_is_on > 1:
        print(2)
