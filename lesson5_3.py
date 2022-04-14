with open("text_3.txt", "r", encoding="utf-8") as f_obj:
  my_list = f_obj.read().split()
all_salaries = 0
n = 0
print("Сотрудники, зарплата которых выше 20000 руб:")
for el in range(1, len(my_list) + 1, 2):
  all_salaries += float(my_list[el])
  if float(my_list[el]) >= 20000:
    print(my_list[el-1])
  n += 1
print(15*"-")
print(f"Средняя зарплата сотрудников в компании: {round((all_salaries/n), 1)}")
