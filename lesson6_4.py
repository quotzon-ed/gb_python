# from tkinter import N


class Car:
  def __init__(self, s, c, n, p):
    self.speed = s
    self.color = c
    self.name = n
    self.is_police = p
    print(f"Добро пожаловать в автомобиль {self.name}, цвет {self.color}.")
    if self.is_police == False:
      print("Данный автомобиль НЕ является полицейской машиной. Поэтому Вам придется соблюдать ПДД.")
    else:
      print("У Вашей машины преимущество. Вы можете включить мигалку и сирену. ")
  def go(self):
    if self.speed > 0:
      print("Вы успешно тронулись с места.")
    else:
      print("Для того, чтобы сдвинуться с места, нажмите на педаль газа.")
  def stop(self, stop_speed):
    self.speed = stop_speed
    if self.speed == 0:
      print("Вы остановились.")
    else:
      print("Ваша скорость не равна 0 км/ч. Похоже, что Вы продолжаете движение. Видимо неисправна тормозная система. Направляйтесь в ближайший автомобильный сервис. И желаем Вам удача!")
  def turn(self, dir):
    print(f"Вы движетесь на {dir}.")
  def show_speed(self, speed):
    if self.is_police == False:
      print(f"Вы движетесь со скоростью {speed} км/ч.")
    else:
      print(f"Вы движетесь со скоростью {speed} км/ч. Допустимая максимальная скорость на данному участке составляет ")
class TownCar(Car):
  def show_speed(self):
    max_speed = 60
    if self.speed > max_speed:
      print(f"Ваша скорость {self.speed} км/ч выше допустимой скорости {max_speed} км/ч на {self.speed - max_speed} км/ч. Снизьте пожалуйста скорость.")
    else:
      print(f"Вы движетесь со скоростью {self.speed} км/ч.")
class SportCar(Car):
  def show_speed(self):
    max_speed = 80
    if self.speed > max_speed:
      print(f"Ваша скорость {self.speed} км/ч выше допустимой скорости {max_speed} км/ч на {self.speed - max_speed} км/ч. Снизьте пожалуйста скорость.")
    else:
      print(f"Вы движетесь со скоростью {self.speed} км/ч.")
class WorkCar(Car):
  def show_speed(self):
    max_speed = 40
    if self.speed > max_speed:
      print(f"Ваша скорость {self.speed} км/ч выше допустимой скорости {max_speed} км/ч на {self.speed - max_speed} км/ч. Снизьте пожалуйста скорость.")
    else:
      print(f"Вы движетесь со скоростью {self.speed} км/ч.")
class PoliceCar(Car):
  def show_speed(self):
    max_speed = 40
    if self.speed > max_speed:
      print(f"Ваша скорость {self.speed} км/ч выше допустимой скорости {max_speed} км/ч на {self.speed - max_speed} км/ч. И Вам ничего за это не будет)")
    else:
      print(f"Вы движетесь со скоростью {self.speed} км/ч.")

t_car = TownCar(60, "Зеленый", '"Antilopa"', False)
t_car.go()
t_car.turn("Юг")
t_car.show_speed()
t_car.stop(0)

s_car = SportCar(100, "Желтый", "Ferrari", False)
s_car.go()
s_car.turn("Север")
s_car.show_speed()
s_car.stop(20)

w_car = WorkCar(60, "Черный", "Toyota Camry", False)
w_car.go()
w_car.turn("Запад")
w_car.show_speed()
w_car.stop(0)

p_car = PoliceCar(100, "Полицейский", "Ford Focus", True)
p_car.go()
p_car.turn("Восток")
p_car.show_speed()
p_car.stop(0)

