def f_sum(row):
  row = row.split()
  d_sum = 0
  err = False
  for word in row:
    if word.isdigit():
      d_sum += int(word)
    elif word == 'q':
      return [d_sum, word]
    else:
      err = True
  return [d_sum, err]

e_sum = 0
while True:
  t_row = input("Enter some symbols: ")
  if f_sum(t_row)[1] == False:
    e_sum += f_sum(t_row)[0]
    print(f"{f_sum(t_row)[0]} ({e_sum})")
  elif f_sum(t_row)[1] == 'q':
    e_sum += f_sum(t_row)[0]
    print(f"{f_sum(t_row)[0]} ({e_sum})")
    break
  else:
    e_sum += f_sum(t_row)[0]
    print(f"Error\n{f_sum(t_row)[0]} ({e_sum})")