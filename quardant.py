x = int(input("enter the coordinate of x- axis: "))
y = int(input("enter the coordinate of y-axis: "))
if (x>0 and y>0):
    print("first quardant")
elif (x<0 and y>0):
    print("second quardant")
elif (x < 0 and y < 0):
    print("third quardant")
elif (x > 0 and y< 0):
    print("fourth quardant")
else:
    print("on axis")