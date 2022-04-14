f_obj = open("lesson5_1.txt", "w", encoding="utf")
user_words = input("Напишите несколько слов и нажмите Enter:\n").split()
for el in user_words:
  f_obj.writelines(el + "\n")
f_obj.close()