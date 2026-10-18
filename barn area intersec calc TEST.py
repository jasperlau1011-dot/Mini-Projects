coordinates = ['x_1', 'x_2', 'x_3', 'x_4', 'y_1', 'y_2', 'y_3', 'y_4' ]
coordinates_x = []
coordinates_y = []
for x in coordinates:
    xs = int(input("enter value of " + x + ".(note that x_1 and x_2, y_3 and y_4 and so on represent a rectangle / square)"))
    if "x" in x:
        coordinates_x.append(xs)
    else:
        coordinates_y.append(xs)
mini_x = min(coordinates_x)
maxa_x = max(coordinates_x)
coordinates_x.remove(maxa_x)
coordinates_x.remove(mini_x)
diff = max(coordinates_x) - min(coordinates_x)
mini_y = min(coordinates_y)
maxa_y = max(coordinates_y)
coordinates_y.remove(maxa_y)
coordinates_y.remove(mini_y)
diff_y = max(coordinates_y) - min(coordinates_y)
list_xy = [diff_y, diff]
area_length = min(list_xy)
area = area_length ** 2
print("heres area: \n" + str(area))

