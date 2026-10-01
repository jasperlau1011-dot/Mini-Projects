
math = input("what would you like to do? addition? subtraction? multiplication? division? \nexponent? percentage? root? linear graph (y=mx+c)? linear equation? simultaneous equation? area? volume? 3 variable equation? quadratic equation? rounding?\nplease state the answer at its congruent form. (eg. exponent, not exponents)")
if math == "addition":
    number_1 = int(input("number 1 (addition)"))
    number_2 = int(input("number 2 (only 2 numbers can be added)"))
    full_number = number_1 + number_2
    print("heres sum of numbers:\n" + str(full_number))
elif math == "subtraction":
    sub_1 = int(input("number 1 (subtraction: number 1 - number 2)"))
    sub_2 = int(input("number 2 (only 2 numbers can be subtracted)"))
    total = sub_1 - sub_2
    print("heres the subtraction:\n" + str(total))
elif math == "multiplication":
    mul_1 = int(input("number 1 (multiplication)"))
    mul_2 = int(input("number 2 (a x b)"))
    product = mul_1 * mul_2
    print("heres the product of 2 the numbers:\n" + str(product))
elif math == "division":
    div_1 = int(input("number 1 (division)"))
    div_2 = int(input("number 2 (first number divided by this number)"))
    division = div_1 / div_2
    print("heres the divided result:\n" + str(division))
elif math == "root":
    root_1 = int(input("number 1 (is the root)"))
    root_2 = int(input("number 2 (what is in root)"))
    result = root_2 ** (1 / root_1)
    print("heres " + str(root_1) + " root of " + str(root_2) + ":\n" + str(result))
elif math == "exponent":
    ex_1 = int(input("number 1 (number bellow exponent)"))
    ex_2 = int(input("number 2 (exponent of number 1)"))
    expo = ex_1 ** ex_2
    print("heres the exponential result:\n" + str(expo))
elif math == "percentage":
    percentage_degree = input("Would you like to find 1. degree angle of 360 in graph (statistic) or 2. percentage of an intiger? (enter 1. or 2.)")
    if percentage_degree == "2.":
        per_1 = int(input("percent (dont include % eg: 100 which is 100%)"))
        per_2 = int(input("number (percent of number)"))
        per = per_1 * per_2 / 100
        print("heres " + str(per_1) + "% of " + str(per_2) + ":\n" + str(per))
    elif percentage_degree == "1.":
        per_3 = int(input("enter value out of total"))
        per_4 = int(input("enter total"))
        per_5 = per_3 / per_4
        per_6 = per_5 * 360
        print(f"heres the degrees (angle): \n {per_6}" + "°")
    else:
        print("answer and request incomplete or invalid. press green 'play button' in the top to complete it again.")
elif math == "linear graph":
    gra = int(input("enter gradient (m)"))
    c = int(input("enter 'c'"))
    quest = input("enter whether your providing value of y or x (enter at its congruent form)")
    if quest == "y":
        lin_1 = int(input("enter value of 'y'"))
        lin_2 = (lin_1 - c) / gra
        print(f"The value of x is: {lin_2}")
    elif quest == "x":
        lin_3 = int(input("enter value of 'x'"))
        print("The value of y is: " + str(int(lin_3 * gra) + c))
elif math == "linear equation":
    x_1 = int(input("enter exponetial of x"))
    c_2 = int(input("enter value of constant / y-intercept"))
    answer = int(input("enter value of integer after equation(eg: 8x+4=3, 3 is an example)"))
    x = (answer - c_2) / x_1
    print("Answer is:\n" + str(x))
elif math == "simultaneous equation":
    sim_1 = int(input("enter value of coefficient of 'x' in first equation: "))
    sim_2 = int(input("enter value of coefficient of 'y' in first equation: "))
    sim_3 = int(input("enter value of coefficient of 'x' in second equation: "))
    sim_4 = int(input("enter value of coefficient of 'y' in second equation: "))
    res_1 = int(input("enter value of final value in first equation: "))
    res_2 = int(input("enter value of final value in second equation: "))
    
    denominator = (sim_1 * sim_4 - sim_2 * sim_3)
    
    if denominator == 0:
        print("These equations are parallel and have no unique solution.")
    else:
        y_3 = (sim_1 * res_2 - res_1 * sim_3) / denominator
        print("heres answer for 'y':\n" + str(y_3))
        
        x_3 = (res_1 - y_3 * sim_2) / sim_1
        print("heres answer for 'x':\n" + str(x_3))

elif math == "area":
    area = input("do you want to do area of right angled quadrilateral or triangle or circle?")
    if area == "right angled quadrilateral":
        length = int(input("enter value of length"))
        width = int(input("enter value of width"))
        print("the area is:\n" + str(length * width))
    if area == "triangle":
        tri = input("state whether you have info of the 3 sides or info of hight and base? type 'info of 3 sides' or 'info of hight and base'")
        if tri == "info of 3 sides":
            side_1 = int(input("enter value of side 1"))
            side_2 = int(input("enter value of side 2"))
            side_3 = int(input("enter value of side 3"))
            semi_perimeter = (side_1 + side_2 + side_3) / 2
            area_tri3 = (semi_perimeter * ((semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3)))** (1 / 2)
            print("heres the answer:\n" + str(area_tri3))
        elif tri == "info of height and base":
            length_tri = int(input("enter value of base length"))
            height_tri = int(input("enter value of height"))
            area_tri2 = length_tri * height_tri / 2
            print("heres area of triangle:\n" + str(area_tri2))
    if area == "circle":
        radius = int(input("enter value of radius"))
        area_circle = radius ** 2 * 3.14159265359
        print("area of circle is:\n" + str(area_circle))
elif math == "volume":
    volume = input("do you request to do volume of sphere or prism or cone or pyramid?")
    if volume == "sphere":
        radius_sphere = int(input("enter value of radius of sphere"))
        volume_sphere = ((radius_sphere ** 3) * 4 * 3.14159265359) / 3
        print("heres volume of sphere:\n" + str(volume_sphere))
    elif volume == "prism":
        prism_base = input("what shape is base of prism? right agled quadrilateral? triangle? circle?")
        if prism_base == "right angled quadrilateral":
            length_prismsquare = int(input("enter value of length"))
            width_prismsquare = int(input("enter value of width"))
            height_prismsquare = int(input("enter value of height"))
            volume_prismsquare = length_prismsquare * width_prismsquare * height_prismsquare
            print("heres volume of right angled quadrilateral:\n" + str(volume_prismsquare))
        elif prism_base == "triangle":
            triangle_baseprism = int(input("enter base of triangle"))
            triangle_heightprism = int(input("enter height of triangle"))
            height_triangleprism = int(input("enter height of prism"))
            volume_triangleprism = ((triangle_baseprism * triangle_heightprism) / 2) * height_triangleprism
            print(volume_triangleprism)
        elif prism_base == "circle":
            radius_prism123 = int(input("enter radius of circle"))
            height_prismcircle = int(input("enter height of prism"))
            volume_circleprism = radius_prism123 ** 2 * 3.14159265359 * height_prismcircle
            print(volume_circleprism)
    elif volume == "cone":
        radius_cone = int(input("enter radius of cone"))
        height_cone = int(input("enter height of cone"))
        volume_cone = (radius_cone ** 2 * 3.14159265359 * height_cone)/3
        print("volume of cone is:\n" + str(volume_cone))
    elif volume == "pyramid":
        basel_pyramidvol = int(input("enter value of length of base"))
        basew_pyramidvol = int(input("enter value of width of base"))
        height_pyramidvol = int(input("enter value of height of pyramid"))
        volume_pyramid = (basel_pyramidvol * basew_pyramidvol * height_pyramidvol) / 3
        print("heres volume of pyramid:\n" + str(volume_pyramid))
elif math == "quadratic equation":
    qua_coe1 = int(input("enter coefficient of x^2"))
    qua_coe2 = int(input("enter coefficient of x"))
    qua_coe3 = int(input("enter y intercept"))
    ans_qua1 = ( - (qua_coe2) + ((qua_coe2 ** 2 - 4 * qua_coe1 * qua_coe3) ** (1 / 2))) / (2 * qua_coe1)
    ans_qua2 = ( - (qua_coe2) - ((qua_coe2 ** 2 - 4 * qua_coe1 * qua_coe3) ** (1 / 2))) / (2 * qua_coe1)
    print("heres solution 1 to 'x'" + str(ans_qua1))
    print("heres solution 2 to 'x'" + str(ans_qua2))
elif math == "3 variable equation":
    x_3var1 = int(input("enter coefficient of x (first equation)"))
    y_3var1 = int(input("enter coefficient of y (first equation)"))
    z_3var1 = int(input("enter coefficient of z (first equation)"))
    
    x_3var2 = int(input("enter coefficient of x (second equation)"))
    y_3var2 = int(input("enter coefficient of y (second equation)"))
    z_3var2 = int(input("enter coefficient of z (second equation)"))
    
    x_3var3 = int(input("enter coefficient of x (third equation)"))
    y_3var3 = int(input("enter coefficient of y (third equation)"))
    z_3var3 = int(input("enter coefficient of z (third equation)"))
    
    resul_3var = int(input("enter the result in the first equation"))
    resul_2var = int(input("enter the result in the second equation"))   
    resul_1var = int(input("enter the result in the last equation"))
    D = (x_3var1 * (y_3var2 * z_3var3 - z_3var2 * y_3var3) - 
         y_3var1 * (x_3var2 * z_3var3 - z_3var2 * x_3var3) + 
         z_3var1 * (x_3var2 * y_3var3 - y_3var2 * x_3var3))
    if D == 0:
        print("The system has no unique solution (infinitely many or zero solutions).")
    else:
        Dx = (resul_3var * (y_3var2 * z_3var3 - z_3var2 * y_3var3) - 
              y_3var1 * (resul_2var * z_3var3 - z_3var2 * resul_1var) + 
              z_3var1 * (resul_2var * y_3var3 - y_3var2 * resul_1var))
        Dy = (x_3var1 * (resul_2var * z_3var3 - z_3var2 * resul_1var) - 
              resul_3var * (x_3var2 * z_3var3 - z_3var2 * x_3var3) + 
              z_3var1 * (x_3var2 * resul_1var - resul_2var * x_3var3))
        Dz = (x_3var1 * (y_3var2 * resul_1var - resul_2var * y_3var3) - 
              y_3var1 * (x_3var2 * resul_1var - resul_2var * x_3var3) + 
              resul_3var * (x_3var2 * y_3var3 - y_3var2 * x_3var3))
        x = Dx / D
        y = Dy / D
        z = Dz / D

        print("heres answer to y:\n" + str(y))
        print("heres answer to z:\n" + str(z))
        print("heres answer to x:\n" + str(x))
elif math == "rounding":
    round_val = int(input("enter value of what decimal unit do you want to round off (eg: 1 for 1 decimal)"))
    round_num = float(input("enter value you want to round off"))
    round_ans = round(round_num, round_val)
    print("heres rounded number:\n" + str(round_ans))
else:
    print("\nresponse unvalid. please press the button above to use calculator.")
