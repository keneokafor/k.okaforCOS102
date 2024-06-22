import tkinter as tk
from tkinter import messagebox

# List all the available food items on the menu
menu = {
    "Rice": ["Jollof Rice", "Coconut Fried Rice", "Jollof Spaghetti"],
    "Side Dishes": ["Savoury Beans", "Roasted Sweet Potatoes", "Fried Plantains", "Mixed Vegetable Salad", "Boiled Yam"],
    "Soups and Swallows": ["Eba and Poundo Yam", "Semo", "Atama Soup", "Egusi Soup"],
    "Proteins": ["Sweet Chili Chicken", "Grilled Chicken wings", "Fried Beef", "Fried Fish", "Boiled Egg", "Sauteed Sausages"],
    "Beverages": ["Water", "Glass Drink(35cl)", "PET Drink(35cl)", "PET Drink(50cl)", "Glass/Canned Malt", "Fresh Yo", "Pineapple Juice", "Mango Juice", "Zobo Drink"]
}

# List the prices for all the available food items
prices = {
    "Jollof Rice": 350,
    "Coconut Fried Rice": 350,
    "Jollof Spaghetti": 350,
    "Savoury Beans": 350,
    "Roasted Sweet Potatoes": 300,
    "Fried Plantains": 150,
    "Mixed Vegetable Salad": 150,
    "Boiled Yam": 150,
    "Eba and Poundo Yam": 100,
    "Semo": 100,
    "Atama Soup": 450,
    "Egusi Soup": 480,
    "Sweet Chili Chicken" : 1100,
    "Grilled Chicken wings" : 400,
    "Fried Beef" : 400,
    "Fried Fish" : 500,
    "Boiled Egg" : 200,
    "Sauteed Sausages" : 200,
    "Water" : 200,
    "Glass Drink(35cl)" : 150,
    "PET Drink(35cl)" : 300,
    "PET Drink(50cl)" : 350,
    "Glass/Canned Malt" : 500,
    "Fresh Yo" : 600,
    "Pineapple Juice" : 350,
    "Mango Juice" : 350,
    "Zobo Drink" : 350,
}
# COnfigure your order window
def order_now_window():
    order_now_window = tk.Toplevel(root)
    order_now_window.title("Ticket")

    chosen_fooditem = []
    desired_quantity = []
 

    def add_to_order():
        item = item_var.get()
        amount = int(quantity_var.get())

        if item == "":
            messagebox.showerror("Error", "Please select an item from the menu.")
            return

        if amount <= 0:
            messagebox.showerror("Error", "Please put in a valid quantity.")
            return
        

        chosen_fooditem.append(item)
        desired_quantity.append(amount)

        order_listbox.insert(tk.END, f"{item}: {amount}")


    def order_now():
        if not chosen_fooditem:
            messagebox.showerror("Error", "No food items selected for your ticket.")
            return
        
        # Calculate the total cost
        total_cost = sum(prices[item] * amount for item, amount in zip(chosen_fooditem, desired_quantity))
        order_summary = "\n".join(f"{item} : {amount}pcs " for item, amount in zip(chosen_fooditem, desired_quantity))
        order_summary += f"\nTotal Cost: #{total_cost:.2f}"

        # Add discounts
        if total_cost < 2500:
            returned_cost = total_cost - (total_cost * 0.1) 
        elif total_cost > 2500 and total_cost < 5000:
            returned_cost = total_cost - (total_cost * 0.15)
        elif total_cost > 5000:
            returned_cost = total_cost - (total_cost * 0.25)
        
        # COnfigure your checkout page which will display total prices of food items including added discounts
        order_summary = "\n".join(f"{item} : {amount}pcs" for item, amount in zip(chosen_fooditem, desired_quantity))
        order_summary += f"\nYour Total Cost: ${returned_cost:.2f}"

        messagebox.showinfo("Checkout", order_summary)
        order_now_window.destroy()
    
    # Configure your Ordering window
    tk.Label(order_now_window, text="Select Food item:").pack()
    item_var = tk.StringVar(order_now_window)
    item_var.set(1) 
    # The 1 is a default value. Customers cannot order less than 1 item

    item_option = tk.OptionMenu(order_now_window, item_var, *sorted(prices.keys()))
    item_option.pack()

    tk.Label(order_now_window, text="Quantity:").pack()
    quantity_var = tk.StringVar(order_now_window, value="1")
    quantity_entry = tk.Entry(order_now_window, textvariable=quantity_var)
    quantity_entry.pack()
    
    add_button = tk.Button(order_now_window, text="Add to Ticket", command=add_to_order)
    add_button.pack()

    order_listbox = tk.Listbox(order_now_window, width = 50, height = 30)
    order_listbox.pack()

    place_order_button = tk.Button(order_now_window, text="Complete Order", command=order_now)
    place_order_button.pack()

# Configure the main window which will display the menu 
root = tk.Tk()
root.title("PAU CAFETERIA MENU")

# Configure the features of the text in the main window
for category, items in menu.items():
    tk.Label(root, text=category, font=("Roman", 11,"bold")).pack()
    for item in items:
        price = prices[item]
        tk.Label(root, text=f"{item}: ${price:.2f}").pack()

# configure the Order button
order_button = tk.Button(root, text="Order Now!", command=order_now_window)
order_button.pack()
order_button.config(fg="red", bg="white")

root.mainloop()
