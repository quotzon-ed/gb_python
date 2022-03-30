n = input("Enter a number greater than 0:\n")
while n < '0':
  print("I've asked for number greater than 0! Please try again!")
  n = input("Please, enter a number greater than 0:\n")
n_2 = int(n * 2)
n_3 = int(n * 3)
n = int(n)
print(f"{n} + {n_2} + {n_3} = {n + n_2 + n_3}")
#4 строки выше можно заменить за более красивую запись в 1 строку:
#print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")