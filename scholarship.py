gpa = float(input("Enter your gpa: "))
attendance = float(input("enter your attendance: "))
income = int(input("Enter your family annual income: "))
student = input("Are you a prior awad holder: (Yes/No)") .lower() =="yes"
if (gpa >= 3.5 and attendance >= 85 and (income <  50000 or student)):
    print("You are eligible for scholarship")
else:
    print("You arent eligible for scholarship")
 


