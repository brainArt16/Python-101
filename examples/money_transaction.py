"""
# Mobile Transaction System — User Stories

## Project Overview

A console-based mobile money transaction system where users can:

* Create accounts
* Send money
* Withdraw money
* Deposit money
* Check balance
* View transaction history

# Core User Stories

# 1. Register Account

**As a user,**
I want to register a mobile account,
so that I can use mobile transaction services.

---

## Acceptance Criteria

* User enters name
* User enters phone number
* User creates PIN
* Account is stored successfully

---

## Concepts Covered

* Variables
* Dictionaries
* Functions

---

## Suggested Function

```python id="xkpdx0"
def register_account():
    pass
```

---

## Pseudocode

```text id="m0o5dq"
START

INPUT full_name
INPUT phone_number
INPUT pin

CREATE account dictionary

STORE account in accounts list

DISPLAY "Account created successfully"

END
```

---

# 2. Login to Account

**As a user,**
I want to login using my phone number and PIN,
so that my account remains secure.

---

## Acceptance Criteria

* User enters phone number
* User enters PIN
* System validates credentials
* Access granted if correct

---

## Suggested Function

```python id="8w0hyk"
def login():
    pass
```

---

## Pseudocode

```text id="qlw2d8"
START

INPUT phone_number
INPUT pin

SEARCH account

IF account exists AND pin is correct THEN
    DISPLAY "Login successful"
ELSE
    DISPLAY "Invalid credentials"
END IF

END
```

---

# 3. Deposit Money

**As an user,**
I want to deposit money into a my account,
so that the my balance increases.

---

## Acceptance Criteria

* Enter account number
* Enter deposit amount
* Balance updates correctly

---

## Suggested Function

```python id="ehp5p4"
def deposit_money():
    pass
```

---

## Pseudocode

```text id="2uq4w6"
START

INPUT phone_number
INPUT amount

ADD amount to balance

DISPLAY new balance

END
```

---

# 4. Withdraw Money

**As a user,**
I want to withdraw money from my account,
so that I can access cash.

---

## Acceptance Criteria

* User enters amount
* System checks balance
* Withdrawal succeeds if sufficient funds exist

---

## Suggested Function

```python id="16m8f5"
def withdraw_money():
    pass
```

---

## Pseudocode

```text id="dtjx74"
START

INPUT amount

IF balance >= amount THEN
    SUBTRACT amount from balance
    DISPLAY "Withdrawal successful"
ELSE
    DISPLAY "Insufficient balance"
END IF

END
```

---

# 5. Send Money

**As a user,**
I want to transfer money to another user,
so that I can pay or support others digitally.

---

## Acceptance Criteria

* Sender enters receiver number
* Enter amount
* Balance deducts from sender
* Receiver balance increases

---

## Suggested Function

```python id="aq2t7x"
def send_money():
    pass
```

---

## Pseudocode

```text id="7ukl40"
START

INPUT receiver_number
INPUT amount

SEARCH sender account
SEARCH receiver account

IF sender balance >= amount THEN

    SUBTRACT amount from sender

    ADD amount to receiver

    DISPLAY "Transfer successful"

ELSE
    DISPLAY "Insufficient balance"

END IF

END
```

---

# 6. Check Balance

**As a user,**
I want to check my account balance,
so that I know how much money I have.

---

## Suggested Function

```python id="w8vw8m"
def check_balance():
    pass
```

---

## Pseudocode

```text id="58zlgf"
START

DISPLAY account balance

END
```

---

# 7. View Transaction History

**As a user,**
I want to view my previous transactions,
so that I can track my account activity.

---

## Acceptance Criteria

* Deposits visible
* Withdrawals visible
* Transfers visible

---

## Suggested Function

```python id="wwum0m"
def transaction_history():
    pass
```

---

## Pseudocode

```text id="eqzcsk"
START

FOR each transaction

    DISPLAY transaction details

END FOR

END
```

---

# 8. Change PIN

**As a user,**
I want to change my PIN,
so that my account remains secure.

---

## Suggested Function

```python id="yj2e66"
def change_pin():
    pass
```

---

## Pseudocode

```text id="r23o6k"
START

INPUT old_pin

IF old_pin is correct THEN

    INPUT new_pin

    UPDATE pin

    DISPLAY "PIN changed"

ELSE

    DISPLAY "Incorrect PIN"

END IF

END
```

---

# 9. Logout

**As a user,**
I want to logout from the system,
so that unauthorized people cannot access my account.

---

## Suggested Function

```python id="vdl2sm"
def logout():
    pass
```

---

## Pseudocode

```text id="3wq7ns"
START

CLEAR current session

DISPLAY "Logged out successfully"

END
```

---

# Suggested Data Structure

```python id="uhjlwm"
accounts = [
    {
        "name": "David",
        "phone": "0755123456",
        "pin": "1234",
        "balance": 50000,
        "transactions": []
    }
]
```

---

# Main Menu Example

```text id="it0tqy"
1. Register
2. Login
3. Deposit
4. Withdraw
5. Send Money
6. Check Balance
7. Transaction History
8. Change PIN
9. Logout
10. Exit
```

# Recommended Project Structure (Follow if possible)

```text id="t4pm7k"
mobile_transaction/
│
├── main.py
├── accounts.py
├── transactions.py
├── auth.py
└── utils.py
```
"""