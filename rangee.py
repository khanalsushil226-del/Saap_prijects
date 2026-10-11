num = int(input("Enter the number: "))

if (num >= 10 and num  <= 50):
    if num %2 == 0:
        print("valid even")
    else:
        print("Valid odd")
else:
    print("please enter the number in range")
