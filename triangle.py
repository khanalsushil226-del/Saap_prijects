a = int(input("enter the first side: "))
b = int(input("enter second side: "))
c = int(input("enter third side: "))
if (a + b > c and a + c > b and b + c > a):
    if (a==b==c):
        print("equilateral triangle")
    elif(a==b or b==c or a==c):
        print("isosceles triangle")
    else:
        print("scalene triangle")
else:
    print("please enter valid sides of triangle")

