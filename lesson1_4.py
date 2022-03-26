number = int(input("Enter a number:\n"))
max = 0
while number != 0 and max != 9:
  next = number%10
  number = number // 10
  if next > max:
    max = next
print(f"Max value is {max}")