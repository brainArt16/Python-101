"""
# 1. Smart Grocery Bill Calculator — User Stories

## Project Goal

Build a small billing system that helps a cashier calculate customer bills and apply discounts.

---

## Story 1 — Welcome Screen

**As a cashier**,
I want the system to display a welcome message,
so that users know the program has started.

### Tasks

* Use `print()`
* Show store name
* Show greeting message

---

## Story 2 — Enter Product Information

**As a cashier**,
I want to enter the product name, price, and quantity,
so that the system can calculate the bill.

### Tasks

* Use variables
* Use `input()`
* Convert numbers using `int()` or `float()`

### Concepts

* Variables
* Data types
* User input

---

## Story 3 — Calculate Total Cost

**As a cashier**,
I want the system to calculate the total price,
so that I know how much the customer should pay.

### Formula

Total = Price * Quantity

### Tasks

* Use multiplication operator
* Store result in variable

### Concepts

* Operators
* Arithmetic calculations

---

## Story 4 — Apply Discount

**As a store owner**,
I want discounts to be applied for large purchases,
so that customers are encouraged to buy more.

### Rules

* If total > 20,000 → 10% discount
* Otherwise → no discount

### Tasks

* Use `if` statement
* Calculate discount

### Concepts

* Conditional statements
* Comparison operators

---

## Story 5 — Print Final Receipt

**As a customer**,
I want to see the final receipt,
so that I know what I bought and how much I paid.

### Receipt Should Show

* Product name
* Quantity
* Original total
* Discount
* Final amount

---

# Intermediate Expansion Stories

## Story 6 — Multiple Products

**As a cashier**,
I want to enter several products,
so that customers can buy multiple items.

### Concepts

* Lists
* Loops

---

## Story 7 — Membership Discount

**As a loyal customer**,
I want members to receive additional discounts,
so that membership becomes beneficial.

### Concepts

* Boolean values
* Nested conditions

"""

# Constants
MINIMUM_AMOUNT = 20000
DISCOUNT_RATE = 0.1
MEMBER_DISCOUNT_RATE = 0.15

#  Welcome Screen: Story 1 — Welcome Screen
print("Welcome to Smart Grocery Store!")

# Enter product information: Story 2 — Enter Product Information
product_name = input("Enter product name: > ")
product_price = float(input("Enter product price: > "))
product_quantity = int(input("Enter product quantity: > "))


# Calculate total cost: Story 3 — Calculate Total Cost
subtotal = product_price * product_quantity
print("Subtotal is Tsh. ", subtotal)

# Apply discount: Story 4 — Apply Discount
if subtotal > MINIMUM_AMOUNT:
    discount = subtotal * DISCOUNT_RATE
else:
    discount = 0

total = subtotal - discount
print("Total is Tsh. ", total)

# Receipt: Story 5 — Print Final Receipt
receipt = f"""
====== RECEIPT ======
Product Name: {product_name}
Unit Price: {product_price}
Quantity: {product_quantity}
Subtotal: Tsh. {subtotal}
Discount: Tsh. {discount}
Total: Tsh. {total}
"""
print(receipt)


# Story 6 — Multiple Products
product_list = []

# Loop
for x in range(3):
    product_name = input("Enter product name: > ")
    product_price = float(input("Enter product price: > "))
    product_quantity = int(input("Enter product quantity: > "))

    subtotal = product_price * product_quantity

    product = {
        'name': product_name,
        'price': product_price,
        'quantity': product_quantity,
        'subtotal': subtotal
    }
    product_list.append(product)

# Calculate overall
overall_subtotal = sum(p['subtotal'] for p in product_list)
if overall_subtotal > MINIMUM_AMOUNT:
    discount = overall_subtotal * DISCOUNT_RATE
else:
    discount = 0
total = overall_subtotal - discount

# Receipt
receipt = """
====== RECEIPT ======
"""
for p in product_list:
    receipt += f"""Product Name: {p['name']}
Unit Price: {p['price']}
Quantity: {p['quantity']}
Subtotal: Tsh. {p['subtotal']}
#############################
"""
receipt += f"""Overall Subtotal: Tsh. {overall_subtotal}
Discount: Tsh. {discount}
Total: Tsh. {total}
"""
print(receipt)


# Story 7 — Membership Discount
is_member = input("Are you a member? (yes/no): > ").lower() == 'yes'

if is_member:
    member_discount = total * MEMBER_DISCOUNT_RATE
else:
    member_discount = 0