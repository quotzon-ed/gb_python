with open("text_5.txt", "w+", encoding="utf-8") as f_obj:
  f_obj.write(input("Введите несколько чисел через пробел и нажмите Enter:\n"))
  f_obj.seek(0)
  content = f_obj.read()
summa = 0
for nums in content.split():
  summa += int(nums)
print(summa)