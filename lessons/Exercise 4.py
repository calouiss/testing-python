def greet_customer(name):
    print("Hello, " + name + "! Welcome!")

def take_order():
    print("We have burger ($5), fries ($4), salad ($4), drinks ($2).")
    order = {}
    while True:
        item = input("Enter item to order (or 'done'): ").lower()
        if item == 'done':
            break
        qty = int(input("How many? "))
        order[item] = order.get(item, 0) + qty
    return order

def calculate_bill(order):
    prices = {'burger': 5, 'fries': 4, 'salad': 4, 'drinks': 2}
    total = 0
    for item in order:
        if item in prices:
            total += prices[item] * order[item]
    return total

def apply_discount(total):
    if total > 20:
        print("You get 10% off!")
        total = total * 0.10
    return total

def countdown(n):
    if n == 0:
        print("Order is ready!")
    else:
        print(n)
        countdown(n-1)

# Run the program
greet_customer("Customer")
order = take_order()
total = calculate_bill(order)
total = apply_discount(total)
print("Total bill: $", total)
countdown(5)