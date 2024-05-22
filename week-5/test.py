import tkinter as tk
from tkinter import messagebox

# Menu dictionary with food items and their prices
menu = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Salad": 4.99,
    "Fries": 2.49,
    "Soda": 1.50
}

def place_order():
    name = name_entry.get()
    item = item_var.get()
    quantity = int(quantity_entry.get())
    
    if item == "":
        messagebox.showerror("Error", "Please select an item from the menu.")
        return
    
    if name == "" or quantity <= 0:
        messagebox.showerror("Error", "Please enter a valid name and quantity.")
        return
    
    price = menu[item]
    total_cost = price * quantity
    
    # Display order summary in a new window
    order_summary = f"Name: {name}\nItem: {item}\nQuantity: {quantity}\nTotal Cost: ${total_cost:.2f}"
    messagebox.showinfo("Order Summary", order_summary)

# Create main window
root = tk.Tk()
root.title("Food Order System")

# Name entry
tk.Label(root, text="Your Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Item selection
tk.Label(root, text="Select Item:").pack()
item_var = tk.StringVar(root)
item_var.set("")  # default value

item_option = tk.OptionMenu(root, item_var, *menu.keys())
item_option.pack()

# Quantity entry
tk.Label(root, text="Quantity:").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Place Order Button
order_button = tk.Button(root, text="Place Order", command=place_order)
order_button.pack()

root.mainloop()
