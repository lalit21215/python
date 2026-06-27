age=int(input("Enter your age: "))
if age>=18:
    if age<=45:
        print("You are eligible for LIC")
    else:
        print("You are not eligible for LIC")
else:
    print("You are not eligible for LIC")