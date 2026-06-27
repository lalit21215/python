cost_price = float(input("Enter the cost price: "))
sale_price = float(input("Enter the sale price: "))
if sale_price > cost_price:
    profit = sale_price - cost_price
    print(f"Profit = {profit}")
elif sale_price < cost_price:
    loss = cost_price - sale_price
    print(f"Loss = {loss}")
else:
    print("No Profit, No Loss")