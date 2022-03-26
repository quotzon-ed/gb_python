profit = int(input("What is the firm's profit?\n"))
expenses = int(input("What is the firm's expenses?\n"))
if profit > expenses:
  print("The company is profitable!")
  print(f"Rentability of company is {(profit / expenses):.2f}")
  employees = int(input("Number of company employees:\n"))
  print(f"Profit per 1 employee is {(profit / employees):.2f}")
else:
  print("The company is operating at a loss!")