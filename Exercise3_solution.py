# Inventory as a nested dictionary
inventory = {
    "P101": {"name": "Laptop", "price": 1200, "qty": 5},
    "P102": {"name": "Mouse", "price": 25, "qty": 20},
    "P103": {"name": "Keyboard", "price": 45, "qty": 15}
}

print("Welcome to Electronics Shop Inventory System")

while True:
    print("\nMenu:")
    print("1. View Inventory")
    print("2. Add New Product")
    print("3. Purchase Product")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    match choice:
        case "1":
            # View inventory
            if not inventory:
                print("Inventory is empty.")
            else:
                print("\nCurrent Inventory:")
                for pid, details in inventory.items():
                    print(f"ID: {pid} | Name: {details['name']} | Price: ${details['price']} | Qty: {details['qty']}")

        case "2":
            # Add new product
            pid = input("Enter new product ID: ").strip()
            if pid in inventory:
                print(" Product ID already exists. Try again.")
                continue
            name = input("Enter product name: ").strip()
            price = float(input("Enter product price: "))
            qty = int(input("Enter product quantity: "))
            
            #inventory[pid] = {"name": name, "price": price, "qty": qty}
            inventory.update({pid: {"name": name, "price": price, "qty": qty}})
            print(f" Product {name} added successfully!")
            

        case "3":
            # Purchase product
            pid = input("Enter product ID to purchase: ")
            if pid not in inventory:
                print(" Invalid product ID.")
                continue
            qty_to_buy = int(input("Enter quantity to purchase: "))
            if qty_to_buy <= inventory[pid]["qty"]:
                total = qty_to_buy * inventory[pid]["price"]
                inventory[pid]["qty"] -= qty_to_buy
                print(f" Purchase successful! Total = ${total}")
                print(f"Remaining stock of {inventory[pid]['name']}: {inventory[pid]['qty']}")
            else:
                print(" Not enough stock available.")

        case "4":
            print("Exiting system. Thank you!")
            break

        case _:
            print(" Invalid choice. Please enter 1-4.")
