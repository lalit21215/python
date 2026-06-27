n=int(input("Enter a no: "))
x=0
while n>0:
    x=x+1
    n=n//10
print(f"Total digits in the number is: {x}")