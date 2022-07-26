# Importing modules from pip
from random_strings import random_string, random_hex

print("PIP Example")

# Handling exceptions
try:
  print("UUID ----->",random_uuid(dashes=False))
except:
  print("You missed the import")


print("RANDOM_HEX ----->",random_hex(128))

quatinty = input("Enter the long for the random str: ")
print("RANDOM_STR ----->",random_string(int(quatinty)))



