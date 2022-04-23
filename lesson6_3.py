class Worker:
  def __init__(self, n, s, p, w, b):
    self.name = n.capitalize()
    self.surname = s.capitalize()
    self.position = p
    self.wage = w
    self.bonus = b
    self.income = {"wage": float(self.wage), "bonus": float(self.bonus)}

class Position(Worker):
  def get_full_name(self):
    print(f"Сотрудник {self.surname} {self.name} работает в должности {self.position}")
  def get_total_income(self):
    print(f"Его зарплата, с учетом оклада в {self.income.get('wage')} руб. и премии в {self.income.get('bonus')} руб. составляет {self.income.get('wage') + self.income.get('bonus')} руб.")

e_name = input("Введите имя сотрудника: ")
e_surname = input("Введите фамилию сотрудника: ")
e_position = input("Введите должность сотрудника: ")
e_wage = input("Введите оклад сотрудника: ")
e_bonus = input("Введите премию сотрудника: ")

a = Position(e_name, e_surname, e_position, e_wage, e_bonus)
a.get_full_name()
a.get_total_income()
