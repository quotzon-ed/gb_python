from random import randint

my_list = [randint(21, 32) for _ in range(20)]
# result_list = [el for el in my_list if my_list.count(el) == 1]
print(my_list)
# print(result_list)

#Another solution

print(a := [randint(0, 9) for _ in range(20)], [i for i in a if a.count(i) == 1], sep = '\n')

#Optimization

my_dict = {i: 0 for i in my_list}

for i in my_list:
  my_dict[i] += 1

print([i for i in my_dict if my_dict[i] == 1])