
purchase = float(input("Enter total purchase amount : "))
user = input("Are you a VIP member? (yes/no): ").lower()

isVIP = (user == "yes")
if isVIP:
    discount = 0.20
elif purchase > 100:
    discount = 0.10
elif 50 <= purchase <= 100:
    discount = 0.05
else:
    discount = 0.0
totalBill = purchase * (1 - discount)

print(f"actual Bill: RS.{purchase}")
print(f"Discount Applied: {discount * 100}%")
print(f"Total Amount to Pay: RS.{totalBill}")