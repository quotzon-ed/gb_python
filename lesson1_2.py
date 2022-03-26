sec = int(input("Enter time in seconds:\n"))
min = sec // 60
sec = sec%60
hour = min // 60
min = min%60
print(f"{hour:02}:{min:02}:{sec:02}")