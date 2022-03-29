my_name = "Denis"
my_age = 36
print(f"My name's {my_name}. I'm {my_age} years old.")
name = input("What is your name?\n")
age = int(input("How old are you?\n"))
diff_age = my_age - age;
if diff_age > 0:
  print(f"Hello, {name}! You're {age} old. And I'm {diff_age} years older than you.")
elif diff_age == 0:
  print(f"Hello, {name}! You're {age} old. And we're the same age.")
else:
  diff_age = -1 * diff_age
  print(f"Hello, {name}! You're {age} old. And I'm {diff_age} years younger than you.")
