from replit import clear
import art



# add
def add(n1, n2):
  return n1 + n2
#subtract
def subtract(n1, n2):
  return n1-n2
#Multiply
def multiply(n1, n2):
  return n1*n2
#Divide
def divide(n1,n2):
  return n1/n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  print(art.logo)
  num1 = float(input("what's the first number?: "))
  go = "y"
  while go == "y":
    for operation in operations:
      print(operation)
    pick = input("Pick an operation symbol above: ")
    num2 = float(input("what's the next number?:"))
    answer = operations[pick](num1,num2)
    print(f"{num1} {pick} {num2} = {answer}")
    go = input("type 'y' to continue calculating, type 'n' to start a new calculating, or type 'off' to switch off the calculator: \n")
    if go == "y":
      num1 = answer
    elif go == 'n':
      clear()
      calculator()
      
    else:
      clear()
      print(art.logo)
      print("You switched off the calculator\nGoodBye!")
      
    
calculator()
