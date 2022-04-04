def f_div(div_1, div_2):
  return div_1 / div_2
try:
  v_1 = int(input("Enter the dividend: "))
  v_2 = int(input("Enter the divider: "))
  while v_2 == 0:
    v_2 = int(input("The divider can't be zero. Please try again: "))
  print(f"{v_1} : {v_2} = {f_div(v_1, v_2)}")
except (ValueError, ZeroDivisionError) as err:
    print(err)