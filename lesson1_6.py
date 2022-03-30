a = int(input("Type start distance value:\n")) #Правильнее все же преобразовывать в float, т.к. далее все равно будет расчет в числах с плавающей точкой. То же касается и следующей строки
b = int(input("Type end distance value:\n"))
duration = 1
print(f"Day {duration} - {a} km.")
while a < b:
  duration += 1
  a = 1.1 * a
  print(f"Day {duration} - {a:.3f} km.")
print(f"The result of {b} km was achieved on the {duration}th day")