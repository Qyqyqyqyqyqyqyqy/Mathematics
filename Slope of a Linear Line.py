def slope():
    x_1,y_1= eval(input("What is the x1 and y1? in the form of (x,y)"))
    x_2,y_2= eval(input("What is the x2 and y2? in the form of (x,y)"))
    rise= y_2-y_1
    run= x_2-x_1
    slope_formula=rise/run
    print("The slope is", slope_formula)


slope()