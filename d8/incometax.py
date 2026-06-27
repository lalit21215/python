income = float(input("Enter your income (in lakhs): "))

if income <= 12:
    tax = 0
elif income <= 16:
    tax = income * 0.05
elif income <= 20:
    tax = income * 0.10
elif income <= 24:
    tax = income * 0.15
else:
    tax = income * 0.20

print(f"Income Tax = {tax} lakhs")
