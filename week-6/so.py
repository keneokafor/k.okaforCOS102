import tkinter as tk

# Global dictionaries for menu and prices
menu = {
    "Burgers": ["Classic Burger", "Cheeseburger", "Veggie Burger"],
    "Pizza": ["Margherita Pizza", "Pepperoni Pizza", "Vegetarian Pizza"],
    "Salads": ["Caesar Salad", "Greek Salad", "Caprese Salad"],
    "Sides": ["French Fries", "Onion Rings", "Garlic Bread"],
    "Drinks": ["Soda", "Lemonade", "Iced Tea"]
}

prices = {
    "Classic Burger": 5.99,
    "Cheeseburger": 6.49,
    "Veggie Burger": 5.49,
    "Margherita Pizza": 8.99,
    "Pepperoni Pizza": 9.99,
    "Vegetarian Pizza": 8.49,
    "Caesar Salad": 4.99,
    "Greek Salad": 5.49,
    "Caprese Salad": 5.99,
    "French Fries": 2.49,
    "Onion Rings": 3.49,
    "Garlic Bread": 2.99,
    "Soda": 1.50,
    "Lemonade": 1.99,
    "Iced Tea": 1.75
}

def create_menu_display_window():
    root_window = tk.Tk()
    root_window.title("Food Menu")

    # Create two frames for two columns
    left_frame = tk.Frame(root_window)
    left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    right_frame = tk.Frame(root_window)
    right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Display categories and menu items in two columns
    row = 0
    for category in menu.keys():
        label_category = tk.Label(left_frame, text=category, font=("Helvetica", 14, "bold"))
        label_category.grid(row=row, column=0, columnspan=2, pady=(10, 5))
        row += 1

        for index, item in enumerate(menu[category]):
            label_item = tk.Label(left_frame, text=f"{item}: ${prices[item]:.2f}")
            label_item.grid(row=row, column=index % 2, padx=5, pady=5, sticky="w")
            row += 1

    root_window.mainloop()

# Run the main function to create the menu display window
create_menu_display_window()
