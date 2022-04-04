def f_sum(v_1, v_2, v_3):
  v_set = sorted([v_1, v_2, v_3])
  return v_set[1] + v_set[2]

try:
  arg_1 = int(input("Enter first number: "))
  arg_2 = int(input("Enter second number: "))
  arg_3 = int(input("Enter third number: "))
  print(f_sum(arg_1, arg_2, arg_3))
except (ValueError, ZeroDivisionError) as err:
    print(err)