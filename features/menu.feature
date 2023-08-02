Feature: Menu Food

@selectOneFood
Scenario: Select one food
  Given a menu with dishes available
  When the user select a food index 14, 3 in quantity and finish the order with finish 
  Then the expected output should contains Total Cost: $15.00

@cancelOrder
Scenario: User cancel the order without ordering any food
  Given a menu with some dishes
  When the user writes finish without ordering any food
  Then the expected output should be You canceled the order.

@selectChefsSpecial
Scenario: User buys 1 Chef's special
  Given a menu with Chef's Specials
  When the user picks a Chef's special and looks forward to pay a single unit
  Then the price should present a 5% surcharge

@bigDiscount
Scenario: User exceeds $100 and gets two discounts
  Given a menu with some dishes available
  When the user orders 25 units of any normal dish
  Then the price should be 90 dollars