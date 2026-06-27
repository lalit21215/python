price=float(input("Enter price of Book:"))
dis=0
net=0
if price>=500:
    dis=price*10/100
else:
    dis=price*5/100

net=price-dis
print(f"price={price}, Discount={dis}, Net Price={net}")