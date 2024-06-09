import art
from replit import clear
print(art.logo)

continue_calculations = True
result = None

while continue_calculations:
  if result != None:
    n1 = result
  else:
    n1 = float(input("What's the first number?: "))
  oper = input("Pick an operation: + - * / \n")
  n2 = float(input("What's the second number?: "))
  
  operations = {
    "+": n1 + n2,
    "-": n1 - n2,
    "*": n1 * n2,
    "/": n1 / n2
  }

  if oper in operations:
    result = operations[oper]
    print(f"{n1} {oper} {n2} = {result}")
  else:
    print(f"Sorry, I can't use {oper}.")
  
  continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  if continue_calculating == "n":
    result = None
    clear()