with open("text_4.txt", "r", encoding="utf-8") as f_obj:
  f_content = f_obj.readlines()
print(f"Количество строк в файле - {len(f_content)}")
n = 1
for el in f_content:
  print(f"Слов в {n} строке - {len(el.split())}.")
  n += 1