from menu import *
from behave import given, then, when, step
import sys

menu = [
  "Kung Pao Chicken", "Beef and Broccoli", "Spring Rolls", "Hot and Sour Soup",
  "Mango Pudding", "Margherita Pizza", "Spaghetti Carbonara",
  "Chicken Piccata", "Caprese Salad", "Tiramisu", "Ceviche", "Locro de Papa",
  "Llapingachos", "Dry Chicken", "Enoniondo"
]

special_category_meals = ["Margherita Pizza", "Tiramisu"]

meal_prices = {
  "Kung Pao Chicken": 8,
  "Beef and Broccoli": 9,
  "Spring Rolls": 4,
  "Hot and Sour Soup": 6,
  "Mango Pudding": 5,
  "Margherita Pizza": 10,
  "Spaghetti Carbonara": 12,
  "Chicken Piccata": 11,
  "Caprese Salad": 7,
  "Tiramisu": 8,
  "Ceviche": 13,
  "Locro de Papa": 9,
  "Llapingachos": 6,
  "Dry Chicken": 10,
  "Enoniondo": 12
}

order = {}
option = None

#@selectOneFood
@given('a menu with dishes available')
def setp_impl(context):
  display_menu()


@when(
  'the user select a food index {index}, {quantity_user} in quantity and finish the order with {finish_word}'
)
def setp_impl(context, index, quantity_user, finish_word):
  responses = [index, finish_word]
  i = 0
  global order
  order = {}
  for i in range(len(responses)):
    print("-------------------------")
    selection = responses[i]

    if selection.lower() == 'finish':
      break

    if not selection.isdigit() or int(selection) <= 0 or int(selection) > len(
        menu):
      print("invalid meal")
      continue

    selection = int(selection)
    meal_name = menu[selection - 1]

    quantity_selection = quantity_user
    quantity = validate_quantity(quantity_selection)

    if quantity is None:
      continue

    order[meal_name] = quantity

  if not order:
    print("You canceled the order.")
    return -1


@then('the expected output should contains {expected_output}')
def setp_impl(context, expected_output):

  str_response = ""

  global order
  str_response += "\n--------"
  total_cost = calculate_total_cost(order)
  for meal, quantity in order.items():
    str_response += f"{quantity} {meal}(s) - ${meal_prices[meal]:.2f} each"

  str_response += f"\nTotal Cost: ${total_cost:.2f}"
  print(str_response)

  assert expected_output.strip() in str_response.strip(), "fail"


#@cancelOrder
@given("a menu with some dishes")
def setp_impl(context):
  display_menu()


@when("the user writes {finish_word} without ordering any food")
def setp_impl(context, finish_word):
  responses = [finish_word]
  i = 0
  global order
  order = {}
  for i in range(len(responses)):
    print("-------------------------")
    selection = responses[i]

    if selection.lower() == 'finish':
      break

    if not selection.isdigit() or int(selection) <= 0 or int(selection) > len(
        menu):
      print("invalid meal")
      continue

    selection = int(selection)
    meal_name = menu[selection - 1]

    quantity_selection = quantity_user
    quantity = validate_quantity(quantity_selection)

    if quantity is None:
      continue

    order[meal_name] = quantity


@then("the expected output should be {cancel_phrase}")
def setp_impl(context, cancel_phrase):
  str_response = ""

  global order

  if not order:
    str_response += "You canceled the order."
    return -1

  assert cancel_phrase.strip() in str_response.strip(), "fail"


#@selectChefsSpecial
@given("a menu with Chef's Specials")
def setp_impl(context):
  display_menu()


@when("the user picks a Chef's special and looks forward to pay a single unit")
def setp_impl(context):
  global option
  global order
  order = {}
  option = menu[9]
  order[option] = 1


@then("the price should present a 5% surcharge")
def setp_impl(context):
  global order
  price = calculate_total_cost(order)
  assert price == 5.25, "Surcharge has not been applied correctly"


#@bigDiscount
@given("a menu with some dishes available")
def setp_impl(context):
  display_menu()


@when("the user orders {quantity} units of any normal dish")
def setp_impl(context, quantity):
  global option
  global order
  order = {}
  option = menu[2]
  order[option] = int(quantity)


@then("the price should be {expectedPrice} dollars")
def setp_impl(context, expectedPrice):
  global order
  price = calculate_total_cost(order)
  assert int(price) == int(
    expectedPrice), "Discount has not been applied correctly"
