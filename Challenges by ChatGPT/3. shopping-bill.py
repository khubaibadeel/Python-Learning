# Arithmetic Operators
# Shopping Bill: Input price and quantity of 3 products. Calculate subtotal and final total.
# ⭐

product1=int(input("Enter the Price of Product 1: "))
product2=int(input("Enter the Price of Product 2: "))
product3=int(input("Enter the Price of Product 3: "))

subtotal=product1+product2+product3

POScharges=1.00
total=subtotal+POScharges
print(total)