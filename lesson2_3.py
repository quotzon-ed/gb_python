list_of_seasons = ['winter', 'spring', 'summer', 'autumn'] # Создаем список с временами года
dict_of_months = {1: list_of_seasons[0], 2: list_of_seasons[0], 3: list_of_seasons[1], 4: list_of_seasons[1], 5: list_of_seasons[1], 6: list_of_seasons[2], 7: list_of_seasons[2], 8: list_of_seasons[2], 9: list_of_seasons[3], 10: list_of_seasons[3], 11: list_of_seasons[3], 12: list_of_seasons[0]} # Создаем словарь, в котором каждому номеру месяца присваиваем ключ, а к ключу - название времени года из списка выше
month = int(input("Please enter a number of a month:\n")) # Предлагаем ввести номер
while month < 1 or month > 12: # Если введено не число между 0 и 13, то предлагаем ввести его заново
  month = int(input("This value is not correct! Please enter a number from 1 to 12:\n"))
print(f"This season is {dict_of_months.get(month)}") # выводим название времени года согласно словарю