words = input("Enters some words separated by ' ':\n").split() # Предлагаем пользователю ввести несколько слов, разделенных пробелами и сразу создаем из предложения список из отдельных слов

# Вариант 1 (оставил на будущее, чтобы видеть, как делать не надо). Хоть вариант и рабочий
print("\n\nVersion 1.0")
n = 1
for i in words: 
  if len(i) > 10:
    print(f"{n}. {i[0:10]}")
  else:
    print(f"{n}. {i}")
  n += 1

#Вариант 2 - верный
print("\n\nVersion 2.0")
for num, i in enumerate(words):
  print(f"{num + 1}. {i[0:10]}")