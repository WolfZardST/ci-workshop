from menu import validate_quantity, calculate_total_cost

def test_quantity():
    assert validate_quantity("5") == 5

def test_calculate_total_cost():
    assert calculate_total_cost({'Mango Pudding': 2, 'Margherita Pizza': 1, 'Spaghetti Carbonara': 3}) == 27.225