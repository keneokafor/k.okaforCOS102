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

# Function to display the order window
def show_order_window():
    order_window = tk.Toplevel(root)
    order_window.title("Place Order")

    # Variables to store selected items and quantities
    selected_items = []
    selected_quantities = []

    def add_to_order():
        item = item_var.get()
        quantity = int(quantity_var.get())

        if item == "":
            messagebox.showerror("Error", "Please select an item from the menu.")
            return

        if quantity <= 0:
            messagebox.showerror("Error", "Please enter a valid quantity.")
            return

        selected_items.append(item)
        selected_quantities.append(quantity)

        # Update order list display
        order_listbox.insert(tk.END, f"{item} x{quantity}")

    def place_order():
        if not selected_items:
            messagebox.showerror("Error", "No items selected for the order.")
            return

        total_cost = sum(menu[item] * quantity for item, quantity in zip(selected_items, selected_quantities))
        order_summary = "\n".join(f"{item} x{quantity}" for item, quantity in zip(selected_items, selected_quantities))
        order_summary += f"\nTotal Cost: ${total_cost:.2f}"

        messagebox.showinfo("Order Summary", order_summary)
        order_window.destroy()

    # Order window components
    tk.Label(order_window, text="Select Item:").pack()
    item_var = tk.StringVar(order_window)
    item_var.set("")  # default value

    item_option = tk.OptionMenu(order_window, item_var, *menu.keys())
    item_option.pack()

    tk.Label(order_window, text="Quantity:").pack()
    quantity_var = tk.StringVar(order_window, value="1")
    quantity_entry = tk.Entry(order_window, textvariable=quantity_var)
    quantity_entry.pack()

    add_button = tk.Button(order_window, text="Add to Order", command=add_to_order)
    add_button.pack()

    order_listbox = tk.Listbox(order_window, height=10, width=40)
    order_listbox.pack()

    place_order_button = tk.Button(order_window, text="Place Order", command=place_order)
    place_order_button.pack()

# Main window (Menu display)
root = tk.Tk()
root.title("PAU CAFETERIA")

menu_label = tk.Label(root, text="Welcome to PAU CAFETERIA!!!")
menu_label.pack()

menu_label = tk.Label(root, text="MENU:")
menu_label.pack()

for item in menu:
    tk.Label(root, text=f"{item}: ${menu[item]:.2f}").pack()

order_button = tk.Button(root, text="Place Order", command=show_order_window)
order_button.pack()

root.mainloop()
