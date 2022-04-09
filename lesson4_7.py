def fact(n):
  for el in range(1, n + 1):
    yield el
number = int(input("Введите целое число: "))
factorial = 1
for v in fact(number):
  factorial = factorial*v
print(factorial)