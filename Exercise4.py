# 1. Function with default parameter
def greet_customer(name, country="Canada"):
    print(f"Welcome {name} from {country}!")


# 2. Function with *args
def calculate_bill(*items):
    total = 0
    for item in items:
        food, price = item   # unpack tuple
        print(f"Added {food} - ${price}")
        total += price
    return total


# 3. Function with **kwargs
def apply_discount(amount, **discounts):
    for key, value in discounts.items():
        print(f"Applying {key} discount of {int(value*100)}%")
        amount -= amount * value
    return amount


# 4. Recursive function
def countdown(order_no):
    if order_no > 0:
        print(f"Preparing order {order_no}")
        countdown(order_no - 1)
    else:
        print("Order Ready!")


# -----------------------------
# Example Flow (Real Scenario)
# -----------------------------

# Greeting customer
greet_customer("Alice")
greet_customer("Bob", "India")

print("\n--- Order Processing ---")

# Customer orders
total = calculate_bill(("Burger", 5), ("Pizza", 8), ("Juice", 3))
print("Total Bill: $", total)

print("\n--- Applying Discounts ---")
final_amount = apply_discount(total, student=0.1, festival=0.2)
print("Final Bill: $", final_amount)

print("\n--- Countdown Until Ready ---")
countdown(3)
