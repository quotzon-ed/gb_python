#Можно было создать список одной строкой. Но мне нагляднее больше нравится. Это конечно не тот вариант, который потребуется "в бою", но в учебе, думаю, можно для наглядности и так оставить
elem_1 = 8
elem_2 = 8.6
elem_3 = True
elem_4 = 5 + 6j
elem_5 = None
elem_6 = [200, "some text", 40.3648, None, False]
elem_7 = ("some text", 68, 8947.6528748, None, True)
elem_8 = set("48 parrots is here!")
elem_9 = frozenset("48 parrots is here!")
elem_10 = {'age': 37, 'sex': 'male', 'name': 'Denis'}
elem_11 = "It's a stroke!"
elem_12 = bytes('sometext', encoding = 'utf-8')
elem_13 = bytearray(b"some text")

elements = (elem_1, elem_2, elem_3, elem_4, elem_5, elem_6, elem_7, elem_8, elem_9, elem_10, elem_11, elem_12, elem_13)

for i in elements:
  print(type(i))