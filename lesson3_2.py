def user_data(*args):
  result = ''
  for data in args:
    result += data + ' '
  return result

first_name = input("Enter your name: ")
second_name = input("Enter your surname: ")
year = input("Enter year of your birthday: ")
city = input("Enter your city: ")
email = input("Enter your email: ")
phone = input("Enter your phone: ")

print(user_data(first_name, second_name, year, city, email, phone))