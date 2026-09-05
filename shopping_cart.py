print(input("Enter customer's name: "))
Product_1 = input("Product 1: ")
Product_1_Price = float(input("Price: "))
Product_2 = input("Product 2: ")
Product_2_Price = float(input("Price: "))
Product_3 = input("Product 3: ")
Product_3_Price = float(input("Price: "))
subtotal = Product_1_Price + Product_2_Price + Product_3_Price
print("Subtotal:", subtotal)
Discount = float(input("discount:"))
final_total = subtotal - Discount
print("Final Total:", final_total)