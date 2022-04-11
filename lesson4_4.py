from random import randint

my_list = []
for k in range(25):
  my_list.append(randint(21, 32))

result_list = [my_list[g] for g in range(len(my_list)) if my_list.count(my_list[g]) == 1]
print(my_list)
print(result_list)