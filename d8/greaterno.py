n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))


if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n2 > n1:
    print(f"{n2} is greater than {n1}")
else:
    print("Both numbers are equal")