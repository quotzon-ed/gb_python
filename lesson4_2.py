from random import randint

my_list = []
for k in range(15):
  my_list.append(randint(1, 1000))
print(my_list)
new_list = [my_list[el+1] for el in range(len(my_list) - 1) if my_list[el+1] > my_list[el]]
print(new_list)