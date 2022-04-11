from functools import reduce

def f_prod(val_1, val_2):
  return val_1 * val_2

# Not cool:

# even_list = [val for val in range(100, 1001) if val % 2 == 0]

# Cool:

even_list = [val for val in range(100, 1001, 2)]

print(even_list)
print(reduce(f_prod, even_list))