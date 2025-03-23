# prompt: Project 7: Password Generator Python Project

import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
  """Generates a random password.

  Args:
    length: The desired length of the password.
    include_uppercase: Whether to include uppercase letters.
    include_numbers: Whether to include numbers.
    include_symbols: Whether to include symbols.

  Returns:
    A randomly generated password.
  """

  characters = string.ascii_lowercase
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  password = ''.join(random.choice(characters) for i in range(length))
  return password

if __name__ == '__main__':
  while True:  # Loop until a valid input is received
    try:
      password_length = int(input("Enter desired password length: "))
      break  # Exit loop if input is a valid integer
    except ValueError:
      print("Invalid input. Please enter a number for the password length.")

  use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
  use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
  use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

  password = generate_password(password_length, use_uppercase, use_numbers, use_symbols)
  print("Generated password:", password) 