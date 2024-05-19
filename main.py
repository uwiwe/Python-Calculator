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
  
  def addition(n1, n2):
    return round(n1 + n2, 2)
  
  def sustraction(n1, n2):
    return round(n1 - n2, 2)
  
  def multiplication(n1, n2):
    return round(n1 * n2, 2)
  
  def division(n1, n2):
    return round(n1 / n2, 2)
  
  if oper == "+":
    result = addition(n1, n2)
  elif oper == "-":
    result = sustraction(n1, n2)
  elif oper == "*":
    result = multiplication(n1, n2)
  elif oper == "/":
    result = division(n1, n2)

  print(f"{n1} {oper} {n2} = {result}")
  
  continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  if continue_calculating == "n":
    result = None
    clear()