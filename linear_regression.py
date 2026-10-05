message = input("enter data-set by (x, y): eg, '1200 12, 3000 30'. NOTE: no decimal places are available.")
total_x = 0
total_y = 0
relationship_xy = []
lists_average = {}
lists = {}
list_data = message.split(", ")
if len(list_data) >= 3:
    for list_1 in list_data:
        list_2 = list_1.split(" ")
        if len(list_2) == 2:
            messages = list_2[0]
            value = list_2[1]
            lists[messages] = value
    for value_x in range(0, len(lists.keys()) - 1):
        if value_x != len(lists.keys()):
            dif_x = int(list(lists.keys())[value_x]) - int(list(lists.keys())[value_x + 1])
            dif_y = int(list(lists.values())[value_x]) - int(list(lists.values())[value_x + 1])
            lists_average[dif_x] = dif_y
            g = dif_y / dif_x
            relationship_xy.append(g)
    all_same_xy = len(set(relationship_xy)) <= 1
    if all_same_xy == True:
        c = int(list(lists.values())[0]) - int(list(lists.keys())[0]) * g
        print(f"\tThe relationship has an linear, constant and estimate gradient of {g}")
        print(f"\tThe equation for relationship is: y = {g}x + {c}")
        question = input("\nEnter 'x' or 'y' to estimate the value of alternate axis: ")
        if question == "x":
            x = int(input("Enter value of 'x': "))
            y = x * g + c
            print(f"The estimated value of 'y' is: {y}")
        elif question == "y":
            y = int(input("Enter value of 'y': "))
            x = (y - c) / g
            print(f"The estimated value of x is: {x}")
        else:
            print("Invalid / Incomplete request")
    else:
        for x_2 in range(0, len(lists_average.keys())):
            total_x += list(lists_average.keys())[x_2]
        total_x = total_x / len(lists_average.keys())
        for y_2 in range(0, len(lists_average.values())):
            total_y += list(lists_average.values())[y_2]
        total_y = total_y / len(lists_average.values())
        g = total_y / total_x
        c = int(list(lists.values())[0]) -  int(list(lists.keys())[0]) * g
        print(f"The relationship shown does not have a constant, linear gradient, estimated gradient is: {g}")
        print(f"The equation for the relationship is: y = {g}x + {c}")
        question = input("\nEnter 'x' or 'y' to estimate the value of alternate axis: ")
        if question == "x":
            x = int(input("Enter value of 'x': "))
            y = x * g + c
            print(f"The estimated value of 'y' is: {y}")
        elif question == "y":
            y = int(input("Enter value of 'y': "))
            x = (y - c) / g
            print(f"The estimated value of 'x' is: {x}")
        else:
            print("Invalid / Incomplete request")
elif len(list_data) == 2:
    print("In result of data given only for 2 points: a linear, constant relationship is demonstrated.")
    for list_1 in list_data:
        list_2 = list_1.split(" ")
        if len(list_2) == 2:
            messages = list_2[0]
            value = list_2[1]
            lists[messages] = value
    dif_x = int(list(lists.keys())[0]) - int(list(lists.keys())[1])
    dif_y = int(list(lists.values())[0]) - int(list(lists.values())[1])
    g = dif_y / dif_x
    c = int(list(lists.values())[0]) - int(list(lists.keys())[0]) * g 
    print(f"\tThe relationship shows a gradient of {g}")
    print(f"\tThe relationship shows an equation of: y = {g}x + {c}")
    question = input("Enter 'x' or 'y' to estimate to alternate axis value: ")
    if question == "x":
        x = int(input("Enter value of 'x': "))
        y = x * g + c
        print(f"The estimated value of 'y' is: {y}")
    elif question == "y":
        y = int(input("Enter value of 'y': "))
        x = (y - c) / g
        print(f"The estimated value of 'x' is: {x}")
    else:
        print("Invalid / Incomplete request")
elif len(list_data) == 1:
    print("Only one point was given, incomplete data.")
else:
    print("Invalid / Incomplete request")
    
    
