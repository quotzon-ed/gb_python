def fact(n):
  for el in range(1, n + 1):
    yield el
try:
  number = int(input("Введите целое число: "))
except ValueError:
  print("Необходимо ввести целое число!")
factorial = 1
for v in fact(number):
  factorial = factorial*v
print(factorial)