def f_sup_easy(x, y):
  return x**y

def f_sup_medium(x, y):
  comp = x
  for n in range((abs(y) - 1)):
    comp *= x
  return 1 / comp

sub = int(input("Enter a positive number: "))
sup = int(input("Enter a negative number: "))
while sub < 0 or sup > 0:
  sub = int(input("Try again!\nEnter a positive number: "))
  sup = int(input("Enter a negative number: "))
print(f_sup_easy(sub, sup))
print(f_sup_medium(sub, sup))