ellipse_filepath = input("Введите путь к файлу эллипса")
points_filepath = input("Введите путь к файлу с точками")

ellipse_cords = []
with open(ellipse_filepath, 'r') as file:
    for line in file:
        if len(line.split()) > 0:
            ellipse_cords.append(tuple(map(int, line.split())))
print(ellipse_cords)

points = []
with open(points_filepath, 'r') as file:
    for line in file:
        if len(line.split()) > 0:
            points.append(tuple(map(int, line.split())))
print(points)

for i in points:
    the_point_is_on = (i[0] - ellipse_cords[0][0])**2/ellipse_cords[1][0]**2 + (i[1] - ellipse_cords[0][1])**2/ellipse_cords[1][1]**2
    if the_point_is_on == 1:
        print(0)
    elif the_point_is_on < 1:
        print(1)
    elif the_point_is_on > 1:
        print(2)
