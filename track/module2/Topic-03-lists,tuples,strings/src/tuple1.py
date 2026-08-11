
product_id=(input())
product_name=(input())
product_category=(input())
unit_price=float(input())
available_quantity=int(input())
reorder_level=int(input())
# read product details and store in tuple

product_details=(product_id,product_name,product_category,unit_price,available_quantity)

# access product id and product name from tuple
product_details[:2]

# unpack tuple into separate variable
product_id,product_name,product_category,unit_price,available_quantity=product_details
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Product Category: {product_category}")
print(f"Unit Price: {unit_price}")
print(f"available Quantity: {available_quantity}")

#total stock value
stock_value=unit_price*available_quantity 
print(f"Stock Value: {stock_value}")

#check stock status
if available_quantity==0:
    print("Out of Stock")

elif available_quantity<=reorder_level:
    print("Reordered Required")

else:
    print("Enough Stock")




