# Calculate net amount to be paid

qty = int(input("Enter qty : "))
price = int(input("Enter price : "))

amount = qty * price
discount = amount * 0.15
net_amount = amount - discount

print(f"Amount      : {amount:5.0f}")
print(f"- Discount  : {discount:5.0f}")
print(f"              -----")
print(f"Net amount  : {net_amount:5.0f}")
