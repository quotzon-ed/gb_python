from sys import argv

file_name, hours, rate, bonus = argv

print(f"Выработка сотрудника в часах: {hours} ч.\nСтавка сотрудника в час: {rate} руб.\nЕжемесячная премия: {bonus} руб.")

try:
  print(f"Оклад сотрудника за текущий месяц: {int(hours) * int(rate) + int(bonus)} руб.")
except (ValueError):
  print("Для расчета оклада должны быть использованы числа, а не буквы!")