m1 = float(input("Enter m of subject 1: "))
m2 = float(input("Enter m of subject 2: "))
m3 = float(input("Enter m of subject 3: "))
m4 = float(input("Enter m of subject 4: "))
m5 = float(input("Enter m of subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 5)
print(f"Total m = {total}")
print(f"Percentage = {percentage:.2f}%")
if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
