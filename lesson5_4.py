with open("text_4.txt", "r", encoding="utf-8") as f_obj:
  my_data = f_obj.readlines()
lang_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
for el in my_data:
  el = el.split()
  el[0] = lang_dict.get(el[0])
  print(" ".join(el))
