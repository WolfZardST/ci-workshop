def display_menu():
    print("Welcome!")
    print("--------- Menu ---------")
    print("--- CHINESE FOOD ---")
    print("1. Kung Pao Chicken - $8")
    print("2. Beef and Broccoli - $9")
    print("3. Spring Rolls - $4")
    print("4. Hot and Sour Soup - $6")
    print("5. Mango Pudding - $5")
    print("--- ITALIAN FOOD ---")
    print("6. Margherita Pizza - $10")
    print("7. Spaghetti Carbonara - $12")
    print("8. Chicken Piccata - $11")
    print("9. Caprese Salad - $7")
    print("10. Tiramisu - $8")
    print("--- ECUADORIAN FOOD ---")
    print("11. Ceviche - $13")
    print("12. Locro de Papa - $9")
    print("13. Llapingachos - $6")
    print("14. Dry Chicken - $10")
    print("15. Enoniondo - $12")
    print("-------------------------")
    print("The Chef's Specials are Tiramisu and Margherita Pizza")

def validate_quantity(user_quantity):
    try:
        quantity = int(user_quantity)
        if quantity > 0 and quantity <= 100:
            return quantity
        else:
            print("Please enter a positive integer between 1 and 100.")
            return -1
    except ValueError:
        print("Please enter a positive integer between 1 and 100.")
        return -1

def calculate_total_cost(order):
    base_cost = 5

    total_quantity = sum(order.values())
    total_cost = 0

    for meal, quantity in order.items():
        if meal in special_category_meals:
            total_cost += (base_cost + base_cost * 0.05) * quantity
        else:
            total_cost += base_cost * quantity

    if total_quantity > 10:
        total_cost *= 0.8
    elif total_quantity > 5:
        total_cost *= 0.9

    if total_cost > 100:
        total_cost -= 25
    elif total_cost > 50:
        total_cost -= 10

    return total_cost

def dining_experience_manager():
    order = {}
    while True:
        display_menu()
        print("-------------------------")
        selection = input("What do you want to order? If not, then type finish: ")

        if selection.lower() == 'finish':
            break

        if not selection.isdigit() or int(selection) <= 0 or int(selection) > len(menu):
            print("invalid meal")
            continue

        selection = int(selection)
        meal_name = menu[selection - 1]

        quantity_selection = input(f"How many {meal_name}(s) do you want to order? ")
        quantity = validate_quantity(quantity_selection)

        if quantity is None:
            continue

        order[meal_name] = quantity

    if not order:
        print("You canceled the order.")
        return -1

    print("\n--------")
    total_cost = calculate_total_cost(order)
    for meal, quantity in order.items():
        print(f"{quantity} {meal}(s) - ${meal_prices[meal]:.2f} each")

    print(f"\nTotal Cost: ${total_cost:.2f}")

menu = [
        "Kung Pao Chicken", "Beef and Broccoli", "Spring Rolls", "Hot and Sour Soup", "Mango Pudding",
        "Margherita Pizza", "Spaghetti Carbonara", "Chicken Piccata", "Caprese Salad", "Tiramisu",
        "Ceviche", "Locro de Papa", "Llapingachos", "Dry Chicken", "Enoniondo"
]

special_category_meals = ["Margherita Pizza", "Tiramisu"]

meal_prices = {
        "Kung Pao Chicken": 8, "Beef and Broccoli": 9, "Spring Rolls": 4, "Hot and Sour Soup": 6, "Mango Pudding": 5,
        "Margherita Pizza": 10, "Spaghetti Carbonara": 12, "Chicken Piccata": 11, "Caprese Salad": 7, "Tiramisu": 8,
        "Ceviche": 13, "Locro de Papa": 9, "Llapingachos": 6, "Dry Chicken": 10, "Enoniondo": 12
}

#total_cost = dining_experience_manager()
