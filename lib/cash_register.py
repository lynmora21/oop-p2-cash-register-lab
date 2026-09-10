#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    # Set the starting values for the cash register.
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    # Only allow whole-number discounts from 0% through 100%.
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")

  def add_item(self, item, price, quantity=1):
    # Add the item's total price to the register.
    self.total += price * quantity

    # Store each item separately when multiple quantities are purchased.
    self.items.extend([item] * quantity)

    # Save the transaction so it can be tracked later.
    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })

  def apply_discount(self):
    # A discount cannot be applied when there is no total.
    if self.total == 0:
      print("There is no discount to apply.")
      return

    # Calculate and subtract the percentage discount.
    self.total = self.total - (self.total * self.discount / 100)

    # Display the customer's new total.
    print(f"After the discount, the total comes to ${self.total:.0f}.")

  def void_last_transaction(self):
    # There is nothing to void if there are no transactions.
    if len(self.previous_transactions) == 0:
      print("There is no transaction to void.")
      return

    # Remove the most recent transaction and subtract its cost.
    transaction = self.previous_transactions.pop()
    self.total -= transaction["price"] * transaction["quantity"]

    # Remove the corresponding items from the items list.
    self.items.pop()

