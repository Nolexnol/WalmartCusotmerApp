#Gets the name of an item
def get_item():
    while True:
        item_name = input("Enter item name to add to cart (enter 'rem' to remove item or press 'Enter' to check out.): ")
        if item_name == "" or item_name.lower() == "rem":
            return item_name
        elif item_name.isdigit():
            print("Invalid input. Item name cannot be only numbers. Please try again.")
        else:
            return item_name
    
#Gets and validates the price of a corresponding item
def get_price():
    while True:
        try:
            b = float(input("Enter the price of the item in USD: $"))
            if b < 0:
                raise ValueError()
        except ValueError:
            print("Invalid value for item price. Price has to be above 0.")
        else:
            return b
    
#Removes an item and its corresponding price from the lists
def remove_item(items,prices,priceAftertax,categorized_items):
        r_item = input("Enter the name of the item that you want to remove: ")
        if r_item not in items:
            print("Item is not in list")
        elif input("Would you like to remove the entered item?(y/n) ").lower() == "y":
            i = items.index(r_item)
            items.pop(i)
            prices.pop(i)
            priceAftertax.pop(i)
            print("Item has been removed.")
        
        for category, values in categorized_items.items():
            if r_item in values:
                if len(values) == 1:
                    categorized_items.pop(category)
                else:
                    values.remove(r_item)
                break

#Calculates price plus tax
def calculate_new_price(price):
    new_price = price*(1.1044)
    return new_price

#Self-explanatory
def display_receipt(items,prices,p_tax,categorized_items):
    total = sum(p_tax)
    tax = total-sum(prices)
    print("="*60)
    print(f"Number of items purchased: {len(items)}")
    print("="*60)
    print(f"{'Category':<20} | {'Item':<20} | {'Price'}")
    print("-"*60)
    for category,values in categorized_items.items():
        print(f"{category:<20} |")
        for item in values:
            i = items.index(item)
            print(f"{'':<20} | {item:<20} | {prices[i]}")
        print("-"*60)
    print("="*60)
    print(f"{'Tax':<20} |  ${tax:.2f}")
    print(f"{'Total':<20} |  ${total:.2f}")
    addToDatabase(items, prices, categorized_items)

def addToDatabase(items,prices,categorized_items):
    file_path = r"C:\Users\dejhs\OneDrive\Desktop\DSALab\WalmartCusotmerApp\Storage.csv"
    storage_file = open(file_path,"w+")
    storage_file.write("ITEM NAMES,")
    for item in items:
        storage_file.write(item+",")
    storage_file.write('\n'+"PRICES,")
    for price in prices:
        storage_file.write(str(price)+",")
    storage_file.write('\n')
    storage_file.close()


def main():
    print("Welcome to Walmart. Please follow the instructions to make your shopping experience successful.")
    print("To remove an item from your list, enter 'rem'")
    print("Once you are done adding things to cart, leave blank and press 'Enter'to checkout")
    print("="*100)
    taxed_prices = []
    items = []
    prices = []
    categorized_items = {}
    categories = {
    "Groceries":{"meat":3.00, "milk":4.00, "bread":2.00, "eggs":3.00, "cheese":1.00},
    "Home products": {"sofa":1000.00, "lamp":150.00, "curtains":100.00, "vase":50.00, "shelves":250.0},
    "Electronics": {"laptop":2000.00, "headphones":100.00, "smartphone":700.00, "camera":5000.00, "tv":1500.00},
    "Clothing": {"t-shirt":20.00, "jeans":30.00, "jacket":40.00, "socks":10.00, "hat":35.00},
    "Toys": {"lego set":50.00, "action figure":70.00, "doll": 35.00, "puzzle":7.99, "bicycle":269.99}
    }
    
    
    while True:
       #Gets item and checks if user wants to remove or add an item
        item = get_item()
        available = False
        if item == "rem":
            if not items:
                print("Item list is empty")
            else:
                remove_item(items,prices,taxed_prices,categorized_items)
                print(categorized_items)
            continue
        if item == "":
            if input("Are you sure you want to check out?(y/n) ").lower() == "y":
                break
            else:
                continue
        
        #Checks if item is in category and appends items to list
        for key, values in categories.items():
            if item in values:
                available = True
                items.append(item)
        if not available:
            print("item unavailable in the store")
            continue
        
        #Gets and appends price and tax to lists
        price = get_price()
        prices.append(price)
        taxed_prices.append(calculate_new_price(price))
        
    #Categorizes items list
    for item in items:
        for category,values in categories.items():
            if item in values:
                if category in categorized_items:
                    categorized_items[category].append(item)
                else:
                    categorized_items[category] = [item]
    
    #displays receipt as neatly formatted table
    display_receipt(items,prices,taxed_prices,categorized_items)
    print("\nThank you for shopping at Walmart.")


if __name__ == "__main__":
    main()
    
