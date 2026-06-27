basic_salary = float(input("Enter the basic salary: "))
if basic_salary < 10000:
    hra = 0.10 * basic_salary 
    da = 0.90 * basic_salary   
else:
    hra = 0.20 * basic_salary 
    da = 0.95 * basic_salary   
net_salary = basic_salary + hra + da
print(f"Basic Salary = {basic_salary}")
print(f"HRA = {hra}")
print(f"DA = {da}")
print(f"Net Salary = {net_salary}")
