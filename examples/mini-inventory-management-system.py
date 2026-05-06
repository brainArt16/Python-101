"""
# 3. Mini Inventory Management System — User Stories

## Project Goal

Build a system for managing products and stock in a small shop or pharmacy.

---

## Story 1 — Add Product

**As a shop owner**,
I want to add products into inventory,
so that stock can be managed digitally.

### Product Information

* Product name
* Price
* Quantity

### Concepts

* Variables
* Dictionaries

---

## Story 2 — Store Products

**As a developer**,
I want products stored in a collection,
so that many products can be managed together.

### Concepts

* Lists
* Dictionaries

### Example

```python
inventory = [
    {
        "name": "Soap",
        "price": 2000,
        "stock": 30
    }
]
```

---

## Story 3 — View Inventory

**As a shop owner**,
I want to see all products,
so that I know current stock levels.

### Concepts

* Loops
* Lists

---

## Story 4 — Search Product

**As a cashier**,
I want to search for products by name,
so that products can be found quickly.

### Concepts

* Input
* Conditions
* String comparison

---

## Story 5 — Detect Low Stock

**As a shop owner**,
I want low-stock products identified,
so that I can restock before items finish.

### Rules

* If stock < 10 → show warning

### Concepts

* Conditional statements

---

## Story 6 — Calculate Stock Value

**As a business owner**,
I want to know the total value of inventory,
so that I can estimate business worth.

### Formula

\text{Stock Value} = \text{Price} \times \text{Quantity}

---

# Intermediate Expansion Stories

## Story 7 — Update Product Quantity

**As a shop owner**,
I want stock quantities updated after sales,
so that inventory remains accurate.

---

## Story 8 — Remove Product

**As an administrator**,
I want old products removed from inventory,
so that the inventory stays clean.

---

## Story 9 — Product Categories

**As a shop owner**,
I want products grouped into categories,
so that inventory becomes easier to manage.

### Example Categories

* Medicine
* Drinks
* Electronics
---
"""