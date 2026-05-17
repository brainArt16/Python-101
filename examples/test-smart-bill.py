# Constants
DISCOUNT = 10
ITERATIONS = 3

# Story 1
print("Welcome to Smart Grocery Bill Calculator")

# Story 2 & Story 6
product_list = []

num = int(input("How many products do you want to buy? "))
for x in range(num):
    name = input("Enter Product name: ")

    while True:
        try:
            price = float(input("Enter Price: "))
            break
        except:
            print("Enter valid amount...")

    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            break
        except:
            print("Enter valid amount...")


    product_dict = {
        "name": name,
        "price": price,
        "quantity": quantity
    }


    product_list.append(product_dict)

    # cancel = input("Enter 99 to cancel: ")

    # if cancel == "99":
    #     break


print(product_list)


# # Story 3
# subtotal = float(price) * int(quantity)

# # Story 4
# if subtotal > 20000:
#     applied_discount = (subtotal * 0.1)
#     total = subtotal - applied_discount

# else:
#     applied_discount = 0
#     total = subtotal
#     print("No Discount Applied!")


# # Story 5
# receipt = f"""
# Product Name: {name}
# Quantity: {quantity}
# Subtotal: {subtotal}
# Discount: {applied_discount}
# Total: {total}
# """
# print(receipt)

