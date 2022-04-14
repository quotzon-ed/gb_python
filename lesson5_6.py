with open("text_6.txt", "r", encoding="utf-8") as f_obj:
  content = f_obj.readlines()

my_dict = {el.split(":")[0]: el.strip().split(":")[1] for el in content}
for key in my_dict.keys():
  all_time = 0
  n = 0
  number = ""
  my_val = list(my_dict.get(key))
  for symb in my_val:
    if ord(symb) <= 57 and ord(symb) >= 48:
      number += symb
      if ord(my_val[n + 1]) > 57 or ord(my_val[n + 1]) < 48:
        all_time += int(number)
        number = ""
    n += 1
  my_dict[key] = all_time
print(my_dict)