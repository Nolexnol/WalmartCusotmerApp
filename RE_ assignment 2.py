import csv

# Gets the name of an item
def get_item():
    while True:
        item_name = input("Enter item name to add to cart (enter 'rem' to remove item or press 'Enter' to check out.): ")
        if item_name == "" or item_name.lower() == "rem":
            return item_name
        elif item_name.isdigit():
            print("Invalid input. Item name cannot be only numbers. Please try again.")
        else:
            return item_name

# Removes an item and its corresponding price from the lists
def remove_item(categorized_items, categories):
    print("Current cart:", categorized_items)
    r_item = input("Enter the name of the item that you want to remove: ").strip()

    found = False
    for category, items in categorized_items.items():
        if r_item in items:
            found = True
            if input(f"Would you like to remove {r_item}? (y/n) ").lower() == "y":
                items[r_item] -= categories[category][r_item]  # Subtract unit price

                if items[r_item] <= 0:  # If price becomes zero, remove the item
                    del items[r_item]

                if not items:  # If the category is now empty, remove it
                    del categorized_items[category]

                print(f"{r_item} has been removed.")
                return
    if not found:
        print("Item not found in your cart.")

# Saves the shopping cart details to a CSV file
def save_to_csv(categorized_items, shopper_id, tax, total):
    filename = r"D:\Grambling Materials\Spring 2025 courses\Data Structures and Algorithms\WalmartCusotmerApp\shopping_cart.csv"
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(f"ShopperID: {shopper_id}")
        writer.writerow(["Category", "Item", "Price"])
        for category, items in categorized_items.items():
            for item, price in items.items():
                writer.writerow([category, item, price])
        writer.writerow([])
        writer.writerow(["Tax", "", tax])
        writer.writerow(["Total", "", total])

# Displays receipt
def display_receipt(categorized_items, shopper_id):
    total = sum(sum(items.values()) for items in categorized_items.values())
    tax = total * 0.1044
    final_total = total + tax
    print("="*60)
    print(f"{'Category':<20} | {'Item':<20} | {'Price'}")
    print("-"*60)
    for category, values in categorized_items.items():
        print(f"{category:<20} |")
        for item, price in values.items():
            print(f"{'':<20} | {item:<20} | ${price:.2f}")
        print("-"*60)
    print("="*60)
    print(f"{'Tax':<20} |  ${tax:.2f}")
    print(f"{'Total':<20} |  ${final_total:.2f}")
    save_to_csv(categorized_items, shopper_id, tax, final_total)


def main():
    shopper_id = input("Enter your Shopper ID: ")
    print("Welcome to Walmart. Please follow the instructions to make your shopping experience successful.")
    print("To remove an item from your list, enter 'rem'")
    print("Once you are done adding things to cart, leave blank and press 'Enter' to checkout")
    print("="*100)
    categorized_items = {}
    categories = {
        "Groceries": {"meat": 3.00, "milk": 4.00, "bread": 2.00, "eggs": 3.00, "cheese": 1.00},
        "Home products": {"sofa": 1000.00, "lamp": 150.00, "curtains": 100.00, "vase": 50.00, "shelves": 250.00},
        "Electronics": {"laptop": 2000.00, "headphones": 100.00, "smartphone": 700.00, "camera": 5000.00, "tv": 1500.00},
        "Clothing": {"t-shirt": 20.00, "jeans": 30.00, "jacket": 40.00, "socks": 10.00, "hat": 35.00},
        "Toys": {"lego set": 50.00, "action figure": 70.00, "doll": 35.00, "puzzle": 7.99, "bicycle": 269.99}
    }
    "Gets item and check if user wants to remove an item or check out"
    while True:
        item = get_item()
        if item == "rem":
            if not categorized_items:
                print("Item list is empty")
            else:
                remove_item(categorized_items, categories)
            continue
        if item == "":
            if input("Are you sure you want to check out? (y/n) ").lower() == "y":
                break
            else:
                continue
        
        available = False
        for category, items in categories.items():
            if item in items:
                available = True
                categorized_items.setdefault(category, {}).setdefault(item, 0)
                categorized_items[category][item] += items[item]
        
        if not available:
            print("Item unavailable in the store")
            continue
    
    display_receipt(categorized_items, shopper_id)

if __name__ == "__main__":
    main()
