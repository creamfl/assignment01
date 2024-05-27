from extras.desc import decrement
from swap import swapper

try:
  num1 = int(input("enter number from 0-3:"))
  num2 = int(input("enter a number from 0-3:"))
  print(swapper(num1, num2))

  descending = int(input("enter a number to decrement from it:"))
  decrement(descending)
except ValueError as err:
  print(f"error {err}")
else:
  print("good job") 
finally:
  print("you are the best!")
