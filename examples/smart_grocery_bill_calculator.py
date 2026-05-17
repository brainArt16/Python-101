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
DEFAULT_PRODUCT_COUNT = 3


def welcome_message(title: str) -> None:
    """Display the store welcome message."""
    print(f"Welcome to {title}!")


def prompt_float(prompt: str) -> float:
    """Prompt the user for a floating-point number."""
    return float(input(prompt))


def prompt_int(prompt: str) -> int:
    """Prompt the user for an integer."""
    return int(input(prompt))


def prompt_yes_no(prompt: str) -> bool:
    """Prompt the user for a yes/no answer."""
    return input(prompt).strip().lower() == "yes"


def get_product_info() -> dict:
    """Collect a single product's information from the cashier."""
    name = input("Enter product name: > ").strip()
    price = prompt_float("Enter product price: > ")
    quantity = prompt_int("Enter product quantity: > ")
    return {
        "name": name,
        "price": price,
        "quantity": quantity,
        "subtotal": calculate_subtotal(price, quantity),
    }


def calculate_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for one product."""
    return price * quantity


def calculate_discount(amount: float) -> float:
    """Return the regular discount for an amount."""
    if amount > MINIMUM_AMOUNT:
        return amount * DISCOUNT_RATE
    return 0.0


def calculate_member_discount(amount: float, is_member: bool) -> float:
    """Return the additional member discount."""
    if not is_member:
        return 0.0
    return amount * MEMBER_DISCOUNT_RATE


def collect_products(count: int = DEFAULT_PRODUCT_COUNT) -> list[dict]:
    """Collect multiple products from the cashier."""
    products = []
    for index in range(1, count + 1):
        print(f"\nProduct {index} of {count}")
        products.append(get_product_info())
    return products


def format_product_lines(products: list[dict]) -> str:
    """Format each product line for the receipt."""
    lines = ["====== RECEIPT ======"]
    for product in products:
        lines.extend(
            [
                f"Product Name: {product['name']}",
                f"Unit Price: {product['price']}",
                f"Quantity: {product['quantity']}",
                f"Subtotal: Tsh. {product['subtotal']}",
                "#############################",
            ]
        )
    return "\n".join(lines)


def print_receipt(
    products: list[dict],
    overall_subtotal: float,
    regular_discount: float,
    member_discount: float,
    final_total: float,
) -> None:
    """Print the final receipt."""
    receipt = format_product_lines(products)
    receipt += f"\nOverall Subtotal: Tsh. {overall_subtotal}"
    receipt += f"\nRegular Discount: Tsh. {regular_discount}"
    receipt += f"\nMember Discount: Tsh. {member_discount}"
    receipt += f"\nTotal: Tsh. {final_total}"
    print(receipt)


def main() -> None:
    welcome_message()
    products = collect_products()

    overall_subtotal = sum(product["subtotal"] for product in products)
    regular_discount = calculate_discount(overall_subtotal)
    subtotal_after_discount = overall_subtotal - regular_discount

    is_member = prompt_yes_no("Are you a member? (yes/no): > ")
    member_discount = calculate_member_discount(subtotal_after_discount, is_member)
    final_total = subtotal_after_discount - member_discount

    print_receipt(
        products, overall_subtotal, regular_discount, member_discount, final_total
    )


if __name__ == "__main__":
    main()
