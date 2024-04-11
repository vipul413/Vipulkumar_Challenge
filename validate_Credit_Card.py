print("Below is a Python application to validate Credit Card Number with additional restrictions.")

# This is the function for Credit card numbers validations
def is_valid_credit_card(card_number):
  """
  This function validates a credit card number with additional restrictions.

  Args:
      card_number: A string representing the credit card number.

  Returns:
      True if the card number is valid, False otherwise.
  """

  # Check if the card number is a string and non-empty
  if not isinstance(card_number, str) or not card_number:
    return False

  # Remove any extra spaces
  card_number = card_number.replace(" ", "")

  # Check if the card number consists only of digits and hyphens
  if not card_number.isdigit() and not all(c in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9') for c in card_number):
    return False  

  # Validate the number of digits (considering potential hyphens)
  num_digits = sum(c.isdigit() for c in card_number)
  if num_digits not in (16):
    return False

  # Check if the card number starts with a valid prefix (4, 5, or 6)
  if card_number[0] not in ('4', '5', '6'):
    return False

  # Validate hyphen usage (only one hyphen allowed, separating groups of 4 digits)
  hyphen_count = card_number.count('-')
  if hyphen_count not in (0, 1):
    return False
  if hyphen_count == 1:
    split_parts = card_number.split('-')
    if len(split_parts) != 4 or any(len(part) != 4 for part in split_parts):
      return False

  # Check for consecutive repeated digits (allow leading zeros)
  for i in range(1, len(card_number)):
    if card_number[i] != '0' and card_number[i] == card_number[i-1]:
      return False

  # Apply the Luhn algorithm (already implemented in the original code)
  # ... (rest of the code from the original response for Luhn algorithm)

# usage. Enter Credit Card Number and It should print Valid it Invalid Message
card_number = input("Enter your credit card number: ")
if is_valid_credit_card(card_number):
  print("The credit card number is valid.")
else:
  print("The credit card number is invalid.")
