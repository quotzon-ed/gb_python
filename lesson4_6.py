from itertools import count
from itertools import cycle
from itertools import islice

try:
  k = int(input("Введите начальное целое число: "))
except ValueError:
  print("Необходимо ввести целое число!")
count_list = [v for v in islice(count(k), 20)]
print(count_list)
print(*islice(cycle(count_list), 15))