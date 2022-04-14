import json

with open("text_7.txt", "r", encoding="utf-8") as f_obj:
  content = f_obj.readlines()
all_data = [data.split() for data in content]
my_dict = {el[0]: (int(el[2]) - int(el[3])) for el in all_data}
a_profit = 0
n = 0
for profit in my_dict.values():
  if profit >= 0:
    a_profit += profit
    n += 1
my_list = [my_dict, {"average_profit": a_profit / n}]
print(my_list)
with open("text_7.json", "w", encoding="utf-8") as j_obj:
  j_obj.write(json.dumps(my_list, sort_keys=True, indent=2))